from django import forms 
from tinymce import TinyMCE 
from projects.models import Projects 


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
    return False


class ProjectForm(forms.ModelForm):
    description = forms.CharField( widget=TinyMCEWidget( 
        attrs={'required': False, 'cols': 30, 'rows': 10} ) ) 
    class Meta:
        model = Projects
        fields = '__all__'

