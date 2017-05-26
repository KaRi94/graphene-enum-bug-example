from django.db import models


class Page(models.Model):
    TYPES = (
        ('ARTICLE', 'Article'),
    )
    type = models.CharField(max_length=255, choices=TYPES)
    
    
class SubPage(Page):
    pass
