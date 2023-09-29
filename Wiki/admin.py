from django.contrib import admin
from django.db import models
from .models import PageTable
from mdeditor.widgets import MDEditorWidget

class PageTableAdmin(admin.ModelAdmin):
  formfield_overrides = {
    models.TextField: {'widget': MDEditorWidget}
  }

admin.site.register(PageTable, PageTableAdmin)
