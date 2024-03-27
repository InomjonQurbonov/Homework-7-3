from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MembersForm, NewsForm, DeleteConfirmationForm
from .models import News, Users, Members


def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about_us/about_us.html')


def our_works(request):
    return render(request, 'our_works/our_works.html')


def law(request):
    return render(request, 'our_works/international_law.html')


def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news_list': news})


def news_detail(request, pk):
    News.objects.filter(pk=pk).update(views_count=F('views_count') + 1)
    new = News.objects.get(id=pk)
    return render(request, 'news/about_news.html', {'new_detail': new})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        news = form.save()
        return redirect('add_news')
    form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})


def edit_news(request, pk):
    this_news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=this_news)
        if form.is_valid():
            form.save()
            return redirect('news_detail', pk=this_news.pk)
    else:
        form = NewsForm(instance=this_news)
    return render(request, 'news/edit_news.html', {'form': form, 'news': this_news})


def delete_news(request, pk):
    this_new = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        this_new.delete()
        return redirect('news_list')
    else:
        form = DeleteConfirmationForm()
    return render(request, 'news/delete_html.html', {'form': form})




# register form
def new_user(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        new_user = Users(full_name=full_name, email=email, password=password, phone=phone)
        new_user.save()
        return redirect('add_news', pk=new_user.pk)
    else:
        return render(request, 'login_form/register.html')


def members_list(request):
    members = Members.objects.all()
    return render(request, "about_us/our_members.html", {'members': members})


def members_details(request, pk):
    members = Members.objects.get(pk=pk)
    return render(request, 'about_us/member_info.html', {'members': members})


def add_members(request):
    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES)
        members = form.save()
        return redirect('add_members')
    form = MembersForm()
    return render(request, 'about_us/add_members.html', {'form': form})


def edit_members(request, pk):
    this_member = get_object_or_404(Members, pk=pk)
    if request.method == 'POST':
        form = MembersForm(request.POST, instance=this_member)
        if form.is_valid():
            form.save()
            return redirect('members_details', pk=this_member.pk)
    else:
        form = MembersForm(instance=this_member)
    return render(request, 'about_us/edit_members.html', {'form': form, 'member': this_member})

def delete_members(request, pk):
    this_member = get_object_or_404(Members, pk=pk)
    if request.method == 'POST':
        this_member.delete()
        return redirect('members_list')
    else:
        form = DeleteConfirmationForm()
    return render(request, 'about_us/delete_members.html', {'form': form, 'member': this_member})

