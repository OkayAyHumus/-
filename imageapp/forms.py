from django import forms
from .models import ModelFile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['id'] = 'image-input'


    class Meta:
        model = ModelFile
        fields = ('image',)

# class ProbaForm(forms.ModelForm):   
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['label'].widget.attrs['id'] = 'label'
#         self.fields['proba'].widget.attrs['id'] = 'proba'
     
#     class Meta:
#         model = ModelFile
#         fields = ('label','proba',)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']=field.label

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']=field.label
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')