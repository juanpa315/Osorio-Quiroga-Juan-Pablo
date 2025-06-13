# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Coe(models.Model):
    coe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coe'
    
    def __str__(self):
        return self.name


class ContractTypes(models.Model):
    contract_type_id = models.AutoField(primary_key=True)
    contract_name = models.CharField(max_length=100)
    contract_description = models.TextField(blank=True, null=True)
    load_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_types'


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    contract_type = models.ForeignKey(ContractTypes, models.DO_NOTHING, db_column='contract_type', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    id_employee = models.AutoField(primary_key=True)
    cedula = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    salary = models.IntegerField()
    date_of_entry = models.DateField()
    withdrawal_date = models.DateField(blank=True, null=True)
    position = models.ForeignKey('JobPositions', models.DO_NOTHING, db_column='position', blank=True, null=True)
    assigned_customers = models.ForeignKey(Customers, models.DO_NOTHING, db_column='assigned_customers', blank=True, null=True)
    seniority = models.ForeignKey('Seniority', models.DO_NOTHING, db_column='seniority', blank=True, null=True)
    coe = models.ForeignKey(Coe, models.DO_NOTHING, db_column='coe', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class JobPositions(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=100)
    junior_salary = models.IntegerField()
    middle_salary = models.IntegerField()
    senior_salary = models.IntegerField()
    coe = models.ForeignKey(Coe, models.DO_NOTHING, db_column='coe', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_positions'


class Seniority(models.Model):
    seniority_id = models.AutoField(primary_key=True)
    seniority_name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seniority'
