from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from .models import PageTable
from .forms import PageForm, PageSettingsFormSet
import random
from django.conf import settings
# from django.views.generic import TemplateView
# 独自ライブラリ
from tree import Tree, gen_tree_htmls, gen_pages_ordered_by_tree
from urllib.parse import quote

def index(request):
  if request.user.is_authenticated:
    pages = PageTable.objects.filter(Q(public=True) | Q(user=request.user)).order_by("-last_updated")
  else:
    pages = PageTable.objects.filter(public=True).order_by("-last_updated")
  context = {
    "tree_htmls":gen_tree_htmls(request, User, PageTable, a_white=False),
    "nav_tree_htmls":gen_tree_htmls(request, User, PageTable, a_white=True),
    "pages": pages
  }
  return render(request, 'Wiki/index.html', context)

def share_detail(request, share_code):
  try:
    page = PageTable.objects.get(share_code=share_code)
  except PageTable.DoesNotExist:
    return not_found(request)
  return detail(request, page.user.username, page.slug, share=True)

def detail(request, username, slug, share=False):
  try:
    user = User.objects.get(username=username)
    page = PageTable.objects.get(user=user, slug=slug)
  except User.objects.model.DoesNotExist:
    return not_found(request)
  except PageTable.DoesNotExist:
    if request.user.is_authenticated:
      if user == request.user:
        return redirect("Wiki:create_with_slug",slug=slug)
      else:
        return not_found(request)
    else:
      return not_found(request)
  if not share and not page.public and page.user != request.user:
    return not_found(request)
  if page.user == request.user or (request.user.is_authenticated and page.edit_permission):
    edit = True
  else:
    edit = False
  if page.share:
    share_url = f"{settings.DOMAIN}{reverse('Wiki:share_detail', args=[page.share_code])}"
  else:
    share_url = None
  context = {
    "page": page,
    "username": username,
    "slug": slug,
    "share": share,
    "share_url": share_url,
    "share_code": page.share_code,
    "edit": edit,
    "nav_tree_htmls":gen_tree_htmls(request, User, PageTable, a_white=True),
  }
  return render(request, 'Wiki/detail.html', context)

@login_required
def create(request, slug=None):
  if request.method == 'POST':
    form = PageForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)  # まだDBには保存しない
      instance.user = request.user  # userをセット
      instance.save()  # DBに保存
      if request.POST['action'] == 'update':
        return redirect("Wiki:update",instance.user.username,instance.slug)
      elif request.POST['action'] == 'detail':
        return redirect("Wiki:detail",instance.user.username,instance.slug)
      else:
        raise Exception
  else:
    allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    length=32
    share_code = ''.join(random.choice(allow) for i in range(length))
    form = PageForm(
      initial={
        'slug': slug,
        'share_code': share_code,
      }
    )
    context = {
      "form": form,
      "type": "create",
      "author": True,
      "nav_tree_htmls":gen_tree_htmls(request, User, PageTable, a_white=True)
    }
    return render(request, 'Wiki/edit.html', context)

def share_update(request, share_code):
  page = PageTable.objects.get(share_code=share_code)
  return update(request, page.user.username, page.slug, share=True)

def not_found(request, message="ページが見つかりません"):
  context = {
    "message": message,
  }
  return render(request, 'Wiki/not_found.html', context)

@login_required
def update(request, username, slug, share=False):
  user = User.objects.get(username=username)
  try:
    page = PageTable.objects.get(user=user, slug=slug)
  except PageTable.DoesNotExist:
    return redirect("Wiki:create_with_slug",slug=slug)
  if page.user == request.user or page.edit_permission:
    if request.method == 'POST':
      form = PageForm(request.POST, instance=page)
      if form.is_valid():
        form.save()
        if request.POST['action'] == 'update':
          if share:
            return redirect("Wiki:share_update",page.share_code)
          else:
            return redirect("Wiki:update",username,form.instance.slug)
        elif request.POST['action'] == 'detail':
          if share:
            return redirect("Wiki:share_detail",page.share_code)
          else:
            return redirect("Wiki:detail",username,form.instance.slug)
        else:
          raise Exception
    else:
      if page.user == request.user:
        author = True
      else:
        author = False
      form = PageForm(instance=page)
      context = {
        "id": page.id,
        "username": username,
        "slug": slug,
        "form": form,
        "type": "update",
        "author": author,
        "share": share,
        "share_code": page.share_code,
        "nav_tree_htmls":gen_tree_htmls(request, User, PageTable, a_white=True)
      }
      return render(request, 'Wiki/edit.html', context)
  else:
    return redirect("Wiki:index")

@login_required
def delete(request, id):
  page = get_object_or_404(PageTable, pk=id)
  if request.user == page.user or page.edit_permission:
    page.delete()
  return redirect("Wiki:index")

@login_required
def page_settings(request):
  if request.method == "POST":
    pages = PageTable.objects.filter(user=request.user)
    formset = PageSettingsFormSet(request.POST, queryset=pages)
    if formset.is_valid():
      formset.save()
      if request.POST['action'] == 'continue':
        return redirect("Wiki:page_settings")
      elif request.POST['action'] == 'end':
        return redirect("Wiki:index")
      else:
        raise Exception
    else:
      print("---- Error ----")
      print("formset.errors:")
      print(formset.errors)
      print("formset.management_form.erros:")
      print(formset.management_form.errors)
      print("---------------")
      raise Exception
  else:
    # 階層図の並び順に並び替えられたQuerSet
    pages = gen_pages_ordered_by_tree(request, User, PageTable)
    # 一つのフォームにする
    formset = PageSettingsFormSet(queryset=pages)
    context = {
      "formset": formset,
      "pages": pages,
      "nav_tree_htmls":gen_tree_htmls(request, User, PageTable, a_white=True)
    }
    return render(request, 'Wiki/page_settings.html', context)



