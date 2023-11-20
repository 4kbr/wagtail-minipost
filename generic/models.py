from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks



# Create your models here.
class GenericPage(Page):
  banner_title = models.CharField(
    max_length=100,
    default='Welcome to my generic page',
  )
  introduction = models.TextField(blank=True)
  banner_image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name='+',
  )

  author = models.ForeignKey(
    'Author',
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name='+',
  )
  body = StreamField([
    # ('name', blocks.SomthingBloc())
    ('heading',blocks.CharBlock(template='heading_block.html')),
    ('image',ImageChooserBlock()),
    ('paragraph',blocks.RichTextBlock()),
  ], use_json_field=True,null = True)

  content_panels = Page.content_panels + [
    FieldPanel("banner_title"),
    FieldPanel("introduction"),
    FieldPanel("banner_image"),
    FieldPanel("author"),
    FieldPanel("body"),
    # Panel in here
  ]

@register_snippet
class Author(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(blank=True, max_length=100)
  company_name = models.CharField(blank=True, max_length=100)
  company_url = models.CharField(blank=True, max_length=100)
  image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    null=True,
    blank=False,
    related_name='+'
  )

  panels = [
    FieldPanel("name"),
    FieldPanel("title"),
    FieldPanel("company_name"),
    FieldPanel("company_url"),
    FieldPanel("image"),
  ]

  def __str__(self) -> str:
    return self.name;