# AJ Social - Clone Social Blog
This is clone social blog project called AJ Social

- External modules installed: misaka, bootstrap4, django-braces

- Django-braces: Allows us to access some convenient Mixins to use with CBVs

- Debug: Using Django Debug Toolbar 

** Note:
- Couldn't install misaka, django-misaka even tried multiple methods as recommended
	+ At groups/models.py changed 
  	self.description_html = misaka.html(self.description)
  	=> self.description_html = self.description