# Generated by Django 2.2.3 on 2019-12-25 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pors_app', '0005_auto_20191224_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_admin',
        ),
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_applicants',
        ),
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_application_form',
        ),
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_clients',
        ),
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_exam',
        ),
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_hired',
        ),
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_jobs',
        ),
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_request',
        ),
        migrations.RemoveField(
            model_name='priuserpermission',
            name='pri_is_schedule',
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_add_clients',
            field=models.BooleanField(default=False, verbose_name='Can Add Clients'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_add_request',
            field=models.BooleanField(default=False, verbose_name='Can Add Requests'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_create_job_request',
            field=models.BooleanField(default=False, verbose_name='Can Create Job Requests'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_delete_applicants',
            field=models.BooleanField(default=False, verbose_name='Can Delete Applicants'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_delete_clients',
            field=models.BooleanField(default=False, verbose_name='Can Delete Clients'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_delete_job_vacancy',
            field=models.BooleanField(default=False, verbose_name='Can Delete Job Vacancy'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_delete_request',
            field=models.BooleanField(default=False, verbose_name='Can Delete Requests'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_edit_clients',
            field=models.BooleanField(default=False, verbose_name='Can Edit Clients'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_edit_job_vacancy',
            field=models.BooleanField(default=False, verbose_name='Can Edit Job Vacancy'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_edit_request',
            field=models.BooleanField(default=False, verbose_name='Can Edit Requests'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_hired_clients',
            field=models.BooleanField(default=False, verbose_name='Can Hired Clients'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_view_applicants_page',
            field=models.BooleanField(default=False, verbose_name='Can View Applicants Page'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_view_clients_page',
            field=models.BooleanField(default=False, verbose_name='Can View Clients Page'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_view_job_vacancy_applicants',
            field=models.BooleanField(default=False, verbose_name='Can View Job Vacancy Applicants'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_view_job_vacancy_page',
            field=models.BooleanField(default=False, verbose_name='Can View Job Vacancy Page'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_view_request',
            field=models.BooleanField(default=False, verbose_name='Can View Requests'),
        ),
        migrations.AddField(
            model_name='priuserpermission',
            name='pri_can_view_request_page',
            field=models.BooleanField(default=False, verbose_name='Can View Requests Page'),
        ),
        migrations.AlterField(
            model_name='priuserinfo',
            name='level',
            field=models.CharField(choices=[('Administrator', 'Administrator'), ('Sub Admin', 'Sub Admin'), ('Employee', 'Employee'), ('Client', 'Client')], default=('Administrator', 'Administrator'), max_length=50),
        ),
        migrations.AlterField(
            model_name='priuserpermission',
            name='pri_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='policy_user_fk', to='pors_app.PRIUserInfo'),
        ),
    ]
