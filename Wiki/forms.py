from django import forms
from .models import PageTable
from markdownx.widgets import MarkdownxWidget

class PageForm(forms.ModelForm):
  class Meta:
    model = PageTable
    fields = ("slug", "title", "text")
    widgets = {
      'text': MarkdownxWidget(),
    }


