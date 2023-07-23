from django import forms
from .models import Order




class OrderForm(forms.ModelForm):

    class Meta:
        model=Order
        fields=['contact','location','price','payment_method','transection_no',]
    
    def __init__(self,*args,**kwargs):
        super(OrderForm,self).__init__(*args,**kwargs)
        self.fields['contact'].widget.attrs.update({'class': 'form-control','placeholder': 'contact no'})
        self.fields['location'].widget.attrs.update({'class': 'form-control','placeholder': 'Your location'})
        self.fields['price'].widget.attrs.update({'class': 'form-control','placeholder': 'price'})
        self.fields['transection_no'].widget.attrs.update({'class': 'form-control','placeholder': 'transection non ex: T35F3F'})