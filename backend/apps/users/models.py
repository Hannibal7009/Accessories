import email
from lib2to3.pgen2 import token
from turtle import update
from venv import create
from zlib import DEF_BUF_SIZE
from django import db
from django.db import models

# Create your models here.


class User(models.Model):
    class Meta(object):
        db_table = 'user'

    name = models.CharField(
        'User Name', max_length=50, blank=False, null=False, db_index=True
    )
    email = models.EmailField(
        'Email', max_length=200, blank=False, null=False, db_index=True
    )
    password = models.CharField(
        'Password', max_length=255, blank=False, null=False, db_index=True
    )
    token = models.CharField(
        'Token', max_length=255, blank=True, null=True, db_index=True
    )
    token_expires_at = models.DateTimeField(
        'Expires At', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )

    def __str__(self):
        return self.name
