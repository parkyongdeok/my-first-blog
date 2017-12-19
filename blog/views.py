from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('title')
    return render(request, 'blog/post_list.html', {'posts':posts})


#Post.objects.order_by('published_date')
