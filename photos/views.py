from models import Gallery, Photo, Category
from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404

def gallery(request, req_name):
    gallery = get_object_or_404(Gallery, name=req_name)
    return render_to_response('photos/gallery.html', \
                            {'gallery': gallery})

def gallery_list(request, req_name):
    cat = get_object_or_404(Category, slug=req_name)
    galleries = sorted(get_list_or_404(Gallery, category=cat), 
                        key=Gallery.date, reverse=True)
    return render_to_response('photos/gallery_list.html', \
                        {'galleries': galleries})
