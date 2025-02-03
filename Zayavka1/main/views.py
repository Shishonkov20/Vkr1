from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import *
from .forms import *


class MainView(TemplateView):
    template_name = 'main/main_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TypeObrView(TemplateView):
    template_name = 'main/typeobr_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objs'] = TypeObr.objects.all()
        return context


class ClientView(TemplateView):
    template_name = 'main/client_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objs'] = Client.objects.all()
        return context


class TypeWorkView(TemplateView):
    template_name = 'main/typework_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objs'] = TypeWork.objects.all()
        return context


class ObrView(TemplateView):
    template_name = 'main/obr_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objs'] = Obr.objects.all()
        return context


class WordByObrView(TemplateView):
    template_name = 'main/workbyobr_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.status == 'Сотрудник':
            context['objs'] = WordByObr.objects.filter(worker=self.request.user)
        else:
            context['objs'] = WordByObr.objects.all()
        return context


class WorkerView(TemplateView):
    template_name = 'main/worker_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objs'] = AdvUser.objects.all()
        return context


class CreateTypeObrView(CreateView):
    template_name = 'main/typeobr_create_view.html'
    model = TypeObr
    form_class = CreateTypeObrForm
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateClientView(CreateView):
    template_name = 'main/client_create_view.html'
    model = Client
    form_class = CreateClientForm
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateTypeWorkView(CreateView):
    template_name = 'main/typework_create_view.html'
    model = TypeWork
    form_class = CreateTypeWorkForm
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateObrView(CreateView):
    template_name = 'main/obr_create_view.html'
    model = Obr
    form_class = CreateObrForm
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateWordByObrView(CreateView):
    template_name = 'main/wordbyobr_create_view.html'
    model = WordByObr
    form_class = CreateWordByObrForm
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ObrInWork(TemplateView):
    template_name = 'main/obrinwork.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objs'] = Obr.objects.filter(status='В работе')
        return context


class WorkObr(TemplateView):
    template_name = 'main/workobr.html'

    def get_queryset(self):
        return WordByObr.objects.filter(obr=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objs'] = WordByObr.objects.all()
        context['voyages'] = Obr.objects.all()
        if self.request.GET.get("q") is not None:
            context['objs'] = WordByObr.objects.filter(obr=self.request.GET.get("q"))
        else:
            context['objs'] = WordByObr.objects.all()
        return context


class RegistrationFormView(CreateView):
    model = AdvUser
    form_class = AdvUserCreationForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = AdvUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MainLoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('main')

    def get_success_url(self):
        return self.success_url


class MainLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'