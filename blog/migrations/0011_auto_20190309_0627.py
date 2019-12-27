# Generated by Django 2.1.7 on 2019-03-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190309_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.CharField(choices=[('BRTN', 'Brain Research Tagging News'), ('BHN', 'Brain Health News'), ('RDCN', 'Research Domain Criteria News')], default='Default', max_length=100),
        ),
    ]
