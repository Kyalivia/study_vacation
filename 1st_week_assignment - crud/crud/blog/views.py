from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Blog
from .forms import Create


def read(request):
    blogs = Blog.objects.order_by('-id')
    return render(request, 'blog/read.html', {'blogs': blogs})

def create(request):
    if request.method == 'POST':
        form = Create(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('read') 
    else:
        form = Create()
        return render(request, 'blog/create.html', {'form':form})
       

def update(request, pk):
        blog = get_object_or_404(Blog, pk=pk)

        if request.method == "POST":
                form = Create(request.POST, instance=blog) 

                if form.is_valid(): 
                        blog = form.save(commit=False) 
                        blog.update_date=timezone.now() 
                        blog.save()
                        return redirect('read') 

        else:
                form = Create(instance=blog) 
                return render(request, 'blog/update.html',{'form' : form})

def delete(request, pk):
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('read')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})