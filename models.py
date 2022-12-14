# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminclearRespondent(models.Model):
    newguid = models.CharField(db_column='NewGUID', max_length=36)  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    login_id = models.IntegerField(db_column='Login_ID', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='Start_Time', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='End_Time', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_number = models.CharField(db_column='ID_Number', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='Image_URL', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gps_location = models.CharField(db_column='GPS_Location', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdminClear_Respondent'


class AdminclearResponses(models.Model):
    responses_id = models.IntegerField(db_column='Responses_ID')  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID')  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    newguid = models.CharField(db_column='NewGUID', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdminClear_Responses'


class BulkuploadRespondent(models.Model):
    newguid = models.CharField(db_column='NewGUID', max_length=36)  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID')  # Field name made lowercase.
    login_id = models.IntegerField(db_column='Login_ID')  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='Start_Time', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='End_Time', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_number = models.CharField(db_column='ID_Number', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='Image_URL', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gps_location = models.CharField(db_column='GPS_Location', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BulkUpload_Respondent'


class BulkuploadResponses(models.Model):
    responses_id = models.IntegerField(db_column='Responses_ID')  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID')  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID')  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    newguid = models.CharField(db_column='NewGUID', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BulkUpload_Responses'


class Gps(models.Model):
    gps_id = models.IntegerField(db_column='GPS_ID')  # Field name made lowercase.
    gps_name = models.TextField(db_column='GPS_Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    max_range = models.IntegerField(db_column='Max_Range', blank=True, null=True)  # Field name made lowercase.
    permission = models.BooleanField(db_column='Permission', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPS'


class Likert(models.Model):
    likert_id = models.IntegerField(db_column='Likert_ID')  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    likert_options = models.CharField(db_column='Likert_Options', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    likert_index = models.IntegerField(db_column='Likert_Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Likert'


class Login(models.Model):
    login_id = models.IntegerField(db_column='Login_ID')  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Login'


class LoginNormal(models.Model):
    login_id = models.FloatField(db_column='Login_ID', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.FloatField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    active = models.FloatField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Login_Normal'


class Questionoptions(models.Model):
    q_opt_id = models.IntegerField(db_column='Q_opt_ID')  # Field name made lowercase.
    question_options = models.CharField(db_column='Question_Options', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID')  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    next_question = models.IntegerField(db_column='Next_Question', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionOptions'


class QuestionoptionsNormal(models.Model):
    q_opt_id = models.FloatField(db_column='Q_opt_ID', blank=True, null=True)  # Field name made lowercase.
    question_options = models.CharField(db_column='Question_Options', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    question_id = models.FloatField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.FloatField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionOptions_Normal'


class Questions(models.Model):
    question = models.OneToOneField('Responses', models.DO_NOTHING, db_column='Question_ID', primary_key=True)  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID')  # Field name made lowercase.
    question_index = models.IntegerField(db_column='Question_Index')  # Field name made lowercase.
    question_text = models.CharField(db_column='Question_Text', max_length=1500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    question_type = models.CharField(db_column='Question_Type', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    question_options = models.CharField(db_column='Question_Options', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    next_questionindex = models.IntegerField(db_column='Next_QuestionIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questions'


class QuestionsNormal(models.Model):
    question_id = models.FloatField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.FloatField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    question_index = models.FloatField(db_column='Question_Index', blank=True, null=True)  # Field name made lowercase.
    question_text = models.TextField(db_column='Question_Text', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    question_type = models.TextField(db_column='Question_Type', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    question_options = models.TextField(db_column='Question_Options', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questions_Normal'


class Respondent(models.Model):
    newguid = models.CharField(db_column='NewGUID', max_length=36)  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID')  # Field name made lowercase.
    login_id = models.IntegerField(db_column='Login_ID')  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='Start_Time', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='End_Time', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_number = models.CharField(db_column='ID_Number', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='Image_URL', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gps_location = models.CharField(db_column='GPS_Location', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Respondent'


class Respondent1(models.Model):
    respondent_id = models.IntegerField(db_column='Respondent_ID')  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    login_id = models.IntegerField(db_column='Login_ID', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='Start_Time', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='End_Time', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_number = models.CharField(db_column='ID_Number', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='Image_URL', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gps_location = models.CharField(db_column='GPS_Location', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Respondent_1'


class RespondentNormal(models.Model):
    newguid = models.CharField(db_column='NewGUID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    respondent_id = models.FloatField(db_column='Respondent_ID', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.FloatField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    login_id = models.FloatField(db_column='Login_ID', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='Start_Time', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='End_Time', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surname = models.TextField(db_column='Surname', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_number = models.TextField(db_column='ID_Number', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image_url = models.TextField(db_column='Image_URL', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gps_location = models.TextField(db_column='GPS_Location', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Respondent_Normal'


class RespondentNormal2(models.Model):
    newguid = models.CharField(db_column='NewGUID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    respondent_id = models.FloatField(db_column='Respondent_ID', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.FloatField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    login_id = models.FloatField(db_column='Login_ID', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='Start_Time', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='End_Time', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surname = models.TextField(db_column='Surname', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_number = models.TextField(db_column='ID_Number', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image_url = models.TextField(db_column='Image_URL', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gps_location = models.TextField(db_column='GPS_Location', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Respondent_Normal2'


class Responses(models.Model):
    responses_id = models.AutoField(db_column='Responses_ID', primary_key=True)  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID')  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID')  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    newguid = models.CharField(db_column='NewGUID', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responses'


class Responses1(models.Model):
    responses_id = models.IntegerField(db_column='Responses_ID')  # Field name made lowercase.
    respondent_id = models.IntegerField(db_column='Respondent_ID')  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID')  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID')  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responses_1'


class ResponsesNormal(models.Model):
    responses_id = models.FloatField(db_column='Responses_ID', blank=True, null=True)  # Field name made lowercase.
    respondent_id = models.FloatField(db_column='Respondent_ID', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.FloatField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    question_id = models.FloatField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responses_Normal'


class ResponsesTemp2(models.Model):
    responses_id = models.FloatField(db_column='Responses_ID', blank=True, null=True)  # Field name made lowercase.
    respondent_id = models.FloatField(db_column='Respondent_ID', blank=True, null=True)  # Field name made lowercase.
    survey_id = models.FloatField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.
    question_id = models.FloatField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    newguid = models.CharField(db_column='NewGUID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responses_Temp2'


class Slider(models.Model):
    slider_id = models.IntegerField(db_column='Slider_ID')  # Field name made lowercase.
    min = models.IntegerField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    max = models.IntegerField(db_column='Max', blank=True, null=True)  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID')  # Field name made lowercase.
    survey_id = models.IntegerField(db_column='Survey_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Slider'


class Survey(models.Model):
    survey_id = models.IntegerField(db_column='Survey_ID')  # Field name made lowercase.
    surveyname = models.CharField(db_column='SurveyName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='Creator', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mastersurvey = models.IntegerField(db_column='MasterSurvey', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Survey'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
