from django.db import models


class Todo(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    font_size = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.text

    def text_preview(self):
        return self.text[:50]
