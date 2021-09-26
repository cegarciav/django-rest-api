from base64 import b64encode
from django.db import models
import environ

class League(models.Model):
    class Meta:
        db_table = "league"
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    sport =  models.CharField(max_length=200)
    teams = models.URLField(max_length=200)
    players = models.URLField(max_length=200)
    self = models.URLField(max_length=200)

    def save(self, *args, **kwargs):
        env = environ.Env()
        environ.Env.read_env()

        base_id = f"{self.name}:{self.sport}"
        self.id = b64encode(base_id.encode()).decode('utf-8')

        base_url = env("BASE_URL")
        self.self = f"{base_url}/leagues/{self.id}"
        self.teams = f"{self.self}/teams"
        self.players = f"{self.self}/players"
        super(League, self).save(*args, **kwargs)
