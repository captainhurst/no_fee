from articles.models import Category
from corp_page.models import CorpPage
import pprint


def get_menu(request):
	# cats = Category.objects.filter(level=0)#.prefetch_related('subs')
	cats = Category.objects.all()
	corp = CorpPage.objects.filter(isLive=True).order_by('PageName')
	# print cats
	# for c in cats:
	# 	pprint.pprint(c)
	# 	for s in c.subs.all():
	# 		pprint.pprint(s)
		# pprint.pprint(c.subs.all())
		# for s in c.subs.all():
			# pprint.pprint(s)

	# print cats.subs__set
	return {'nodes': cats, 'corp': corp }