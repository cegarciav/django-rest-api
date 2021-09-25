from base64 import b64encode
import environ
from django.db import models

from assignment2.leagues.model import League

class Team(models.Model):
    class Meta:
        db_table = "team"
    id = models.CharField(max_length=30, primary_key=True)
    league_id = models.ForeignKey(League, on_delete=models.CASCADE, db_column="league_id")
    name = models.CharField(max_length=30)
    city =  models.CharField(max_length=30)
    league = models.URLField(max_length=200)
    players = models.URLField(max_length=200)
    self = models.URLField(max_length=200)

    def save(self, *args, **kwargs):
        env = environ.Env()
        environ.Env.read_env()

        base_id = f"{self.name}:{self.city}"
        self.id = b64encode(base_id.encode()).decode('utf-8')

        base_url = env("BASE_URL")
        self.self = f"{base_url}/teams/{self.id}"
        self.league = f"{base_url}/leagues/{self.league_id.id}"
        self.players = f"{self.self}/players"
        super(Team, self).save(*args, **kwargs)
