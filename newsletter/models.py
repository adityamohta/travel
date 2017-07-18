# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriptions(models.Model):
    email = models.EmailField()
    # maybe add fields like subscribers' interests.

    def __str__(self):
        return self.email
