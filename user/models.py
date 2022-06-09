from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import FileExtensionValidator
from django import forms
# Create your models here.
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    This is the manager for custom user model
    """

    def create_user(self, username, email, full_name, password=None):

        if not username:
            raise ValueError('Username should not be empty')
        if not email:
            raise ValueError('Email should not be empty')
        if not full_name:
            raise ValueError('Name should not be empty')
        if not password:
            raise ValueError('Password should not be empty')

        user = self.model(
            username=username,
            email=self.normalize_email(email=email),
            full_name=full_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name, password=None):
        user = self.create_user(
            username=username,
            email=email, full_name=full_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model Class
    """
    username = models.CharField(
        max_length=100, verbose_name='Username', unique=True, blank=False)
    email = models.EmailField(
        max_length=100, verbose_name='Email', unique=True, blank=True)
    full_name = models.CharField(verbose_name='Full Name', max_length=100)
    phone_number = models.CharField(max_length=255, verbose_name="Phone Number")
    address_one = models.CharField(max_length=255, blank=True)
    address_two = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(
        verbose_name="Country", max_length=50, blank=True)
    profile_pic = models.ImageField(
        upload_to='users/', default='users/default.png')
    birth_date = models.DateField(
        verbose_name='Birth Date', blank=True, null=True)
    date_joined = models.DateTimeField(
        verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    gender_options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    gender = models.CharField(
        verbose_name='Choose Gender', choices=gender_options, max_length=20)

    is_staff = models.BooleanField(verbose_name='Staff Status', default=False, help_text='Designate if the user has '
                                                                                         'staff status')
    is_active = models.BooleanField(verbose_name='Active Status', default=True, help_text='Designate if the user has '
                                                                                          'active status')
    is_superuser = models.BooleanField(verbose_name='Superuser Status', default=False, help_text='Designate if the '
                                                                                                 'user has superuser '
                                                                                                 'status')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']

    objects = UserManager()

    def __str__(self):
        return self.full_name


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=4, unique=True)
    slug = models.SlugField(max_length=100, allow_unicode=True, null=True, editable=False)
    # location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='موقعیت')
    start_date = models.DateField(default=timezone.now, null=True, blank=True)
    end_date = models.DateField(default=timezone.now, null=True, blank=True)
    duration = models.IntegerField(default=0, editable=False)


class Phase(models.Model):
    title = models.CharField(max_length=20)


class ProjectPhase(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='phase')
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, related_name='project')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    duration = models.IntegerField(default=0, editable=True)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'



class Provinsi(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'provinsi'
        verbose_name_plural = 'provinsi'

    def __str__(self):
        return self.name


class Kabupaten(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    provinsi_code = models.IntegerField(null=True, blank=True)
    provinsi = models.ForeignKey(
        Provinsi,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'kabupaten'
        verbose_name_plural = 'kabupaten'

    def __str__(self):
        return self.name


class Kecamatan(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    kabupaten_code = models.IntegerField(null=True, blank=True)
    kabupaten = models.ForeignKey(
        Kabupaten,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'kecamatan'
        verbose_name_plural = 'kecamatan'

    def __str__(self):
        return self.name


class Kelurahan(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.BigIntegerField(null=True, blank=True)
    kecamatan_code = models.IntegerField(null=True, blank=True)
    kecamatan = models.ForeignKey(
        Kecamatan,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'kelurahan'
        verbose_name_plural = 'kelurahan'

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    provinsi = models.ForeignKey(
        Provinsi,
        on_delete=models.CASCADE,
        related_name='warehouse_provinsi',
    )
    kabupaten = models.ForeignKey(
        Kabupaten,
        on_delete=models.CASCADE,
        related_name='warehouse_kabupaten',
    )
    kecamatan = models.ForeignKey(
        Kecamatan,
        on_delete=models.CASCADE,
        related_name='warehouse_kecamatan',
    )
    kelurahan = models.ForeignKey(
        Kelurahan,
        on_delete=models.CASCADE,
        related_name='warehouse_kelurahan',
    )