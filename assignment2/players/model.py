from base64 import b64encode
import environ
from django.db import models

from assignment2.teams.model import Team

class Player(models.Model):
    class Meta:
        db_table = "player"
    id = models.CharField(max_length=30, primary_key=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, db_column="team_id")
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    position =  models.CharField(max_length=30)
    times_trained = models.PositiveIntegerField()
    league = models.URLField(max_length=200)
    team = models.URLField(max_length=200)
    self = models.URLField(max_length=200)

    def save(self, *args, **kwargs):
        env = environ.Env()
        environ.Env.read_env()

        base_id = f"{self.name}:{self.position}"
        self.id = b64encode(base_id.encode()).decode('utf-8')

        base_url = env("BASE_URL")
        self.self = f"{base_url}/players/{self.id}"
        self.league = f"{base_url}/leagues/{self.team_id.league_id.id}"
        self.team = f"{self.self}/teams/{self.team_id.id}"
        super(Player, self).save(*args, **kwargs)
