from django import forms

class jobStatsForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    category = forms.CharField(widget=forms.TextInput(attrs={'class':'chosen-value', 'placeholder':'Search Category'}))
    job_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Search Job Title (optional)'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Location (optional)'}))