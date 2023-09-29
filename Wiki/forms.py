from django import forms
from django.forms import modelformset_factory
from .models import PageTable

class PageForm(forms.ModelForm):
  class Meta:
    model = PageTable
    fields = ("slug", "priority", "public", "edit_permission", "title", "text")
    widgets = {
      'title': forms.TextInput(
        attrs={
          'style': 'width: 100%; height: auto; font-size: 2rem;'
        }
      ),
      'slug': forms.TextInput(
        attrs={
          'style': 'width: 500px;'
        }
      ),
    }


PageSettingsFormSet = modelformset_factory(
  PageTable, 
  fields=(
    "title",
    "slug",
    "priority",
    "public",
    "edit_permission"
  ), 
  extra=0
)
