from django import forms



class ArticleForm(forms.Form):
    title = forms.CharField(
        label='文章标题',
        required=True,
        max_length=32,
        min_length=1,
        widget=forms.widgets.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    content = forms.CharField(
        label='文章内容',
        required=True,
        widget=forms.widgets.Textarea(

        )
    )