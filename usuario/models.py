from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


from django.urls import reverse
from django.utils.html import mark_safe


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('O usuário precisa ter um email válido.')
        if not password:
            raise ValueError('Precisa inserir a senha correta.')

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        # user.staff = True
        # user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        # user.staff = True
        # user.admin = True
        # user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    PROFILE_CHOICES = {
        ('usuario', 'Usuário'),
        ('profissional', 'Profissional'),
    }

    profile     = models.CharField('Perfil', max_length=13, choices=PROFILE_CHOICES, null=False)
    email       = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    active      = models.BooleanField('Usuário ativo', default=True)
    staff       = models.BooleanField('Membro da equipe', default=False) # a admin user; non super-user
    admin       = models.BooleanField('Usuário admin', default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    # def get_absolute_url_profile(self):
    #     return reverse('usuario:profile', args=[self.pk])

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "O usuário tem a permissão específica?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "O usuário tem permissões para visualizar o aplicativo 'app_label'?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_active(self):
        "A conta está ativa?"
        return self.active

    @property
    def is_staff(self):
        "O usuário é um membro da equipe?"
        return self.staff

    @property
    def is_admin(self):
        "O usuário é membro Admin?"
        return self.admin

    objects = UserManager()


class Profile(models.Model):
    
    CATEGORIES_CHOICES = (
        ('enventos','enventos'),
        ('entretenimento','entretenimento'),
        ('automotivo','automotivo'),
        ('serviços elétricos','serviços elétricos'),
        ('professores','professores'),
        ('entregadores','entregadores'),
        ('predeiros','predeiros'),
        ('motorista','motorista'),
        ('outros','outros'),
    )

    email       = models.ForeignKey(User, 
                                    on_delete=models.CASCADE, 
                                    related_name='+')
    name        = models.CharField('Nome', max_length=100, null=False)
    cpf         = models.CharField('CPF', max_length=14, null=False)
    photograph  = models.ImageField('Foto', blank=True, upload_to='usuario')
    doc_id      = models.CharField('Documento de identidade', max_length=20, blank=False, null=False)
    
    street      = models.CharField('Rua/av.', max_length=30)
    number      = models.IntegerField('Número')    
    compl       = models.CharField('Complemento', max_length=30, blank=True)
    neighbor    = models.CharField('Bairro', max_length=30)
    city        = models.CharField('Cidade', max_length=30)

    category    = models.CharField('Categoria', max_length=50, choices=CATEGORIES_CHOICES, blank=True)
    curriculum  = models.TextField(blank=True, null=True)
    terms       = models.BooleanField('Aceito os Termos', default=False)
    
    date_joined = models.DateTimeField('Data do cadastro', auto_now_add=True)


    def __str__(self):
        return self.name

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />'%self.photograph.url)
    
    class Meta:
        verbose_name        = 'Perfil'
        verbose_name_plural = 'Perfis'
