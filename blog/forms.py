from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        

        fields = '__all__' 
        exclude = ['pub_date']
        
        widgets = { # name 필드 위젯을 재정의, Textinput 태그, class는 test 지정
            'title' : forms.TextInput(attrs={'type' : 'title','class' : 'form-control', 'placeholder' : 'Text input'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }