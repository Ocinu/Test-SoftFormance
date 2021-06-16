from django.shortcuts import render
from .models import FeedItem, RegisteredUser


def index(request):
    current_user = request.user
    items = FeedItem.objects.all()
    content = {
        'current_user': current_user,
        'title': 'Main Page',
        'items': items,
    }
    return render(request, 'index.html', content)

def tracking_posts(request):
    current_user = request.user
    tracking = RegisteredUser.objects.filter(post_authors=request.user)
    content = {
        'items': tracking,
        'current_user': current_user,
    }
    return render(request, 'index.html', content)


def my_posts(request):
    current_user = request.user
    items = FeedItem.objects.filter(user=request.user)
    content = {
        'items': items,
        'current_user': current_user,
    }
    return render(request, 'index.html', content)


def following(request):
    pass
