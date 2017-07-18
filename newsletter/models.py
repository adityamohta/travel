# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriptions(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=127, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    # TODO 3: maybe add fields like subscribers' interests.

    def __str__(self):
        return self.email
