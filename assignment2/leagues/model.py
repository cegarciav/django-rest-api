from base64 import b64encode
from django.db import models

class League(models.Model):
    class Meta:
        db_table = "league"
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    sport =  models.CharField(max_length=30)
    teams = models.URLField(max_length=200)
    players = models.URLField(max_length=200)
    self = models.URLField(max_length=200)

    def save(self, *args, **kwargs):
        base_id = f"{self.name}:{self.sport}"
        self.id = b64encode(base_id.encode()).decode('utf-8')
        super(League, self).save(*args, **kwargs)
