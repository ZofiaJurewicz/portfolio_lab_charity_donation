from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from charity_donation_app.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        institutions = Institution.objects.all()
        donations = Donation.objects.all()
        total_bags_donations = sum(donation.quantity for donation in donations)
        total_institutions_donated = Donation.objects.values('institution').distinct().count()

        ctx = {
            'total_bags_donations': total_bags_donations,
            'total_institutions_donated': total_institutions_donated,
            'page_type': 'landing_page',
            'institutions': institutions,
        }

        return render(request, 'index.html', ctx)


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html', {'page_type': 'add_donation'})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'page_type': 'login'})


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {'page_type': 'register'})

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not (name and surname and email and password and password2):
            return redirect('register')

        if password != password2:
            return redirect('register')

        if User.objects.filter(email=email).exists():
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.last_name = surname
        user.save()

        return redirect('login')

