from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate, login
import pdb
 
class EmailBackend(ModelBackend):
    """
    """
    def authenticate(self, email=None):
	"""
		the third party user authentication
	"""
        #validate email format
        EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+') 
        if EMAIL_REGEX.match(email):
            try: 
                user = User.objects.get(email=email)  
		return user
            except User.DoesNotExist:
                return None
        else:
                return None
         
			
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
     
