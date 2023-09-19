from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import PageTable
from .forms import PageForm
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import lib

def index(request):
  if request.user.is_authenticated:
    pages = PageTable.objects.filter(Q(public=True) | Q(user=request.user)).order_by("-last_updated")
  else:
    pages = PageTable.objects.filter(public=True).order_by("-last_updated")
  context = {
    "tree_htmls":lib.wiki.gen_tree_htmls(request, User, PageTable, a_white=False),
    "nav_tree_htmls":lib.wiki.gen_tree_htmls(request, User, PageTable, a_white=True),
    "pages": pages
  }
  return render(request, 'Wiki/index.html', context)

def detail(request, username, slug):
  user = User.objects.get(username=username)
  page = PageTable.objects.get(user=user, slug=slug)
  if not page.public and page.user != request.user:
    return redirect("Wiki:index")
  if page.user == request.user:
    edit = True
  else:
    edit = False
  context = {
    "page": page,
    "username": username,
    "slug": slug,
    "edit": edit,
    "nav_tree_htmls":lib.wiki.gen_tree_htmls(request, User, PageTable, a_white=True)
  }
  return render(request, 'Wiki/detail.html', context)

@login_required
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
      "nav_tree_htmls":lib.wiki.gen_tree_htmls(request, User, PageTable, a_white=True)
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
    if page.user != request.user:
      return redirect("Wiki:index")
    form = PageForm(instance=page)
    context = {
      "id": page.id,
      "username": username,
      "slug": slug,
      "form": form,
      "type": "update",
      "nav_tree_htmls":lib.wiki.gen_tree_htmls(request, User, PageTable, a_white=True)
    }
    return render(request, 'Wiki/edit.html', context)

@login_required
def delete(request, id):
  page = get_object_or_404(PageTable, pk=id)
  if request.user == page.user:
    page.delete()
  return redirect("Wiki:index")
