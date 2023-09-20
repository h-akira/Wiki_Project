from django import forms
from .models import PageTable
from markdownx.widgets import MarkdownxWidget

class PageForm(forms.ModelForm):
  class Meta:
    model = PageTable
    fields = ("slug", "public", "title", "text")
    widgets = {
      'text': MarkdownxWidget(
        attrs={
          'rows': 25, 
          'style': 'width: 100%; overflow-y: hidden;',
          'class': 'custom-textarea',
        }
      ),
      'title': forms.TextInput(
        attrs={
          'style': 'width: 100%; height: auto; font-size: 1.5rem;'
        }
      ),
      'slug': forms.TextInput(
        attrs={
          'style': 'width: 100%;'
        }
      ),
      # 'text': MarkdownxWidget(attrs={'rows': 25, 'style': 'width: 100%;'}),
    }


