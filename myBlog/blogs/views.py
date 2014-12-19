from django.shortcuts import render
from blogs.models import BlogPost

# Create your views here.
def home(request):
	print 'welcome to my blog'

	blogs = BlogPost.objects.filter(is_published=True)

	context = {
		'blogs' : blogs
	}

	return render(request, 'blogs/index.html', context)