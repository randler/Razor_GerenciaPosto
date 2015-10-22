#encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.forms import forms
from django.contrib.auth.forms import UserCreationForm

class Usuario(User):

    def __unicode__(self):
        return self.nome_estabelecimento

class criaUsuario(UserCreationForm):

    class Meta:
        model = Usuario

        fields = ['username','email','is_staff','groups']

