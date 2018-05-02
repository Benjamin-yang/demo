from django.shortcuts import render, redirect


from cart.models import Post

# Create your views here.

def create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        # 跳转到read，而不是直接render加载
        return redirect('/cart/read/?post_id=%s' % post.id)
        # return render(request, 'create.html', {})
    else:
        return render(request, 'create.html')


def edit(request):
    return render(request, 'edit.html',{})


def read(request):
    post_id = int(request.GET.get('post_id', 1))
    post = Post.objects.get(id=post_id)
    return render(request, 'read.html', {'post':post})


def list(request):
    return render(request, 'post_list.html', {})


def search(request):
    return render(request, 'search.html', {})

