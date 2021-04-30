from django import forms
from .models import Post, Category, Comment
from ckeditor.fields import RichTextField


# choices = [('coding', 'Coding'), ('anime', 'Anime'), ('entertainment', 'Entertainment')]
choices = [item for item in Category.objects.all().values_list('name', 'name')]

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'featured_image', 'summary', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-form trans-bg'}),
            'author': forms.TextInput(attrs={'class': 'input-form trans-bg', 'type': 'hidden', 'id': 'author'}),
            'category': forms.Select(choices=choices, attrs={'class': 'input-form trans-bg'}),
            'summary': forms.TextInput(attrs={'class': 'input-form trans-bg'}),
            'body': RichTextField()
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'class': 'input-form trans-bg'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'summary', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-form trans-bg'}),
            'summary': forms.TextInput(attrs={'class': 'input-form trans-bg'}),
            'body': RichTextField(),
            'category': forms.Select(choices=choices, attrs={'class': 'input-form trans-bg'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'textarea-form trans-bg', 'rows': 6, 'placeholder': 'Enter your comment...'}),
        }