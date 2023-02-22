from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}! Your account is created')
            return redirect('food:index')
    else:
        form = RegistrationForm()

    # We want to check our request data, and if it is post and valid then we do stuff.
    return render(request, 'users/register.html', {'form': form})
