from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import PageTable
from .forms import PageForm

def index(request):
  context = {
    "tree":None
  }
  return render(request, 'Wiki/index.html', context)

def detail(request, username, slug):
  user = User.objects.get(username=username)
  page = PageTable.objects.get(user=user, slug=slug)
  context = {
    "page": page,
    "username": username,
    "slug": slug
  }
  return render(request, 'Wiki/detail.html', context)

def create(request):
  if request.method == 'POST':
    form = PageForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)  # まだDBには保存しない
      instance.user = request.user  # userをセット
      instance.save()  # DBに保存
    return redirect("Wiki:detail",instance.user.username,instance.slug)
  else:
    form = PageForm()
    context = {
      "form": form,
      "type": "create",
    }
    return render(request, 'Wiki/edit.html', context)
    
def update(request, username, slug):
  user = User.objects.get(username=username)
  # page = PageTable.objects.get(user=user, slug=slug)
  page = get_object_or_404(PageTable, user=user, slug=slug)
  if request.method == 'POST':
    form = PageForm(request.POST, instance=page)
    if form.is_valid():
      form.save()
    return redirect("Wiki:detail",username,form.instance.slug)
  else:
    form = PageForm(instance=page)
    context = {
      "id": page.id,
      "username": username,
      "slug": slug,
      "form": form,
      "type": "update"
    }
    return render(request, 'Wiki/edit.html', context)

def delete(request, id):
  page = get_object_or_404(PageTable, pk=id)
  page.delete()
  return redirect("Wiki:index")
