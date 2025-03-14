# Generated by Django 5.1.6 on 2025-02-23 20:37

import user.models.user
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Identificador')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('full_name', models.CharField(max_length=255, verbose_name='full name')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('date_of_birth', models.DateField()),
                ('bio', models.TextField(blank=True, null=True, verbose_name='User bio')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=user.models.user.user_avatar_upload_path, verbose_name='User Avatar')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=user.models.user.user_cover_upload_path, verbose_name='User Cover')),
                ('followers', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
