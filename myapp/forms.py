from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'summary',
            'price'
        ]



class RawProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(required=False)
    price = forms.DecimalField(decimal_places=2, max_digits=100)
    summary = forms.CharField(max_length=1000)