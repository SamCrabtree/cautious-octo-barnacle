# Generated by Django 3.2.8 on 2021-11-09 17:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_call_list', '0008_note_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loop', models.TextField(max_length=500)),
                ('loop_type', models.CharField(choices=[('Financial', 'FINANCIAL'), ('Note Follow Up', 'NOTE FOLLOW UP'), ('Legal Follow Up', 'LEGAL FOLLOW UP'), ('Investor Follow Up', 'INVESTOR FOLLOW UP'), ('Oppurtunities', 'OPPURTUNITIES')], default='Other', max_length=500)),
                ('contact', models.TextField(max_length=200)),
                ('goal', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door', models.TextField(max_length=250)),
                ('key_1', models.TextField(max_length=250)),
                ('key_2', models.TextField(max_length=250)),
                ('key_3', models.TextField(max_length=250)),
                ('key_4', models.TextField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
