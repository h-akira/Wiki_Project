#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from django.urls import reverse
from bs4 import BeautifulSoup

class Tree:
  def __init__(self, name, data, upper_slug="", top=True, end=False):
    self.name = name
    self.end = end
    if top:
      self.slug=""
    else:
      self.slug = os.path.join(upper_slug, name)
    next_names = []
    next_datas = []
    next_ends = []
    for d in data:
      if d[0] not in next_names:
        next_names.append(d[0])
        next_datas.append([])
        next_ends.append(False)
      if len(d)>1:
        next_datas[next_names.index(d[0])].append(d[1:])
      else:
        next_ends[next_names.index(d[0])]=True
    self.nexts = []
    for _name, _data, _end in zip(next_names, next_datas, next_ends):
      self.nexts.append(Tree(_name, _data, upper_slug=self.slug, top=False, end=_end))

  def gen_html(self, username, prettify=True, top=True, a_class=None):
    text = ""
    if top:
      text += "<ul>"
    text += "<li>"
    if self.end:
      url = reverse('Wiki:detail', args=[username, self.slug])
      if a_class == None:
        text += f'<a href="{url}"> {self.name} </a>'
      else:
        text += f'<a href="{url}" class="{a_class}"> {self.name} </a>'
    else:
      text += self.name
    if len(self.nexts):
      text += "<ul>"
      for next_tree in self.nexts:
        text += next_tree.gen_html(username, prettify=False, top=False, a_class=a_class)
      text += "</ul>"
    text += "</li>"
    if top:
      text += "</ul>"
    if prettify:
      soup = BeautifulSoup(text, "html.parser")
      text = soup.prettify()
    return text
