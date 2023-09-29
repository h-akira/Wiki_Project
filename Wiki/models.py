from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# import markdown as md
from mdeditor.fields import MDTextField # 追加

class PageTable(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  last_updated = models.DateTimeField(auto_now=True)
  slug = models.CharField(max_length=127)
  priority = models.FloatField(default=0)
  title = models.CharField(max_length=127)
  public = models.BooleanField(default=True)
  edit_permission = models.BooleanField(default=False)
  text = MDTextField(null=True, blank=True) # 変更
  # test_text = MDTextField(null=True, blank=True) # 変更
  # def get_text_markdownx(self):
    # return md.markdown(self.text, extensions=settings.MARKDOWN_EXTENSIONS)
  def __str__(self):
    return self.title
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=["user", "slug"],
        name="slug_unique"
      )
    ]




