from django.contrib import admin
from .models import PageTable
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(PageTable, MarkdownxModelAdmin)
