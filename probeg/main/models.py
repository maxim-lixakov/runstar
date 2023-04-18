# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Klb1(models.Model):
    idklb = models.AutoField(db_column='IDKLB', primary_key=True)  # Field name made lowercase.
    titul = models.CharField(max_length=100)
    dj_is_active = models.IntegerField()
    dj_is_member_list_visible = models.IntegerField()
    members_can_pay_themselves = models.IntegerField()
    strana = models.CharField(db_column='Strana', max_length=100)  # Field name made lowercase.
    obl = models.CharField(db_column='Obl', max_length=100)  # Field name made lowercase.
    gorod = models.CharField(db_column='Gorod', max_length=100)  # Field name made lowercase.
    www = models.CharField(max_length=200)
    emblema = models.CharField(db_column='Emblema', max_length=100)  # Field name made lowercase.
    logo = models.CharField(max_length=255)
    logo_thumb = models.CharField(max_length=255)
    url_vk = models.CharField(max_length=100)
    url_facebook = models.CharField(max_length=100)
    datasozdan = models.DateField(db_column='DataSozdan', blank=True, null=True)  # Field name made lowercase.
    nmembers = models.IntegerField(db_column='NMembers', blank=True, null=True)  # Field name made lowercase.
    adres = models.CharField(db_column='Adres', max_length=200)  # Field name made lowercase.
    email = models.CharField(max_length=100)
    tfonklb = models.CharField(max_length=50)
    tfon = models.CharField(max_length=50)
    tfonrab = models.CharField(max_length=50)
    tfondom = models.CharField(max_length=50)
    othercontacts = models.CharField(db_column='OtherContacts', max_length=200)  # Field name made lowercase.
    predsedatel = models.CharField(db_column='Predsedatel', max_length=100)  # Field name made lowercase.
    adrespr = models.CharField(db_column='AdresPr', max_length=200)  # Field name made lowercase.
    emailpr = models.CharField(db_column='emailPr', max_length=100)  # Field name made lowercase.
    prcontacticq = models.CharField(db_column='PrContactICQ', max_length=100)  # Field name made lowercase.
    prcontactskype = models.CharField(db_column='PrContactSkype', max_length=100)  # Field name made lowercase.
    head_vk = models.CharField(max_length=100)
    head_facebook = models.CharField(max_length=100)
    dj_head_other_contacts = models.CharField(max_length=200)
    dj_speaker_name = models.CharField(max_length=100)
    dj_speaker_email = models.CharField(max_length=100)
    color = models.CharField(max_length=7)
    tales = models.TextField(db_column='Tales')  # Field name made lowercase.
    dj_training_timetable = models.CharField(max_length=100)
    dj_training_cost = models.CharField(max_length=100)
    added_time = models.DateTimeField(blank=True, null=True)
    last_update_time = models.DateTimeField(blank=True, null=True)
    dj_comment_private = models.CharField(max_length=250)
    dj_city = models.ForeignKey('DjCity', models.DO_NOTHING, blank=True, null=True)
    dj_country = models.ForeignKey('DjCountry', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'klb1'


class DjCountry(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length=100)
    nameen = models.CharField(db_column='nameEn', max_length=100)  # Field name made lowercase.
    prep_case = models.CharField(max_length=100)
    value = models.SmallIntegerField()
    has_regions = models.SmallIntegerField()
    code = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'dj_country'



class Probegdist(models.Model):
    probeg_id = models.IntegerField(db_column='Probeg_id')  # Field name made lowercase.
    dj_surface_type = models.SmallIntegerField()
    dist = models.DecimalField(db_column='Dist', max_digits=8, decimal_places=4)  # Field name made lowercase.
    dj_ak_distance_raw = models.CharField(max_length=10)
    dist_ed = models.CharField(db_column='Dist_ed', max_length=3)  # Field name made lowercase.
    n_s = models.IntegerField(db_column='N_s', blank=True, null=True)  # Field name made lowercase.
    dj_n_participants_men = models.IntegerField(blank=True, null=True)
    n_u = models.IntegerField(db_column='N_u', blank=True, null=True)  # Field name made lowercase.
    n_m = models.IntegerField(db_column='N_m', blank=True, null=True)  # Field name made lowercase.
    namep1 = models.CharField(db_column='NameP1', max_length=100)  # Field name made lowercase.
    namep2 = models.CharField(db_column='NameP2', max_length=100)  # Field name made lowercase.
    koordp = models.CharField(db_column='KoordP', max_length=100)  # Field name made lowercase.
    rez = models.CharField(db_column='Rez', max_length=10)  # Field name made lowercase.
    dj_is_male_course_record = models.IntegerField()
    namep1f = models.CharField(db_column='NameP1f', max_length=100)  # Field name made lowercase.
    namep2f = models.CharField(db_column='NameP2f', max_length=100)  # Field name made lowercase.
    koordpf = models.CharField(db_column='KoordPf', max_length=100)  # Field name made lowercase.
    rezf = models.CharField(db_column='Rezf', max_length=10)  # Field name made lowercase.
    dj_is_female_course_record = models.IntegerField()
    komm = models.CharField(db_column='Komm', max_length=250)  # Field name made lowercase.
    dj_comment_private = models.CharField(max_length=250)
    dj_precise_name = models.CharField(max_length=50)
    dj_gps_track = models.CharField(max_length=300)
    dj_start_date = models.DateField(blank=True, null=True)
    dj_start_time = models.TimeField(blank=True, null=True)
    dj_finish_date = models.DateField(blank=True, null=True)
    dj_elevation_meters = models.IntegerField(blank=True, null=True)
    dj_descent_meters = models.IntegerField(blank=True, null=True)
    dj_altitude_start_meters = models.IntegerField(blank=True, null=True)
    dj_altitude_finish_meters = models.IntegerField(blank=True, null=True)
    dj_start_lat = models.FloatField(blank=True, null=True)
    dj_start_lon = models.FloatField(blank=True, null=True)
    dj_loaded = models.SmallIntegerField()
    dj_loaded_from = models.CharField(max_length=200)
    dj_was_checked_for_klb = models.IntegerField()
    dj_has_no_results = models.IntegerField()
    dj_is_for_handicapped = models.IntegerField()
    dj_is_multiday = models.IntegerField()
    dj_timing = models.SmallIntegerField()
    dj_price = models.IntegerField(blank=True, null=True)
    dj_price_can_change = models.IntegerField()
    itra_score = models.SmallIntegerField()

    class Meta:
        db_table = 'probegdist'


class DjCategorySize(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField(blank=True, null=True)
    race = models.ForeignKey('Probegdist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dj_category_size'
        unique_together = (('race', 'name'),)


class DjCity(models.Model):
    raion = models.CharField(max_length=100)
    city_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    nameen = models.CharField(db_column='nameEn', max_length=100)  # Field name made lowercase.
    url_wiki = models.CharField(max_length=200)
    skip_region = models.IntegerField()
    added_time = models.DateTimeField()

    class Meta:
        db_table = 'dj_city'



class DjRunner(models.Model):
    ak_person_id = models.CharField(max_length=6, blank=True, null=True)
    parkrun_id = models.IntegerField(unique=True, blank=True, null=True)
    lname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    midname = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    birthday_known = models.IntegerField()
    gender = models.SmallIntegerField()
    club_name = models.CharField(max_length=100)
    deathday = models.DateField(blank=True, null=True)
    url_wiki = models.CharField(max_length=200)
    n_starts = models.SmallIntegerField(blank=True, null=True)
    total_length = models.IntegerField(blank=True, null=True)
    total_time = models.BigIntegerField(blank=True, null=True)
    has_many_distances = models.IntegerField()
    n_parkrun_results = models.IntegerField()
    comment_private = models.CharField(max_length=250)
    private_data_hidden = models.IntegerField()
    last_find_results_try = models.DateField(blank=True, null=True)
    added_time = models.DateTimeField(blank=True, null=True)
    city = models.ForeignKey('DjCity', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'dj_runner'


class DjResult(models.Model):
    ak_person_id = models.CharField(max_length=6, blank=True, null=True)
    parkrun_id = models.IntegerField(blank=True, null=True)
    country_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    club_name = models.CharField(max_length=100)
    name_raw = models.CharField(max_length=100)
    lname_raw = models.CharField(max_length=100)
    fname_raw = models.CharField(max_length=70)
    midname_raw = models.CharField(max_length=50)
    time_raw = models.CharField(max_length=20)
    gun_time_raw = models.CharField(max_length=20)
    country_raw = models.CharField(max_length=100)
    region_raw = models.CharField(max_length=100)
    city_raw = models.CharField(max_length=100)
    club_raw = models.CharField(max_length=100)
    birthyear_raw = models.SmallIntegerField(blank=True, null=True)
    birthday_raw = models.DateField(blank=True, null=True)
    age_raw = models.SmallIntegerField(blank=True, null=True)
    place_raw = models.IntegerField(blank=True, null=True)
    place_gender_raw = models.IntegerField(blank=True, null=True)
    place_category_raw = models.IntegerField(blank=True, null=True)
    comment_raw = models.CharField(max_length=200)
    status_raw = models.SmallIntegerField()
    bib_raw = models.CharField(max_length=10)
    category_raw = models.CharField(max_length=100)
    gender_raw = models.CharField(max_length=10)
    result = models.IntegerField()
    gun_result = models.IntegerField(blank=True, null=True)
    time_for_car = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField()
    place = models.IntegerField(blank=True, null=True)
    place_gender = models.IntegerField(blank=True, null=True)
    place_category = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=200)
    bib = models.CharField(max_length=10)
    birthday = models.DateField(blank=True, null=True)
    birthday_known = models.IntegerField()
    age = models.SmallIntegerField(blank=True, null=True)
    lname = models.CharField(max_length=100)
    fname = models.CharField(max_length=70)
    midname = models.CharField(max_length=50)
    gender = models.SmallIntegerField()
    do_not_count_in_stat = models.IntegerField()
    source = models.SmallIntegerField()
    added_time = models.DateTimeField()
    last_update = models.DateTimeField()
    category_size = models.ForeignKey('DjCategorySize', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('DjCity', models.DO_NOTHING, blank=True, null=True)
    club = models.ForeignKey('Klb1', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('DjCountry', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'dj_result'

