from django.db import models
class HopeStory(models.Model):
    CATEGORY_CHOICES = [
    ('depression', 'Depression Recovery'),
    ('anxiety', 'Anxiety Management'),
    ('grief', 'Grief and Loss'),
    ('trauma', 'Trauma Recovery'),
    ('addiction', 'Addiction Recovery'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    preview = models.TextField(max_length=500)
    full_story = models.TextField()
    author_pseudonym = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Hope Stories"
        ordering = ['-created_at']
    def __str__(self):
        return self.title