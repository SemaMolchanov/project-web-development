# Generated by Django 2.2.19 on 2022-07-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webproj_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamedetails',
            options={'verbose_name': 'Game Details', 'verbose_name_plural': 'Game Details'},
        ),
        migrations.AlterField(
            model_name='gamedescription',
            name='game_id',
            field=models.ForeignKey(on_delete='cascade', to='webproj_api.Game'),
        ),
        migrations.AlterField(
            model_name='gamedetails',
            name='game_id',
            field=models.ForeignKey(on_delete='cascade', to='webproj_api.Game'),
        ),
        migrations.AlterField(
            model_name='gameimages',
            name='game_id',
            field=models.ForeignKey(on_delete='cascade', to='webproj_api.Game'),
        ),
    ]