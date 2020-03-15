from django.db import models

# Create your models here.
class SocialAccount(models.Model):
    ICONS = [
        ("Facebook", "fa-facebook"),
        ("twitter", "fa-twitter"),
        ("Google-plus", "fa-google-plus"),
        ("Linkedin", "fa-linkedin")
        
        
    ]
    
    nom = models.CharField(max_length=255)
    icon = models.CharField(choices=ICONS, max_length=20)
    lien = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social Account'
        verbose_name_plural = 'Social Accounts'

    def __str__(self):
        return self.nom
    
    
class InfoSite(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/InfoSite')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'InfoSite'
        verbose_name_plural = 'InfoSites'

    def __str__(self):
        return self.titre