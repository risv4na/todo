from django import forms
from product_app.models import ProductDetails

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = '__all__'