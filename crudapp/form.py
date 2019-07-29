from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'content', 'date']

        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'제목을 입력하세요',
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':'5',
                }
            ),

            'date':forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date',
                }
            ),
        }

        labels = {
            'title':'제목',
            'content':'내용',
            'date':'날짜',
        }
