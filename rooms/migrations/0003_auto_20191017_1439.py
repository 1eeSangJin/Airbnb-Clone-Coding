# Generated by Django 3.0a1 on 2019-10-17 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20191017_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rooms.AbstractItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('rooms.abstractitem',),
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rooms.AbstractItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('rooms.abstractitem',),
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rooms.AbstractItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('rooms.abstractitem',),
        ),
        migrations.RemoveField(
            model_name='room',
            name='roomType',
        ),
        migrations.AddField(
            model_name='room',
            name='roomType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.RoomType'),
        ),
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(to='rooms.Amenity'),
        ),
    ]
