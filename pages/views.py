from django.http import HttpResponse
from django.template import RequestContext, loader
from pages.models import Page

def page_not_found(request):
    '''
    Default page not found view
    '''
    template = loader.get_template('pages/page_not_found.html')
    context = RequestContext(request,{
                                      'pages': Page.objects.order_by('sequence'),
                                      })
    response = template.render(context)
    return HttpResponse(response)


def index(request,requested_tab_name=None):
    '''
    Shows the main pages of the website
    '''

    try:
        if requested_tab_name is None:
            requested_tab_name = Page.objects.order_by('sequence')[:1][0]

        template = loader.get_template('pages/index.html')
        context = RequestContext(request,{
                                      'pages': Page.objects.filter(show_on_menu = 1).order_by('sequence'),
                                      'page': Page.objects.get(tab_name = requested_tab_name),
                                      })
        response = template.render(context)
        return HttpResponse(response)

    except:
        return page_not_found(request)