#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .tree import Tree

def gen_tree_htmls(request, User, PageTable, a_white=True):
  htmls = []
  users = User.objects.all()
  for user in users:
    if request.user.is_authenticated:
      if user == request.user:
        pages = PageTable.objects.filter(user=user)
      else:
        pages = PageTable.objects.filter(user=user, public=True)
    else:
      pages = PageTable.objects.filter(user=user, public=True)
    pages = pages.order_by('-priority')
    data = []
    for page in pages:
      data.append(page.slug.split("/"))
    tree = Tree(user.username, data=data)
    if a_white:
      htmls.append(tree.gen_html(user.username, a_class="a-white"))
    else:
      htmls.append(tree.gen_html(user.username))
  return htmls
