from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, middlewares, forms


class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = forms.CustomRegistrationForm
    success_url = '/login/'

    def form_valid(self, form):
        response = super(). form_valid(form)
        age = form.cleaned_data['age']
        if age < 5:
            self.object.club = 'Не подходит по возрасту'
        elif 5 <= age <= 10:
            self.object.club = 'Детский клуб'
        elif 11 <= age <= 17:
            self.object.club = 'Подростковый клуб'
        elif 18 <= age <= 45:
            self.object.club = 'Взрослый клуб'
        else:
            self.object.club = 'Клуб не определен'
        self.object.save()
        return response


class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse('users:user_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = getattr(self.request, 'club', 'Клуб не определен')
        return context


