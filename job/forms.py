from django import forms
from django.db.models import fields
from .models import Apply,Job

class ApplyForm(forms.ModelForm):
          class Meta:
                    model= Apply
                    fields=["name","email",'website',"upload_cv",'message']