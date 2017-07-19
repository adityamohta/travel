# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import Partner


class Testimonial(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=255)
    review = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
