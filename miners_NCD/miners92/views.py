from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import JsonResponse HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.forms import PasswordResetForm
from .models import PerformanceMetrics Matric


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class MyLoginView(LoginView):
    pass

class MyLogoutView(LogoutView):
    pass

class MyPasswordResetView(FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('miners92:password_reset_done')
    template_name = 'miners92/password_reset_fo.html'

    def form_valid(self, form):
        """
        Generate a one-time use token and send a password reset email.
        """
        form.save(
            domain_override='chybuzd.tech',
            email_template_name='miners92/password_reset_email.html',
        )

        return JsonResponse({'success': True})

    def dashboard(request):
        latest_metrics = PerformanceMetrics.objects.latest('timestamp')
        context = {
            'latest_matrics': latest_matrics
            }
        return render(request, 'dashboard.html', context)

    @csrf_exempt
    def save_metric(request):
        if request.method != 'POST':
            return HttpResponseBadRequest('Only POST request are allowed.')
        name = request.POST.get('name')
        value = request.POST.get('value')
        if name is None or value is None:
            return HttpResponseBadRequest('Both name and value parameters are required.')
        try:
            value = float(value)
        except ValueError:
            return HttpResponseBadRequest('Value parameter must be valid floating point number.')
        metric = Metric(name=name, value=value)
        matric.save()
        return HttpResponse('OK')
