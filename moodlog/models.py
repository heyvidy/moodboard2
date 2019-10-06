from django.db import models
from django.contrib.auth.models import User


class Mood(models.Model):
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.emoji} {self.name}"

    def natural_key(self):
        return {"id": self.id, "emoji": self.emoji, "name": self.name}


class Action(models.Model):
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.emoji} {self.name}"

    def natural_key(self):
        return {"id": self.id, "emoji": self.emoji, "name": self.name}


class MoodLog(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.SET_NULL, null=True)
    action = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True)
    note = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.mood} | {self.timestamp}"
