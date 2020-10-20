# Generated by Django 3.1.2 on 2020-10-20 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201019_1542'),
        ('instagram', '0010_post_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=255),
        ),
    ]
