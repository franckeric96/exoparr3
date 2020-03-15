from django.db import models

# Create your models here.
class Event(models.Model):
    
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Event")
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.nom
    
    
class Admission(models.Model):
    
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.URLField()
    numero = models.IntegerField()
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Admission'
        verbose_name_plural = 'Admissions'

    def __str__(self):
        return self.nom
    
    
class Courses(models.Model):
    
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Courses")
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.titre