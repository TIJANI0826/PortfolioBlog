from django import forms 
from tinymce.widgets import TinyMCE
from projects.models import Projects,Participant


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class ProjectForm(forms.ModelForm):
    description = forms.CharField( widget=TinyMCEWidget( 
        attrs={'required': False, 'cols': 30, 'rows': 10} ) ) 
    class Meta:
        model = Projects
        fields = '__all__'



class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'phone']


