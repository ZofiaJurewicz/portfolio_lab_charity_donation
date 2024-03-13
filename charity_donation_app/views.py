from django.shortcuts import render
from django.views import View

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
