# Generated by Django 2.2.7 on 2019-11-22 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peertotur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('paddress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('pemail', models.CharField(blank=True, max_length=100, null=True, verbose_name='E-mail address')),
                ('pmajor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Major')),
                ('pdep', models.CharField(blank=True, max_length=100, null=True, verbose_name='Department')),
                ('pgpamajor', models.CharField(blank=True, max_length=10, null=True, verbose_name='GPA in major')),
                ('pgpacum', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cumulative GPA')),
                ('pexgraduate', models.CharField(blank=True, max_length=20, null=True, verbose_name='Expected date of Graduation')),
                ('reqdate', models.DateTimeField(auto_now_add=True)),
                ('ptel', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tel')),
                ('pgsm', models.CharField(blank=True, max_length=20, null=True, verbose_name='GSM')),
                ('yearofstudy', models.CharField(blank=True, choices=[('Soph', 'Sopph'), ('Jr', 'Jr'), ('Sr', 'Sr'), ('Grad_Student', 'Grad_Student')], max_length=20, null=True, verbose_name='Year of Study')),
                ('pimg', models.ImageField(blank=True, null=True, upload_to='peertoturs/img/%Y/%m/%d', verbose_name='Peer Totur Image')),
            ],
            options={
                'ordering': ['-reqdate'],
            },
        ),
        migrations.CreateModel(
            name='Peertoturfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=500)),
                ('filepath', models.FileField(blank=True, null=True, upload_to='peertoturs/uploads/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='StudentComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtitle', models.CharField(blank=True, max_length=300, null=True)),
                ('mbody', models.CharField(blank=True, max_length=300, null=True)),
                ('mstatus', models.BooleanField(default=False)),
                ('mdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peertoturq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(blank=True, max_length=300, null=True, verbose_name='Question1')),
                ('answer1', models.TextField(blank=True, null=True, verbose_name='Answer1')),
                ('question2', models.CharField(blank=True, max_length=300, null=True, verbose_name='Question2')),
                ('answer2', models.TextField(blank=True, null=True, verbose_name='Answer2')),
                ('question3', models.CharField(blank=True, max_length=300, null=True, verbose_name='Question3')),
                ('answer3', models.TextField(blank=True, null=True, verbose_name='Answer3')),
                ('qsdate', models.DateTimeField(auto_now_add=True)),
                ('pname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peertotur.Peertotur', verbose_name='Peer Tutor Name')),
            ],
        ),
        migrations.CreateModel(
            name='Peertoturexperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(blank=True, max_length=200, null=True, verbose_name='Course Name')),
                ('coursecode', models.CharField(blank=True, max_length=10, null=True, verbose_name='Course Code')),
                ('fp', models.BooleanField(blank=True, default=False, null=True)),
                ('pname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peertotur.Peertotur', verbose_name='Peer Totur List')),
            ],
            options={
                'ordering': ['coursename'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='file title')),
                ('file', models.FileField(blank=True, null=True, upload_to='peertoturs/docs/')),
                ('dateupload', models.DateTimeField(auto_now_add=True)),
                ('pname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peertotur.Peertotur')),
            ],
        ),
    ]