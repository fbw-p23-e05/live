from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            # Create a new user object without saving it
            new_user = registration_form.save(commit=False)
            # Set the user password
            new_user.set_password(
                registration_form.cleaned_data['password'])
            # Save the user object
            new_user.save()
            return redirect('account:login')
    else:
        registration_form = UserRegistrationForm()
    
    return render(request, "account/register.html", {"form": registration_form})
