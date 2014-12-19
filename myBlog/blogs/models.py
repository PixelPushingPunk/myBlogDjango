from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=250)
	# body = models.TextField(blank=True)
	body = RichTextField(blank=True, config_name='awesome_ckeditor')
	image = models.ImageField(upload_to='blog')

	is_published = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now=True, null=True)

	def __unicode(self):
		return self.title