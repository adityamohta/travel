from django import forms

from .models import Package


class PackageCreateForm(forms.ModelForm):

    class Meta:
        model = Package
        fields = [
            "partner",
            "title",
            "description",
            "price",
            "category",
        ]

    def __init__(self, *args, **kwargs):
        super(PackageCreateForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'

        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'

        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['placeholder'] = 'Category'
