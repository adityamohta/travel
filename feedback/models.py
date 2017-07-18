# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Partner
from django.core.validators import MinValueValidator,MaxValueValidator

# TODO 4: Add a testimonial model here


class Testimonial(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    customer = models.CharField(max_length=255)
    review = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)

    def __str__(self):
        return self.review