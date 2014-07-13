from articles.models import Category
import pprint


def get_menu(request):
	cats = Category.objects.filter(level=0)#.prefetch_related('subs')
	# print cats
	# for c in cats:
	# 	pprint.pprint(c)
	# 	for s in c.subs.all():
	# 		pprint.pprint(s)
		# pprint.pprint(c.subs.all())
		# for s in c.subs.all():
			# pprint.pprint(s)

	# print cats.subs__set
	return {'header': cats }