# encoding: utf-8
from django.db import models

class Page(models.Model):

    class Meta:
        verbose_name = u'Strona'
        verbose_name_plural = u'Strony'

    tab_name = models.CharField(max_length=25, unique=True, blank = False, db_index = True, null = False, verbose_name = 'Nazwa Tab')
    tab_link = models.CharField(max_length=25, unique=True, blank = False, db_index = True, null = False)

    sequence = models.IntegerField(unique=True, null = False, db_index = True, verbose_name ='Sekwencja')
    content = models.TextField(blank = True, verbose_name ='Zawartość')
    show_on_menu = models.BooleanField(default=True, db_index = True, null = False, verbose_name ='Pokaż na menu')

    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name ='Data Utworzenia')
    last_updated_date = models.DateTimeField(auto_now=True, verbose_name ='Data Ostatniej Aktualizacji')

    def __unicode__(self):
        return self.tab_name

    def __str__(self):
        return self.tab_name

    def save(self, *args, **kwargs):

        #format name so it can be used for URLs
        import re
        self.tab_link = re.sub('[\W_]+', '', self.tab_name.lower())
        super(Page, self).save(*args, **kwargs)