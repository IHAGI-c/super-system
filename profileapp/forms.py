from django.forms import ModelForm

from profileapp.models import profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = profile
        fields = ['image','nickname', 'message']
        