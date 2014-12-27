from django.shortcuts import render
from blogs.models import BlogPost
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404 
from forms import NameForm

# Create your views here.
def home(request, id=None):
	if not id: 
		print 'welcome to my blog homepage'

		blogs = BlogPost.objects.filter(is_published=True)

		context = {
			'blogs' : blogs
		}

		return render(request, 'blogs/index.html', context)
	else:
		print 'welcome to my blog single'

		try:

			blogs = BlogPost.objects.filter(pk=id)

			context = {
				'blogs' : blogs
			}

		except BlogPost.DoesNotExist:

			raise Http404

		return render(request, 'blogs/single.html', context)




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