from django.contrib.auth import backends
from django.contrib.auth import get_user_model
from django.db.models import Q

# class that will authenticate users using their email
class EmailBackend(backends.ModelBackend):
    # function to authenticate
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # find a user matching the email (username parameter will contain email)
            user = UserModel.objects.get(
                Q(email=username)  # Only check email, no username check
            )
        except UserModel.DoesNotExist:
            # run the default password hasher once to reduce timing difference
            # which is also a security measure to prevent timing attacks by hashing the password
            # even if the user does not exist
            UserModel().set_password(password)  # Fixed: call on instance, not class
            return None  # return none if authentication fails
        
        # verify if password entered matches the user hashed password and if the user is active
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        return None