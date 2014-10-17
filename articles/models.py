
from django.db import models
from django.contrib.auth.models import User

#Represents an article
class Article(models.Model):

    name = models.CharField(max_length=255, unique=True, blank = False, db_index = True, null = False, verbose_name = 'slug (unique)')
    header = models.CharField(max_length=255,blank = False, null = False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name = 'Image 16:9 ratio',null=True, blank=True)
    content = models.TextField(blank = True)
    published = models.BooleanField(default=False, db_index=True)
    author = models.ForeignKey(User,null=True, blank=True)

    #Tracking
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        #format name so it can be used for URLs
        import re
        self.name = re.sub(r'\W+', '', self.name.lower())
        super(Article, self).save(*args, **kwargs)



