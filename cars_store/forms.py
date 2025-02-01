from django import forms
from .models import Category, Goods

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', )

class GoodsForms(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('title', 'description', 'photo', 'price',)
        read_only_fields = ('category',)