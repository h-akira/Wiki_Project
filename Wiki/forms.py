from django import forms
from .models import PageTable
from markdownx.widgets import MarkdownxWidget

class PageForm(forms.ModelForm):
  class Meta:
    model = PageTable
    fields = ("slug", "priority", "public", "edit_permission", "title", "text")
    widgets = {
      # 'text': MarkdownxWidget(
        # attrs={
          # 'class': 'dynamic-textarea'
        # }
      # ),
      'title': forms.TextInput(
        attrs={
          'style': 'width: 100%; height: auto; font-size: 1.5rem;'
        }
      ),
      'slug': forms.TextInput(
        attrs={
          'style': 'width: 500px;'
        }
      ),
    }


