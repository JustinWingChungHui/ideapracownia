# encoding: utf-8
from django.db import models

class Photo(models.Model):
    '''
    Represents a photo that can be used across entire website
    '''
    class Meta:
        verbose_name = u'Zdjęcie'
        verbose_name_plural = u'Zdjęcia'

    title = models.CharField(blank=False, max_length=255, db_index = True, verbose_name = 'Tytuł')
    caption = models.CharField(blank=True, max_length=255, verbose_name = 'Podpis')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name = 'Obraz 16:9 stosunek')
    photographer = models.CharField(blank=True, max_length=255, verbose_name ='Fotograf')

    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name ='Data Utworzenia')
    last_updated_date = models.DateTimeField(auto_now=True, verbose_name ='Data Ostatniej Aktualizacji')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
