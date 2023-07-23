from django import forms
from .models import Garbage





class ProductUploadForm(forms.ModelForm):

    class Meta:
        model=Garbage
        fields='__all__'
        exclude=['uploaded_by','slug','status',]
         
    def __init__(self,*args,**kwargs):
        super(ProductUploadForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control','placeholder': 'Garbage Name'})
        self.fields['desc'].widget.attrs.update({ 'rows':3, 'class': 'form-control','placeholder': 'Garbage description'})
        self.fields['weight'].widget.attrs.update({'class': 'form-control','placeholder': 'Approximate Weight Garbage Ex: 500kg Pape'})