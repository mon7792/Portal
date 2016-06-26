from django import forms
from .models import User
'''
Django Crispy
'''
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from crispy_forms.bootstrap import TabHolder, Tab



class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):    
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    'Personal',
                    'first_name',
                    'last_name',
                    'email',
                    'Bio',
                    'CapGID',
                    'DOB',
                    ),
                Tab(
                    'SJM',
                    'SJMID',
                    'SJMBillableDate',
                    'SJMEMAILID',
                    ),
                Tab(
                    'ODC',
                    'DeskNo',
                    ),
                Tab(
                    'Designation',
                    'ROLE',
                    'MANAGER',
                    )
            ),
            
        )
    class Meta:
        model = User
        fields = ('first_name','last_name','email','Bio','CapGID','DOB','SJMID','SJMBillableDate', 'SJMEMAILID', 'DeskNo', 'ROLE', 'MANAGER',)
        #code
