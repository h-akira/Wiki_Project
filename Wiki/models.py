from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class PageTable(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  slug = models.CharField(max_length=127)
  title = models.CharField(max_length=127)
  # text = models.TextField(null=True, blank=True)
  text = MarkdownxField(null=True, blank=True)
  def get_text_markdownx(self):
    return mark_safe(markdownify(self.text))
  def __str__(self):
    return self.title




