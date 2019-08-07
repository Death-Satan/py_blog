# Generated by Django 2.1 on 2019-08-07 08:43

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='abodu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/%Y/%m/%d/', verbose_name='文章图片'),
        ),
    ]
