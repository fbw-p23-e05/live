from django.db import models
from django.utils.text import slugify
from sanitizer.models import SanitizedTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = SanitizedTextField(allowed_tags=['a', 'img', 'p'], allowed_attributes=['href', 'src', 'class'], allowed_styles=['width', 'height'])
    published_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    category = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        super(BlogPost, self).save(*args, **kwargs)
        