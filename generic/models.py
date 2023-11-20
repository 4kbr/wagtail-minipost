from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

# Create your models here.
class GenericPage(Page):
  banner_title = models.CharField(
    max_length=100,
    default='Welcome to my generic page',
  )

  introduction = models.TextField(blank=True)

  content_panels = Page.content_panels + [
    FieldPanel("banner_title"),
    FieldPanel("introduction"),
  ]