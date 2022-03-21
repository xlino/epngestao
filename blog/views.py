# Create your views here.
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
#def post_list(request):
#    posts=Post.published.all()
#    return render(request, 'blog/post/list.html',{'posts':posts})

#def post_list(request):
#    title = request.GET.get('title', None)
#    author = request.GET.get('author', None)

#    posts = Posts.objects.all()

#    return render(request, 'detail.html', {'posts': posts})

def post_list(request):
    posts=Post.published.all()
#    posts=get_object_or_404(Post, slug=post,status='published',publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'bloglist.html',{'posts':posts})

def post_detail(request, year, month, day, post):
    post=get_object_or_404(Post, slug=post, status='published', publish__year=year, publish_month=month, publish__day=day)
#    posts=get_object_or_404(Post, slug=post,status='published',publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blogdetail.html',{'post':post})
