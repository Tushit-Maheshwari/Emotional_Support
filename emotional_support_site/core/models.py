from django.db import models
from django.contrib.auth.models import User
class CrisisHotline(models.Model):
    country = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.country}: {self.number}"
class SelfAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    assessment_date = models.DateTimeField(auto_now_add=True)
    mood_score = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    anxiety_level = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    notes = models.TextField(blank=True)
    class Meta:
        ordering = ['-assessment_date']