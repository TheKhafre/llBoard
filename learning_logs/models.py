from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
    
class Entry(models.Model):

    """CASCADE tells it to delete everything under it 
    once the topic is deleted"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class meta:
        """Change the name to entries once there are more than one entry"""
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        """return the first 50 character of the topic and ..."""
        return f"{self.text[:50]}..."