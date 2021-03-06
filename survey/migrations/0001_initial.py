# Generated by Django 3.1.3 on 2020-12-28 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'survey_categories',
            },
        ),
        migrations.CreateModel(
            name='EffectiveDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateField(null=True)),
                ('end_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'effective_dates',
            },
        ),
        migrations.CreateModel(
            name='EvasionGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=1)),
                ('tendency', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'evasion_grade',
            },
        ),
        migrations.CreateModel(
            name='InvestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'invest_types',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survey.category')),
                ('effective_date', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.effectivedate')),
            ],
            options={
                'db_table': 'surveys',
            },
        ),
        migrations.CreateModel(
            name='UserSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(null=True)),
                ('answer', models.CharField(max_length=45, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survey.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
            options={
                'db_table': 'users_surveys',
            },
        ),
        migrations.AddField(
            model_name='survey',
            name='users',
            field=models.ManyToManyField(through='survey.UserSurvey', to='user.User'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(null=True)),
                ('effective_date', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='survey.effectivedate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
            options={
                'db_table': 'results',
            },
        ),
    ]
