# Generated by Django 3.2 on 2022-10-30 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshops', '0002_auto_20221029_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to=settings.AUTH_USER_MODEL)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshop_testimonials', to='workshops.workshop')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]
