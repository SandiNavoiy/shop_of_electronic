from rest_framework import authentication
from rest_framework import exceptions
class IsActiveUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user = request.user
        if user and user.is_active:
            return (user, None)
        raise exceptions.AuthenticationFailed("Пользователь не активен")
