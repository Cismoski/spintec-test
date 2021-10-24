from django.db import models


class BaseModel(models.Model):
    """A base model that declares both "created_at" and "updated_at" fields."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=256)


class News(BaseModel):
    author = models.ForeignKey(to=Author, related_name='news', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256)
    body = models.TextField(max_length=8192)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
