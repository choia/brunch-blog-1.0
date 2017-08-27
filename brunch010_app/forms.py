from django import forms
from .models import Post
from markdownx.fields import MarkdownxFormField

class PostForm(forms.ModelForm):
	content = MarkdownxFormField()
	
	class Meta:
		model = Post
		fields = [
			"user",
			"title",
			"categories",
			"image",
			"content",			
		]