# Generated by Django 3.2.9 on 2021-12-20 05:41

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'restaurant'), (2, 'customer')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser')),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Other', 'Other'), ('Female', 'Female'), ('Male', 'Male')], max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('birth', models.DateField(null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('city', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser')),
                ('rating', models.DecimalField(decimal_places=1, default=10.0, max_digits=3)),
                ('restaurant_name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Cafe', 'Cafe'), ('Fine Dining', 'Fine Dining'), ('Casual or Family-Style', 'Casual or Family-Style'), ('Fast Food', 'Fast Food'), ('Other', 'Other')], max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('address', models.TextField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('cost', models.IntegerField(null=True)),
                ('ingredients', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Cold Drink', 'Cold Drink'), ('Hot Drink', 'Hot Drink'), ('Alcohol', 'Alcohol'), ('Starter', 'Starter'), ('Meat&Fish', 'Meat&Fish'), ('Soup', 'Soup'), ('Burger', 'Burger'), ('Pizza', 'Pizza'), ('Pasta', 'Pasta'), ('Desert', 'Desert')], max_length=100, null=True)),
                ('image', models.ImageField(default='default.png', upload_to='menu')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_date', models.DateTimeField(null=True)),
                ('table', models.CharField(max_length=100, null=True)),
                ('notes', models.TextField(max_length=200, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Restaurant Approved', 'Restaurant Approved'), ('Restaurant Declined', 'Restaurant Declined')], max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer')),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(null=True)),
                ('content', models.TextField(max_length=100, null=True)),
                ('notes', models.TextField(max_length=200, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Restaurant Approved', 'Restaurant Approved'), ('Restaurant Declined', 'Restaurant Declined')], max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer')),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.restaurant'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, null=True)),
                ('comment', models.TextField(max_length=200, null=True)),
                ('rate', models.DecimalField(decimal_places=1, default=10, max_digits=3)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer')),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.restaurant')),
            ],
        ),
    ]
