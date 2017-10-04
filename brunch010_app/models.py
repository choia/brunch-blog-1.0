from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


def upload_location(instance, filename):
	return "%s/%s" % (instance.id, filename)


class Post(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	categories = models.CharField(max_length=25)
	title = models.CharField(max_length=180)
	email = models.EmailField()
	content = MarkdownxField()
	date_added = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True, height_field="height_field", width_field="width_field")


	def __str__(self):
		return self.title
	

	def get_absolute_url(self):
		return reverse("brunch010:post_detail", kwargs={"id": self.id})


	def get_html(self):
		return markdownify(self.content)


	def get_next(self):
		next = Post.objects.filter(id__gt=self.id)
		if next:
			return next.first()
		return False


	def get_prev(self):
		prev = Post.objects.filter(id__lt=self.id).order_by('-id')
		if prev:
			return prev.first()
		return False


