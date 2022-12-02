# Generated by Django 4.1.3 on 2022-12-01 09:47

from django.conf import settings
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
            name='User',
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
                ('is_doctor', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('Masculin ', 'Masculin'), ('Feminin', 'Feminin')], max_length=10)),
                ('profession', models.CharField(max_length=50)),
                ('domicile', models.CharField(max_length=50)),
                ('nationalite', models.CharField(max_length=50)),
                ('referent', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=10)),
                ('groupe_sanguin', models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', '+B'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=3, null=True)),
                ('taille', models.CharField(max_length=50)),
                ('poids', models.CharField(max_length=50)),
                ('imc', models.CharField(max_length=50)),
                ('asthme', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('epilepsie', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('drepanocytose', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('ulcere', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('sinusite', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('diabete', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('hta', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('operation', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('gestite_parite', models.CharField(max_length=50)),
                ('contraception', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('alcool', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('tabac', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=3)),
                ('autre', models.CharField(blank=True, max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexe', models.CharField(choices=[('Masculin ', 'Masculin'), ('Feminin', 'Feminin')], max_length=10)),
                ('telephone', models.CharField(max_length=10)),
                ('groupe_sanguin', models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', '+B'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=3, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif_de_la_consultation', models.TextField(blank=True)),
                ('debut_de_la_maladie', models.CharField(blank=True, max_length=50)),
                ('signes_de_la_maladie', models.CharField(blank=True, max_length=100)),
                ('traitement_recu', models.TextField(blank=True)),
                ('evaluation', models.TextField(blank=True)),
                ('tension_arterielle', models.IntegerField(default=0)),
                ('pouls', models.IntegerField(default=0)),
                ('sao2', models.IntegerField(default=0)),
                ('temperature', models.IntegerField(default=0)),
                ('score_de_glasow', models.IntegerField(default=0)),
                ('conjonctives', models.IntegerField(default=0)),
                ('resume', models.TextField(blank=True)),
                ('hypothese_diagnostique', models.TextField(blank=True)),
                ('bilan_demande', models.TextField(blank=True)),
                ('diagnostic', models.TextField(blank=True)),
                ('traitement', models.TextField(blank=True)),
                ('evoluation', models.TextField(blank=True)),
                ('rendez_vous', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('docteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_consultation', to='hospital.doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_consultation', to='hospital.patient')),
            ],
            options={
                'verbose_name': 'Consultation',
                'verbose_name_plural': 'Consultations',
            },
        ),
    ]
