from django.db import models

class Page(models.Model):

    tab_name = models.CharField(max_length=25, unique=True, blank = False, db_index = True, null = False, verbose_name = 'Tab Name')
    sequence = models.IntegerField(unique=True, null = False, db_index = True)
    content = models.TextField(blank = True)

    def __unicode__(self):
        return self.tab_name

    def __str__(self):
        return self.tab_name