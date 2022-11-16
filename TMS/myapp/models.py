from django.db import models


class Landlord(models.Model):
    lid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    name = models.CharField(max_length=122)
    spouse = models.CharField(max_length=122)
    id = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=122)
    address = models.TextField()
    date = models.DateField()
    gender = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Property(models.Model):
    pid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    name = models.CharField(max_length=122)
    hn = models.CharField(max_length=122)
    landlord = models.CharField(max_length=122)
    location = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name


class House(models.Model):
    hid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    housename = models.CharField(max_length=122)
    desc = models.CharField(max_length=122)
    hrent = models.CharField(max_length=122)
    type = models.CharField(max_length=122)
    property = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.housename


class Tenant(models.Model):
    tid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=122)
    address = models.TextField()
    idtype = models.CharField(max_length=122)
    idn = models.CharField(max_length=122)
    dob = models.DateField()
    date = models.DateField()
    gender = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class HouseAllocation(models.Model):
    hid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    tname = models.CharField(max_length=122)
    housename = models.CharField(max_length=12)
    status = models.CharField(max_length=12)
    deposit = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.tname


class Payment(models.Model):
    pid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    name = models.CharField(max_length=122)
    house = models.CharField(max_length=12)
    hrent = models.CharField(max_length=122)
    month = models.CharField(max_length=122)
    amount = models.CharField(max_length=122)
    balance = models.CharField(max_length=122)
    status = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.name


class Turnover(models.Model):
    tuid = models.AutoField(auto_created=True, serialize=False, primary_key=True)
    name = models.CharField(max_length=122)
    id = models.CharField(max_length=122)
    amount = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name