from django.http import HttpResponse
from django.template import RequestContext, loader
from pages.models import Page
from pages.views import page_not_found
from articles.models import Article

num_article_stubs_per_page = 9

def index(request,page_number_text = '1'):
    '''
    Shows a list of articles with previews
    '''
    try:
        page_number = int(page_number_text)

        #Work out the offset given the gallery page
        offset = num_article_stubs_per_page * (page_number - 1)

        #Gives the total number of gallery pages
        num_pages = (Article.objects.all().count() - 1) // num_article_stubs_per_page + 1 #integer division

        #Ensure that page_number is between reasonable bounds
        page_number = max(1, page_number)
        page_number = min(num_pages, page_number)


        template = loader.get_template('articles/index.html')
        context = RequestContext(request,{
                                      'pages': Page.objects.filter(show_on_menu = 1).order_by('sequence'),
                                      'articles': Article.objects.filter(published = True).order_by('-creation_date')[offset:num_article_stubs_per_page + offset],
                                      'show_previous': (page_number > 1),
                                      'show_next': (page_number < num_pages),
                                      'previous_page': page_number - 1,
                                      'next_page': page_number + 1,
                                      'page_number': page_number_text,
                                      })

        response = template.render(context)
        return HttpResponse(response)

    except:
        return page_not_found(request)



def single_article(request, article_name):
    '''
    Shows a single article
    '''
    try:
        template = loader.get_template('articles/article.html')
        context = RequestContext(request,{
                                  'pages': Page.objects.filter(show_on_menu = 1).order_by('sequence'),
                                  'article': Article.objects.get(name = article_name),
                                  })

        response = template.render(context)
        return HttpResponse(response)

    except:
        return page_not_found(request)
