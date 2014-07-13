from django.core.cache import cache
from HTMLParser import HTMLParser
# from models import ParentCategory, SubCategory

class strip_html(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def get_menu():
	cats = ParentCategory.objects.all().prefetch_related('subs')
	return cats



