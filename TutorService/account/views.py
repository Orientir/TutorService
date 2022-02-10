from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import views as django_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.utils.translation import pgettext, ugettext_lazy as _

from .forms import (
    ChangePasswordForm,
    LoginForm,
    NameForm,
    PasswordResetForm,
    SignupForm,
    logout_on_password_change,
)

def login(request):
    kwargs = {"template_name": "account/login.html", "authentication_form": LoginForm}
    return django_views.LoginView.as_view(**kwargs)(request, **kwargs)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, _("You have been successfully logged out."))
    return redirect(settings.LOGIN_REDIRECT_URL)


def password_reset(request):
    kwargs = {
        "template_name": "account/password_reset.html",
        "success_url": reverse_lazy("account:reset-password-done"),
        "form_class": PasswordResetForm,
    }
    return django_views.PasswordResetView.as_view(**kwargs)(request, **kwargs)


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        print('valid')
        form.save()
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = auth.authenticate(request=request, email=email, password=password)
        if user:
            print('user')
            auth.login(request, user)
        messages.success(request, _("User has been created"))
        redirect_url = request.POST.get("next", settings.LOGIN_REDIRECT_URL)
        return redirect(redirect_url)
    ctx = {"form": form}
    return TemplateResponse(request, "account/signup.html", ctx)


@login_required
def details(request):
    password_form = get_or_process_password_form(request)
    name_form = get_or_process_name_form(request)

    ctx = {
        "addresses": request.user.addresses.all(),
        "change_password_form": password_form,
        "user_name_form": name_form,
    }

    return TemplateResponse(request, "account/details.html", ctx)


def get_or_process_password_form(request):
    form = ChangePasswordForm(data=request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        logout_on_password_change(request, form.user)
        messages.success(
            request, pgettext("Storefront message", "Password successfully changed.")
        )
    return form


def get_or_process_name_form(request):
    form = NameForm(data=request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(
            request, pgettext("Storefront message", "Account successfully updated.")
        )
    return form