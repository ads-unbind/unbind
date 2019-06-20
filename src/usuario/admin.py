from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuario.models import Usuario
# Register your models here.
from usuario.forms import UsuarioCreationForm
from usuario.forms import UsuarioChangeForm

from usuario.forms import UsuarioCreationFormAdmin


class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationFormAdmin
    form = UsuarioChangeForm
    model = Usuario
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_name', 'last_name', 'nome', 'foto',
    #                    'scoreTotal', 'atividade', 'artigo', 'questionario', 'conquista', 'password1')
    #     }
    #     )
    # )


UsuarioAdmin.fieldsets += ('custom fields set', {'fields': ('foto', 'scoreTotal', 'atividade',
                                                                'artigo', 'questionario', 'conquista')}),


admin.site.register(Usuario, UsuarioAdmin)
