from django import forms
from .models import *

class Feedback_Form(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name','email','phone_number','city','station','ans1','ans2','ans3','ans4','ans5','textbox']

    def clean(self):
        super(Feedback_Form, self).clean()

        phone_number = self.cleaned_data.get('phone_number')
        textbox = self.cleaned_data.get('textbox')
        
        if len(phone_number) != 10:
            self._errors['phone_number'] = self.error_class(['Phone Number should be of 10 digits'])
        
        if len(textbox)<10 or len(textbox):
            self._errors['textbox'] = self.error_class(['Minimum 10 characters and Maximum 300 characters'])
        
        return self.cleaned_data
    