from django import forms
from django.contrib.auth.models import User
from . import models
from school.models import Fee , Payment ,StudentExtra,TeacherExtra
 

#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


#for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['roll','cl','mobile','fee','status']
        def __init__(self, *args, **kwargs):
            super(StudentExtraForm, self).__init__(*args, **kwargs)
            self.fields['fee'].widget.attrs['readonly'] = True
            self.fields['cl'].widget.attrs['onchange'] = 'updateFee()'
            self.fields['fee'].initial = Fee.objects.get(cl='default').amount

#for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields=['salary','mobile','status']




#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()




#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'



#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class FeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['cl', 'amount']
        widgets = {
            'cl': forms.TextInput(attrs={'readonly': 'readonly'}),
            'amount': forms.NumberInput(attrs={'min': 0}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'amount_received', 'date_received', 'collected_by']

# class StudentPaymentForm(forms.Form):
#     cl = forms.CharField(max_length=10, widget=forms.Select(choices=[('one','one'),('two','two'),('three','three'),
# ('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]))
#     student = forms.ModelChoiceField(queryset=StudentExtra.objects.all(), to_field_name='user_id', label='Student')
#     fees_received = forms.DecimalField(min_value=0)
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     collected_by = forms.ModelChoiceField(queryset=TeacherExtra.objects.all(), to_field_name='user_id', label='Collected By')

#     class Meta:
#         model = Payment
#         fields = ['cl', 'student', 'fees_received', 'date', 'collected_by']

#     def __init__(self, *args, **kwargs):
#         super(StudentPaymentForm, self).__init__(*args, **kwargs)

#         # Dynamically load choices for collected_by field
#         teachers = TeacherExtra.objects.filter(status=True)
#         teacher_choices = [(teacher.user_id, teacher.get_name) for teacher in teachers]
#         self.fields['collected_by'].choices = teacher_choices



class PaymentForm(forms.Form):
    fees_received = forms.DecimalField(min_value=0)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date')
    collected_by = forms.ModelChoiceField(queryset=TeacherExtra.objects.all(), to_field_name='user_id', label='Collected By')

    # def __init__(self, *args, **kwargs):
    #     first_day_of_month = kwargs.pop('first_day_of_month', None)
    #     last_day_of_month = kwargs.pop('last_day_of_month', None)
    #     initial_date = kwargs.pop('initial_date', None)
    #     super(PaymentForm, self).__init__(*args, **kwargs)
        
    #     if first_day_of_month and last_day_of_month:
    #         self.fields['date'].widget.attrs['min'] = first_day_of_month.strftime('%Y-%m-%d')
    #         self.fields['date'].widget.attrs['max'] = last_day_of_month.strftime('%Y-%m-%d')
    #     if initial_date:
    #         self.fields['date'].widget.attrs['value'] = initial_date.strftime('%Y-%m-%d')

