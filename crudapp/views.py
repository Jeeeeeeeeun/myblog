from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Post, Scrap, Like
from .form import PostForm

# Create your views here.

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})

def show(request, post_id) :
    post = get_object_or_404(Post, pk=post_id)
    scrap = Scrap.objects.filter(user=request.user, post=post)
    like =  Like.objects.filter(user=request.user, post=post)
    return render(request, 'show.html', {'post': post, 'scrap':scrap, 'like':like})

def new(request) :
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form':form})

def edit(request) :
    return render(request, 'edit.html')


def postupdate(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('show', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form': form})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('main')

def scrap(request, post_id) :
    post = get_object_or_404(Post, pk=post_id)
    scrapped = Scrap.objects.filter(user=request.user, post=post)
    if not scrapped:
        Scrap.objects.create(user=request.user, post=post)
    else:
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def like(request, post_id) :
    post = get_object_or_404(Post, pk=post_id)
    liked = Like.objects.filter(user=request.user, post=post)
    if not liked:
        Like.objects.create(user=request.user, post=post)
    else:
        liked.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
