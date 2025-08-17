from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import EmailSubscriptionForm
import json

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        
        # Handle AJAX requests
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            form = EmailSubscriptionForm(data)
            
            if form.is_valid():
                email = form.cleaned_data['email']
                # Save email to database or send to email service
                # For now, just return success
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you! Your email has been added to our waiting list.'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
        
        # Handle regular form submission
        if form.is_valid():
            email = form.cleaned_data['email']
            # TODO: Save email logic here (database, email service, etc.)
            messages.success(request, 'Thank you! Your email has been added to our waiting list.')
            return redirect('home')
        else:
            # Form has errors, render with errors
            return render(request, 'home/home.html', {'form': form})
    
    else:
        form = EmailSubscriptionForm()
    
    return render(request, 'home/home.html', {'form': form})