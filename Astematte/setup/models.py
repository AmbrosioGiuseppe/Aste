from django.db import models

# Create your models here.

class Menu (models.Model):
    nomeMenu            = models.CharField(max_length=500,blank=True,null=True)
    slugUrl             = models.CharField(max_length=500,blank=True,null=True)
    url                 = models.CharField(max_length=500,blank=True,null=True)
    attivo              = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return str(self.nomeMenu)