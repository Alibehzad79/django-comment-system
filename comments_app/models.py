from django.db import models
from django.utils.translation import gettext_lazy as _
from blog_app.models import Article
# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name=_("Article"), related_name="comments")
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    text = models.TextField(verbose_name=_("Comment"))

    class Meta:
        verbose_name  = _("Comment")
        verbose_name_plural = verbose_name + _("s")
        ordering = ['-id']
    
    def __str__(self):
        return self.name