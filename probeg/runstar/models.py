from django.db import models


from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class TrainingPlanPage(Page):
    date = models.DateField()
    description = RichTextField()
    total_km = models.DecimalField(max_digits=5, decimal_places=2)
    wellness = models.IntegerField()
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('description'),
        FieldPanel('total_km'),
        FieldPanel('wellness'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        return context


class BiographyPage(Page):
    body = RichTextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('image'),
    ]

