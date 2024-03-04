from django.db import models

# Create your models here.
class MyMessages(models.Model):
    message  = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    def serialize(self):
        return {
            'id': self.pk,
            'message': self.message,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }