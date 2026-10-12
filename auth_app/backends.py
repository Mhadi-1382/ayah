from django.contrib.auth.backends import ModelBackend
from .models import CUser

class PhoneAuthBackend(ModelBackend):
    def authenticate(self, request, phone=None, password=None, **kwargs):
        try:
            user = CUser.objects.get(phone=phone)
            if user.check_password(password):
                return user
        except CUser.DoesNotExist:
            return None
