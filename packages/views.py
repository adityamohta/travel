# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView
from django.shortcuts import render

from .models import Package
from .forms import PackageCreateForm


def home(request):

    return render(request, "base.html", {})


class PackageCreateView(CreateView):
    model = Package
    template_name = "packages/package_create.html"
    form_class = PackageCreateForm

    # TODO : Add markdown support in future?
    # TODO : Display Field errors in form. its still incomplete.
