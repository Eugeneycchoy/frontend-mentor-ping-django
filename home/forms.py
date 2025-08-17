from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import re

class EmailSubscriptionForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'max-sm:w-full bg-[white] text-preset-3-light w-[421px] border-[1px] border-[solid] border-[#c2d3ff] px-[32px] py-[18px] rounded-[100px] text-[#c2d3ff]',
            'placeholder': 'Your email address...',
            'id': 'email',
            'autocomplete': 'email',
            'aria-describedby': 'email-error',
        }),
        error_messages={
            'required': 'Please provide a valid email address',
            'invalid': 'Whoops! It looks like you forgot to add a valid email',
        }
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Additional custom validation
        if email:
            # Check for basic email pattern
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                raise ValidationError("Whoops! It looks like you forgot to add a valid email")
            
            # Check for common disposable email domains (optional)
            disposable_domains = ['10minutemail.com', 'tempmail.org', 'guerrillamail.com']
            domain = email.split('@')[1].lower()
            if domain in disposable_domains:
                raise ValidationError("Please use a valid email address")
        
        return email
