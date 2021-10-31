from django.db import models


class Staff(models.Model):
    staff_id = models.IntegerField(unique=True, auto_created=True, editable=False, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField()
    date_employed = models.DateField()
    position = models.CharField(max_length=30, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    local = models.CharField(max_length=100, null=True, blank=True)
    SSF_no = models.CharField(max_length=20, null=True, blank=True)
    salary = models.IntegerField( null=True, blank=True)
    telephone = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class TransferHistory(models.Model):
    transfers_id = models.IntegerField(unique=True, auto_created=True, editable=False, primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_transferred = models.DateField()
    transferred_from = models.CharField(max_length=100, null=True, blank=True)
    from_area = models.CharField(max_length=100, null=True, blank=True)
    transferred_to = models.CharField(max_length=100, null=True, blank=True)
    to_area = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return (f" {self.transfers_id} {self.staff_id}")

