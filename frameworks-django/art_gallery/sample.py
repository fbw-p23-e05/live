# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Art_Pieces(models.Model):
    art_piece_id = models.AutoField(primary_key=True)
    art_piece_name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)
    date_of_creation = models.DateField(blank=True, null=True)
    genre = models.TextField()
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    artist = models.ForeignKey('Artists', models.DO_NOTHING, blank=True, null=True)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    museum = models.ForeignKey('Museums', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'art_pieces'
        unique_together = (('artist', 'art_piece_name'),)
        

class ArtPiecesBkp(models.Model):
    art_piece_id = models.AutoField()
    art_piece_name = models.TextField()
    description = models.TextField(blank=True, null=True)
    date_of_creation = models.DateField(blank=True, null=True)
    genre = models.TextField()
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    artist_id = models.IntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    museum_id = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'art_pieces_bkp'


class Artists(models.Model):
    artist_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField(blank=True, null=True)
    email_address = models.CharField(unique=True, max_length=100)
    art_style = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    phone_numbers = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'artists'
        unique_together = (('first_name', 'last_name'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
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


class Clients(models.Model):
    client_id = models.UUIDField(primary_key=True)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_img = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class DemoStamp(models.Model):
    ts_1 = models.DateTimeField(blank=True, null=True)
    ts_2 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_stamp'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Museums(models.Model):
    location_id = models.UUIDField(primary_key=True)
    location_name = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'museums'


class Shifts(models.Model):
    shift_id = models.AutoField(primary_key=True)
    shift_name = models.CharField()
    start_at = models.TimeField()
    end_at = models.TimeField()

    class Meta:
        managed = False
        db_table = 'shifts'


class StockVisitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    visitor_name = models.CharField(max_length=150)
    time_of_visit = models.DateTimeField()
    purchases = models.TextField()

    class Meta:
        managed = False
        db_table = 'stock_visitor'


class StockWarehouse(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
