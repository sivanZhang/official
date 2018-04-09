from django.contrib.auth.backends import ModelBackend
from appuser.models import AdaptorUser as User
import re
from django.contrib.auth import authenticate, login
import pdb
 
class PhoneBackend(ModelBackend):
    """
    """
    def authenticate(self, phone=None):
        """
            the third party user authentication
        """ 
        try:  
            user = User.objects.get(phone=phone)  
            return user
        except User.DoesNotExist:
            return None
     
         
            
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
     
