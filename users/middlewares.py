from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class AgeClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            if age < 5:
                return HttpResponseBadRequest('Ваш возраст слишком мал')
            elif 5 <= age <= 10:
                request.club = 'Детский клуб образования'
            elif 11 <= age <= 17:
                request.club = 'Подростковый клуб образования'
            elif 18 <= age <= 45:
                request.club = 'Взрослый клуб'
            else:
                return HttpResponseBadRequest('Извините, вы не подходите по возрасту')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Клуб не определен')
