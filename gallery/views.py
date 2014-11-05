from django.http import HttpResponse
from django.template import RequestContext, loader
from gallery.models import Photo
from pages.models import Page
from pages.views import page_not_found

num_photos_on_page = 9

def index(request,page_number_text='1'):
    '''
    Shows the main gallery
    Show 9 photos on a page
    '''
    try:
        page_number = int(page_number_text)

        #Work out the offset given the gallery page
        offset = num_photos_on_page * (page_number - 1)

        #Gives the total number of gallery pages
        num_pages = (Photo.objects.all().count() - 1) // num_photos_on_page + 1 #integer division

        #Ensure that page_number is between reasonable bounds
        page_number = max(1, page_number)
        page_number = min(num_pages, page_number)


        template = loader.get_template('gallery/index.html')
        context = RequestContext(request,{
                                      'pages': Page.objects.filter(show_on_menu = 1).order_by('sequence'),
                                      'images': Photo.objects.all().order_by('-creation_date')[offset:num_photos_on_page + offset],
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



def single_photo(request,photo_id = 1):
    '''
    Brings up a page to display one photo
    '''

    try:

        photo = Photo.objects.get(id = photo_id)

        #Used to find the gallery page the photo is on
        photo_row_index = Photo.objects.filter(creation_date__gte = photo.creation_date).count()

        template = loader.get_template('gallery/single_photo.html')
        context = RequestContext(request,{
                                      'pages': Page.objects.filter(show_on_menu = 1).order_by('sequence'),
                                      'photo': photo,
                                      'gallery_page': (photo_row_index - 1)  // num_photos_on_page + 1,
                                      })

        response = template.render(context)
        return HttpResponse(response)

    except:
        return page_not_found(request)