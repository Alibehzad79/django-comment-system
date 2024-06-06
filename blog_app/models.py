from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content")) # You can use django-ckeditor package for advanced projects

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = verbose_name + _("s")
        ordering = ['-id']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"pk": self.id})