# Generated by Django 2.0.3 on 2019-08-31 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0002_produto_loja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens_dos_produtos'),
        ),
    ]