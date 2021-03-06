# Generated by Django 3.2 on 2021-04-30 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('section_id', models.IntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='section.id'))),
            ],
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.id'))),
                ('modifier_id', models.IntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modifier.id'))),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.item')),
            ],
        ),
        migrations.CreateModel(
            name='Modifier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=10000)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='modifiers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.modifier'),
        ),
    ]
