# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import Partner


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title


class Package(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(help_text="Add your product description here.")
    # TODO : some destinations field? think about it.
    # TODO : add images field?
    price = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.ManyToManyField(Category, blank=True)     # do we need this field? Not sure...
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
            we must have a get_absolute_url() function because 
            PackageCreateView search for it in this Model, 
            so it can redirect to the given url after creating Object.
        :return: Package url.
        """
        # TODO : Fix this later.
        return '/'
