from django.db import models

# Create your models here.
class Notification(models.Model):
    content = models.CharField(max_length=500)
    sent_on = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_on']
    
    def __str__(self):
        return f"sent onj {self.content}"
    



