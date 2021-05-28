from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from .forms import SavePost
from django.contrib.auth.decorators import login_required


def post_list(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id_extra', False)
        form = SavePost(request.POST, request.FILES or None)
        if form.is_valid():
            if not post_id:
                obj = form.save(commit=False)
                obj.save()
            else:
                update_object(request, form, post_id)
        else:
            form.cleaned_data['title'] = None
            update_object(request, form, post_id)

    all_posts = Post.objects.filter(admin_approval=True)
    sorted_posts = all_posts.order_by('title')
    paginator = Paginator(sorted_posts, 3)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts': posts, }
    return render(request, 'index.html', context)


def update_object(request, form, post_id):
    explain_previous = request.POST.get('post_explain_extra', "")
    advantage_previous = request.POST.get('post_adv_extra', "")
    disadvantage_previous = request.POST.get('post_disadv_extra', "")
    similar_previous = request.POST.get('post_similar_extra', "")

    obj = Post.objects.get(id=post_id)
    obj.explain = explain_previous + form.cleaned_data.get('explain')
    obj.adv = advantage_previous + form.cleaned_data.get('adv')
    obj.disadv = disadvantage_previous + form.cleaned_data.get('disadv')
    obj.similar = similar_previous + form.cleaned_data.get('similar')
    obj.save()


class post_detail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def post_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            results = Post.objects.filter(title__icontains=query)
            context = {'results': results, }
            return render(request, 'index.html', context)

        else:
            return render(request, 'index.html')


class PostCreate(generic.CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = 'title', 'explain', 'adv', 'disadv', 'similar', 'image',


def post_edit(request, slug):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('signin')
    form = SavePost()
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post, 'form': form}
    return render(request, 'post_details_edit.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Invalid credentials ")

        else:
            messages.info(request, "Invalid credentials")

    form = AuthenticationForm()
    return render(request, "signin.html", {"form": form})


def category_search(request, category):
    print(request)
    print(category)
    posts = Post.objects.filter(category=category)
    return render(request, "category_search.html", {'posts': posts})


def logout_request(request):
    logout(request)
    return redirect("/")

def wait(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id_extra', False)
        form = SavePost(request.POST, request.FILES or None)
        if form.is_valid():
            if not post_id:
                obj = form.save(commit=False)
                obj.save()
            else:
                update_object(request, form, post_id)
        else:
            form.cleaned_data['title'] = None
            update_object(request, form, post_id)
    return render(request,"waiting_approval.html")