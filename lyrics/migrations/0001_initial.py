# Generated by Django 3.2.5 on 2021-07-06 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('moodId', models.IntegerField(primary_key=True, serialize=False)),
                ('mood', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SongInfo',
            fields=[
                ('songId', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('artist', models.CharField(max_length=300)),
                ('imgURL', models.URLField(default='https://cdnimg.melon.co.kr/cm2/album/images/100/43/575/10043575_20210302112520_500.jpg/melon/resize/120/quality/80/optimize', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SongMood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moodId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lyrics.mood')),
                ('songId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lyrics.songinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('songId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lyrics.songinfo')),
            ],
        ),
    ]
