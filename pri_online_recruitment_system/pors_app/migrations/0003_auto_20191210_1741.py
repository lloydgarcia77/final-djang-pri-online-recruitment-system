# Generated by Django 2.2.3 on 2019-12-10 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pors_app', '0002_auto_20191209_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priapplicantcharacterreferencesinfo',
            name='applicant_character_references',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_references_applicant_fk', to='pors_app.PRIApplicantProfileInfo'),
        ),
        migrations.AlterField(
            model_name='priapplicantcharacterreferencesinfo',
            name='contact_no',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantcharacterreferencesinfo',
            name='full_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='priapplicantcharacterreferencesinfo',
            name='occupation',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='priapplicantemploymenthistoryinfo',
            name='applicant_employment_history',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='employment_applicant_fk', to='pors_app.PRIApplicantProfileInfo'),
        ),
        migrations.AlterField(
            model_name='priapplicantemploymenthistoryinfo',
            name='basic_salary_pay',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='priapplicantemploymenthistoryinfo',
            name='company',
            field=models.CharField(blank=True, max_length=150, verbose_name='Employer/Company Name'),
        ),
        migrations.AlterField(
            model_name='priapplicantemploymenthistoryinfo',
            name='date_from',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='priapplicantemploymenthistoryinfo',
            name='date_to',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='priapplicantemploymenthistoryinfo',
            name='position',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='priapplicantemploymenthistoryinfo',
            name='reason_for_leaving',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='bldg_name_0',
            field=models.CharField(blank=True, max_length=250, verbose_name='Bldg Name.'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='bldg_name_1',
            field=models.CharField(blank=True, max_length=250, verbose_name='Bldg Name.'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='brgy_sub_0',
            field=models.CharField(blank=True, max_length=250, verbose_name='Brgy Sub.'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='brgy_sub_1',
            field=models.CharField(blank=True, max_length=250, verbose_name='Brgy Sub.'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='cit_pro_0',
            field=models.CharField(blank=True, max_length=250, verbose_name='City/Province'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='cit_pro_1',
            field=models.CharField(blank=True, max_length=250, verbose_name='City/Province'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Person Name'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='contact_person_mobile_no',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='ctc',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='dis_mun_0',
            field=models.CharField(blank=True, max_length=250, verbose_name='District/Municipality.'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='dis_mun_1',
            field=models.CharField(blank=True, max_length=250, verbose_name='District/Municipality.'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='father_full_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='father_home_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='father_occupation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Height (Inch)'),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='length_of_pants',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='mother_full_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='mother_home_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='mother_occupation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='pagibig',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='philhealth',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='relationship',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='shirt_size',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='shoe_size',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='sss',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='telephone_no',
            field=models.CharField(blank=True, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='tin',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='waistline',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='priapplicantprofileinfo',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Weight (Lbs)'),
        ),
        migrations.AlterField(
            model_name='priapplicantsibilingsinfo',
            name='applicant_siblings',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='siblings_applicant_fk', to='pors_app.PRIApplicantProfileInfo'),
        ),
        migrations.AlterField(
            model_name='priapplicantsibilingsinfo',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='priapplicantsibilingsinfo',
            name='occ',
            field=models.CharField(blank=True, max_length=50, verbose_name='Occupation/Company'),
        ),
        migrations.AlterField(
            model_name='priapplicanttrainingsinfo',
            name='applicant_trainings',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tranings_applicant_fk', to='pors_app.PRIApplicantProfileInfo'),
        ),
        migrations.AlterField(
            model_name='priapplicanttrainingsinfo',
            name='date_attended',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='priapplicanttrainingsinfo',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Title of traning'),
        ),
    ]
