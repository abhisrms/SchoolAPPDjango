from django.db import models
from django.contrib.auth.models import User
from import_export import resources
from import_export.fields import Field
# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee = models.PositiveIntegerField() 
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
          return f"{self.user.first_name} {self.user.last_name}"



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)


class Fee(models.Model):
    cl = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cl

class Payment(models.Model):
    student = models.ForeignKey(StudentExtra, on_delete=models.CASCADE)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_fee = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()
    collected_by = models.ForeignKey(TeacherExtra, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.student.get_name} - {self.date_received}"


class StudentExportResource(resources.ModelResource):
    first_name = Field(attribute='user__first_name', column_name='First Name')
    last_name = Field(attribute='user__last_name', column_name='Last Name')
    username = Field(attribute='user__username', column_name='Username')
    # password = Field(column_name='Password')  # You may not want to export passwords for security reasons
    roll = Field(attribute='roll', column_name='Roll')
    mobile = Field(attribute='mobile', column_name='Mobile')
    fee = Field(attribute='fee', column_name='Fee')
    cl = Field(attribute='cl', column_name='Class')
    status = Field(attribute='status', column_name='Status')

    class Meta:
        model = StudentExtra
        fields = ('first_name', 'last_name', 'username', 'roll', 'mobile', 'fee', 'cl', 'status')
        export_order = fields