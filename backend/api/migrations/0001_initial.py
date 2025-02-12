# Generated by Django 5.0.7 on 2024-07-28 19:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_consultation', models.DateTimeField()),
                ('symptoms', models.JSONField()),
                ('diagnostic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('poids', models.FloatField()),
                ('taille', models.FloatField()),
                ('tension_art', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_naissance', models.DateField()),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('consultation', models.CharField(max_length=100)),
                ('montant', models.FloatField()),
                ('prestation', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='personne',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.personne'),
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=255)),
                ('type_adresse', models.CharField(max_length=50)),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informations', to='api.personne')),
            ],
        ),
        migrations.CreateModel(
            name='GardeMalade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='garde_malade', to='api.patient')),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personne')),
            ],
        ),
        migrations.CreateModel(
            name='DossierMedical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateField()),
                ('date_modification', models.DateField()),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dossier_medical', to='api.consultation')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient')),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dossiers_medical', to='api.personne')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fonction', models.CharField(max_length=100)),
                ('horaire_travail', models.CharField(max_length=100)),
                ('specialites', models.CharField(max_length=255)),
                ('patient', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.patient')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('service', models.CharField(max_length=100)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='api.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_examen', models.CharField(max_length=100)),
                ('date_realiser', models.DateTimeField()),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultat', models.TextField()),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.personne')),
            ],
        ),
        migrations.CreateModel(
            name='Rattacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('infirmier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personnel')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service')),
            ],
        ),
        migrations.AddField(
            model_name='personnel',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service'),
        ),
        migrations.CreateModel(
            name='Diriger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('poste', models.CharField(max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service')),
            ],
        ),
    ]
