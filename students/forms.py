from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model =Student

        fields = [
            'name',
            'email',
            'age',
            'phone',
            'address',
            'course'
        ]

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 18:
            raise forms.ValidationError(
                "Age Must be 18 or above."
            )
        
        return age
    