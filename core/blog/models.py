from django.contrib.auth.models import User
from django.db import models

options = {
    ("draft", "Draft"),
    ("published", "Published"),
    ("review", "Review"),
}


class Post(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True, editable=False
    )
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=options, default="draft"
    )

    class Meta:
        ordering = ("-created_on",)

    def __str__(self):
        return self.name
