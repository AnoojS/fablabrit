from django import forms

from .models import Component,Material,Tool


class ComponentForm(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'item',
        'data-val': 'true',
        'data-val-required': 'Please enter item',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'description',
        'data-val': 'true',
        'data-val-required': 'Please enter description',
    }))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'quantity',
        'data-val': 'true',
        'data-val-required': 'Please enter quantity',
    }))


class MaterialForm(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'item',
        'data-val': 'true',
        'data-val-required': 'Please enter item',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'description',
        'data-val': 'true',
        'data-val-required': 'Please enter description',
    }))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'quantity',
        'data-val': 'true',
        'data-val-required': 'Please enter quantity',
    }))    


class ToolForm(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'item',
        'data-val': 'true',
        'data-val-required': 'Please enter item',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'description',
        'data-val': 'true',
        'data-val-required': 'Please enter description',
    }))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'quantity',
        'data-val': 'true',
        'data-val-required': 'Please enter quantity',
    }))