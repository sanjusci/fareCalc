from django.db import models

class Address(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    owner = models.ForeignKey('auth.User',default="1", related_name='api')
    
    class Meta:
        ordering = ('created',)

class Location(models.Model):
    entity_id = models.TextField()
    entity_type = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User',default="1", related_name='loc')
        
    class Meta:
        ordering = ('created',)
