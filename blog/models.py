# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    # image relation
    content = models.TextField()
    draft = models.BooleanField(default=True)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    read_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at", "-updated_at"]
