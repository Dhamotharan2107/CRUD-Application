
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BlogsForm
from .models import Blogs
from django.db.models import Q



# Create your views here.
def home(request):
    blogs = Blogs.objects.all()
    context={
        "blogs":blogs
    }
    return render(request, 'index.html', context)

def create_post(request):
    if request.method == 'POST':
        form = BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogsForm()
    return render(request, 'create_post.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Blogs, pk=pk)
    if request.method == 'POST':
        form = BlogsForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogsForm(instance=task)
    return render(request, 'edit_blogs.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Blogs, pk=pk)
    task.delete()
    return redirect('home')

# def filter(request):
#     filter = request.GET.get('search')
#     blogs = Blogs.objects.filter(author__icontains=filter) or  Blogs.objects.filter(tags__icontains=filter)
#     # blogs = Blogs.objects.filter(Q(author__icontains=filter) | Q(tags__icontains=filter))
#     return render(request, 'index.html', {'blogs':blogs})

def filter(request):
    search_term = request.GET.get('search')
    fields = ['author', 'tags', 'title', ]
    pop = (
        blog for field in fields for blog in Blogs.objects.filter(**{f"{field}__icontains": search_term})
    )
    return render(request, 'index.html', {'blogs': pop})





