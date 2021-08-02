from django.shortcuts import render,redirect,get_object_or_404
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book

from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.views.generic import ListView


# Create your views here.

class tagview(ListView):
    model=Book
    template_name='books.html'
    context_object_name='tags'

    def get_queryset(self):
        print(self.kwargs.get('tag_slug'))
        print(type(self.kwargs.get('tag_slug')))
        ob=Book.objects.filter(tags__name__in=[self.kwargs.get('tag_slug')])
        print(ob)
        return ob
    
def booklist(request):
    books =Book.objects.all()
    #post = get_object_or_404(Book)
    return render(request,'books.html',{'books':books})

def uploadbook(request):
    if request.method == 'POST':
        print("Post method execution")
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            #newpost.slug = slugify(newpost.title)
            newpost.save()
            form.save_m2m()
            return redirect(booklist)
    else:
        print("Else block execution")
        form=BookForm()
    return render(request,'uploadbook.html',{'form':form})
