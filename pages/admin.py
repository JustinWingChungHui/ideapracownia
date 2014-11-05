from django.contrib import admin
from pages.models import Page
from django.db import models
from django.forms import TextInput, Textarea


class PageAdmin(admin.ModelAdmin):
    '''
    Page admin customisation
    '''

    fieldsets = [
              (None, {'fields': ['id','sequence','tab_name','show_on_menu','content']}),
              ('śledzenie',  {'fields':['last_updated_date','creation_date'], 'classes': ['collapse']}),
              ]

    list_display = ('id','sequence','tab_name','last_updated_date','creation_date')
    search_fields = ['tab_name']
    list_filter = ['creation_date','last_updated_date']
    readonly_fields = ('last_updated_date','creation_date','id')

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':25, 'cols':50})},
    }

    class Media:
        from django.conf import settings
        static = settings.STATIC_URL
        js = (
            static+'/js/tinymce/tinymce.min.js ',
            static+'/js/editor.js',
        )

admin.site.register(Page, PageAdmin)