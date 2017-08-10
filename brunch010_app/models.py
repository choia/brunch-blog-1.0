from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
	title = models.CharField(max_length=180)
	email = models.EmailField()
	# content = models.TextField()
	content = MarkdownxField()
	date_added = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	image = models.ImageField(null=True, blank=True, height_field="height_field", width_field="width_field")


	def __str__(self):
		return self.title
	

	def get_absolute_url(self):
		return reverse("brunch010:post_detail", kwargs={"id": self.id})


	def get_html(self):
		return markdownify(self.content)
