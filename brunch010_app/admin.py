from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ["__str__", "date_added", "date_updated"]
	class Meta:
		model = Post

		
admin.site.register(Post, PostAdmin)
