#import blog
import blog
from blog.forms import CreateBlogForm
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog_detail': blog_detail})

def create(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
        return redirect('/detail/'+str(blog.id)) #여기는 왜 str로 보내는거지?.?
    else:
        form = CreateBlogForm()  #얘는 여기서 멀하는뎅...?.?
    return render(request, 'create.html', {'form': form})

def edit(reqeust, blog_id):
    edit_blog = Blog.objects.get(id = blog_id)
    return render(reqeust, 'edit.html',{'blog': edit_blog})

def update(request, blog_id):
    blog = Blog.objects.get(id= blog_id)
    if request.method == "POST":
        form = CreateBlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('/detail/'+str(blog.id))
    else:
        form = CreateBlogForm(instance=blog)
        return render(request, 'create.html', {'form': form})

def delete(request, blog_id):
    blog = Blog.objects.get(id= blog_id)
    blog.delete()
    return redirect('home')

# def create_blog(reqeust):
#     blog = Blog()
#     blog.title = request.GET['title']
#     blog.writer = reqeust.GET['writer']
#     blog.pub_date = timezone.datetime.now()
#     blog.todo = request.GET['todo']
#     blog.body = reqeust.GET['body']
#     blog.save()
#     return redirect('/detail/'+str(blog.id))  #여기는 왜 str로 보내는거지?.?
