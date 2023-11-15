from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, EditForm


def home(request):
    if request.method == 'GET':
        code = request.GET.get('code', '')
        posts = Post.objects.filter(code=code)
        context = {
            'posts': posts
        }
        return render(request, 'blog/home.html', context)


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(code=post_id)

    if request.method == 'POST':
        if request.POST.get("action") == "Delete":
            post.delete()
        else:
            post.left_boolean = request.POST.get('left_checkbox', False) == 'on'
            post.country_boolean = request.POST.get('country_checkbox', False) == 'on'
            post.city_boolean = request.POST.get('city_checkbox', False) == 'on'
            post.delivered_boolean = request.POST.get('delivered_checkbox', False) == 'on'

            post.save()

        return redirect('/posts/')
    context = {'post': post}
    return render(request, 'blog/edit.html', context)


@login_required
def posts(request):
    on_delivery = Post.objects.filter(delivered_boolean=False)
    delivered = Post.objects.filter(delivered_boolean=True)

    context = {
        'on_delivery': on_delivery,
        'delivered': delivered
    }
    return render(request, 'blog/posts.html', context)


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Ошибка'
    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create.html', context)