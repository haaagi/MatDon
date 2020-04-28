from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[

                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('store_id', models.IntegerField(
                    primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=50)),
                ('store_tel', models.CharField(max_length=20, null=True)),
                ('store_address', models.CharField(max_length=255, null=True)),
                ('store_latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('store_longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('store_category', models.CharField(max_length=50, null=True)),
                ('store_image', models.TextField(max_length=500, null=True)),
                ('store_price', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True)),
                ('score_mean', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
>>>>>>> develop
            ],
        ),
        migrations.CreateModel(
            name='Store_score',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
=======
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> develop
                ('store_name', models.CharField(max_length=50, null=True)),
                ('user_id', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('rep_price', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True)),
                ('store_image', models.TextField(max_length=500, null=True)),
<<<<<<< HEAD
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='stores.Store')),
=======
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='review', to='stores.Store')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50, null=True)),
                ('user_id', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('rep_price', models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True)),
                ('store_image', models.TextField(max_length=500, null=True)),
                ('mean_score', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='stores.Store')),
>>>>>>> 9f0efd5e0310ae7a212ca18bd655c7c519f3e1a8
>>>>>>> develop
            ],
        ),
        migrations.CreateModel(
            name='Store_menu',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=200, null=True)),
                ('menu_price', models.DecimalField(decimal_places=0, max_digits=9, null=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='stores.Store')),
=======
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=200, null=True)),
                ('menu_price', models.DecimalField(
                    decimal_places=0, max_digits=9, null=True)),
                ('store', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='stores.Store')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=200, null=True)),
                ('menu_price', models.DecimalField(decimal_places=0, max_digits=9, null=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='stores.Store')),
>>>>>>> 9f0efd5e0310ae7a212ca18bd655c7c519f3e1a8
>>>>>>> develop
            ],
        ),
    ]
