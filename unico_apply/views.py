from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm


# View for the Home page
def Home(request):
    return render(request, 'Home.html')



# View for Universities page
def Universities(request):
    return render(request, 'Universities.html')

# View for About page
def About_Us(request):
    return render(request, 'About-Us.html')

# View for Contact Us Page
def Contact_Us(request):
    return render(request, 'Contact.html')


# View for register
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )

            # Optional: save phone (requires profile model)
            # Profile.objects.create(user=user, phone=form.cleaned_data['phone'])

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, "Register.html", {"form": form})