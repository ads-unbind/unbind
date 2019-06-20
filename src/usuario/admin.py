from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuario.models import Usuario
from usuario.forms import UsuarioChangeForm

from usuario.forms import UsuarioCreationFormAdmin


class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationFormAdmin
    form = UsuarioChangeForm
    model = Usuario


UsuarioAdmin.fieldsets += ('custom fields set', {'fields': ('foto', 'scoreTotal', 'atividade',
                                                                'artigo', 'questionario', 'conquista')}),


admin.site.register(Usuario, UsuarioAdmin)
