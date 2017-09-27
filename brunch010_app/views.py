from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm
from .models import Post


'''Main Home Page'''
def post_home(request):
	queryset_list = Post.objects.all().order_by('-date_added')
	paginator = Paginator(queryset_list, 6)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"queryset": queryset,
	}

	return render(request, 'index.html', context)


'''Create Post Page'''
def post_create(request):
	if request.method != 'POST':
		form = PostForm()
	else:
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('brunch010:post_home'))

	context = {
		"form": form
	}

	return render(request, 'forms.html', context)


'''Detailed Post Page'''
def post_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
		"instance": instance,
	}

	return render(request, 'detail.html', context)


'''Update Post Page'''
def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	if request.method != 'POST':
		form = PostForm(instance=instance)
	else:	
		form = PostForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}

	return render(request, 'forms.html', context)


'''Delete Post Page'''
def post_delete(request):
	context = {}

	return render(request, 'delete.html', context)

