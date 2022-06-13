from django.contrib import admin
from core.models import Compromisso


class CompromissoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo','usuario', 'data_evento', )

# Register your models

admin.site.register(Compromisso, CompromissoAdmin)

