from django.shortcuts import render
from blogs.models import BlogPost
from django.http import HttpResponseRedirect
from forms import NameForm

# Create your views here.
def home(request):
	print 'welcome to my blog'

	blogs = BlogPost.objects.filter(is_published=True)

	context = {
		'blogs' : blogs
	}

	return render(request, 'blogs/index.html', context)


def home_forms(request):
	print 'welcome to my forms'

	if request.method == 'POST':

		form = NameForm(request.POST)

		if form.is_valid():

			return HttpResponseRedirect('/thanks/')

	else:

		form = NameForm()


	context = {
		'form' : form
	}

	return render(request, 'blogs/forms.html', context)