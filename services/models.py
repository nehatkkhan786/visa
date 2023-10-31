from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class VisaServices(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    details = models.TextField()
    requirements = models.CharField(max_length=200)
    processing_time = models.CharField(max_length=50)
    fees = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.title
    

class VisaApplications(models.Model):

    ADDRESS_TYPE = (
        ('dl', 'Driving License'),
        ('passport', 'Passport'),
        ('adhar', 'Adhar Card'),
    )

    VISA_STATUS = (
        ('pending', 'Pending'), 
        ('verified', 'Verified'), 
        ('rejected', 'Rejected'), 
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    visa_service = models.ForeignKey(VisaServices, on_delete=models.SET_NULL, blank=True , null=True)
    address_proof_type = models.CharField(choices=ADDRESS_TYPE, max_length=10)
    address_proof = models.FileField(upload_to='files/')
    id_proof_type = models.CharField(choices=ADDRESS_TYPE, max_length=50)
    id_proof = models.FileField(upload_to='files/')
    phone = models.CharField(max_length=10)
    status = models.CharField(choices=VISA_STATUS, max_length=50)

    # def __str__():
    #     return user.username



