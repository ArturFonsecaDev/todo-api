from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('An email must be given!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user
    
    def update_user(self, user_id, email, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)

        try:
            user = self.model.objects.get(pk=user_id)
        except self.model.DoesNotExist:
            raise self.model.DoesNotExist(f'User with id {user_id} not found!')

        user.email = email if email else user.email

        if password:
            user.set_password(password)

        for key, value in extra_fields.items():
            setattr(user, key, value)

        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        assert email and password

        email = self.normalize_email(email=email)

        superuser = User(email=email)
        superuser.set_password(password)

        superuser.is_staff = True
        superuser.is_superuser = True
        
        superuser.save(using=self._db)
        return superuser
    
    def deactivate_user(self, id: int):
        if not id:
            raise ValueError('An Id must be given!')

        try:
            user = self.model.objects.get(id=id)
        except:
            raise self.model.DoesNotExist(f'User with id {id} not found!')
        
        user.is_active = False
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'