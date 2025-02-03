from django.contrib import admin
from .models import *


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'status']


@admin.register(TypeObr)
class TypeObrAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['fio', 'address', 'phone']


@admin.register(TypeWork)
class TypeWorkAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Obr)
class ObrAdmin(admin.ModelAdmin):
    list_display = ['dat', 'client', 'type_obr', 'status']


@admin.register(WordByObr)
class WordByObrAdmin(admin.ModelAdmin):
    list_display = ['obr', 'type_work', 'worker']