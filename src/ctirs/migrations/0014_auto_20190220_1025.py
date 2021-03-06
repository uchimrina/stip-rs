# Generated by Django 1.10.4 on 2019-02-20 01:25


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctirs', '0013_auto_20190220_0938'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='activity',
            table='stip_sns_activity',
        ),
        migrations.AlterModelTable(
            name='aliases',
            table='stip_gv_aliases',
        ),
        migrations.AlterModelTable(
            name='attachfile',
            table='stip_sns_attachfile',
        ),
        migrations.AlterModelTable(
            name='config',
            table='stip_gv_system',
        ),
        migrations.AlterModelTable(
            name='country',
            table='stip_common_country',
        ),
        migrations.AlterModelTable(
            name='feed',
            table='stip_sns_feed',
        ),
        migrations.AlterModelTable(
            name='group',
            table='stip_common_group',
        ),
        migrations.AlterModelTable(
            name='gvauthuser',
            table='stip_gv_user',
        ),
        migrations.AlterModelTable(
            name='message',
            table='stip_sns_message',
        ),
        migrations.AlterModelTable(
            name='mongoconfig',
            table='stip_rs_mongo',
        ),
        migrations.AlterModelTable(
            name='notification',
            table='stip_sns_notification',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='stip_sns_user',
        ),
        migrations.AlterModelTable(
            name='region',
            table='stip_common_region',
        ),
        migrations.AlterModelTable(
            name='stipuser',
            table='stip_common_user',
        ),
        migrations.AlterModelTable(
            name='system',
            table='stip_rs_system',
        ),
        migrations.AlterModelTable(
            name='taxii',
            table='stip_gv_taxii',
        ),
    ]
