# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

#Represents an article
class Article(models.Model):

    class Meta:
        verbose_name = u'Aktualności Artykuł'
        verbose_name_plural = u'Artykuły Prasowe'

    name = models.CharField(max_length=255, unique=True, blank = False, db_index = True, null = False, verbose_name = 'Nazwa Unque')
    header = models.CharField(max_length=255,blank = False, null = False, verbose_name = 'Nagłówek')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name = 'Zdjęcie 16:9 stosunek',null=True, blank=True)
    content = models.TextField(blank = True, verbose_name = 'Zawartość')
    published = models.BooleanField(default=False, db_index=True, verbose_name = 'Opublikowany')
    author = models.ForeignKey(User,null=True, blank=True, verbose_name = 'Autor')

    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name ='Data Utworzenia')
    last_updated_date = models.DateTimeField(auto_now=True, verbose_name ='Data Ostatniej Aktualizacji')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        #format name so it can be used for URLs
        import re
        self.name = re.sub(r'\W+', '', self.name.lower())
        super(Article, self).save(*args, **kwargs)



