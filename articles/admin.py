from django.contrib import admin
from articles.models import Article
from django.db import models
from django.forms import TextInput, Textarea



class ArticleAdmin(admin.ModelAdmin):
    '''
    Article admin customisation
    '''

    fieldsets = [
              (None, {'fields': ['id','name','published','header','image','content','author']}),
              ('Tracking',  {'fields':['last_updated_date','creation_date'], 'classes': ['collapse']}),
              ]

    list_display = ('id','name','last_updated_date','creation_date','published')
    search_fields = ['name','header','tagline','content']
    list_filter = ['creation_date','last_updated_date']
    readonly_fields = ('last_updated_date','creation_date','id')

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':50, 'cols':100})},
    }

    #Auto populates author field with current user
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(ArticleAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(Article, ArticleAdmin)