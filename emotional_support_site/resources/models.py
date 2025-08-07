from django.db import models
class CopingStrategy(models.Model):
    CATEGORY_CHOICES = [
        ('anxiety', 'Anxiety'),
        ('depression', 'Depression'),
        ('grief', 'Grief'),
        ('stress', 'Stress'),
        ('general', 'General'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    steps = models.TextField()
    difficulty_level = models.IntegerField(choices=[(i, i) for i in range(1, 4)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class BreathingExercise(models.Model):
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    duration_minutes = models.IntegerField()
    def __str__(self):
        return self.name