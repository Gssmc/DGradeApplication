from django import forms
#from .models import Complain




'''
class ComplainForm(forms.ModelForm):

    class Meta:
        model=Complain
        fields=['title','desc']
         
    def __init__(self,*args,**kwargs):
        super(ComplainForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control','placeholder': 'Garbage Name'})
        self.fields['desc'].widget.attrs.update({ 'rows':3, 'class': 'form-control','placeholder': 'Garbage description'})
'''