# Generated by Django 5.1.2 on 2024-10-30 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_alter_conversation_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ('-modified_at',), 'verbose_name': 'conversation', 'verbose_name_plural': 'conversations'},
        ),
        migrations.AlterModelOptions(
            name='conversationmessage',
            options={'ordering': ('created_at',), 'verbose_name': 'conversation message', 'verbose_name_plural': 'conversation messages'},
        ),
    ]
