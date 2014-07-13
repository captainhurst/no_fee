#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.conf import settings
from twython import Twython
import json
import codecs
import re
import operator
from commonregex import CommonRegex
import mechanize as mech
from BeautifulSoup import BeautifulSoup, NavigableString
from readability.readability import Document
# NLTK STUFF
from auto_content.summarizer import NaiveSummarizer, go_terms
from auto_content.rake import Rake
from textblob import TextBlob
from HTMLParser import HTMLParser


def get_tweets():
	twitter = Twython(settings.TWITTER_APP_KEY,settings.TWITTER_APP_SECRET,settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
	list_data = []
	for i in range(1,8,1):
		ld = twitter.get_list_statuses(slug='first-test-content-list',owner_screen_name='captainhurst',include_rts=1,page=i,count=100)
		list_data.append(ld)
	return list_data[0:20]

def _remove_attrs(soup):
	for tag in soup.findAll(True):
		# tag.attrs = None
		for attribute in ["class", "id", "name", "style"]:del tag[attribute]
	return soup

	# for tag in soup():
	#     for attribute in ["class", "id", "name", "style"]:
	#         del tag[attribute]

def striphtml(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_html_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#tags_to_strip = ['b', 'i', 'u'] -- this is how the stripped ta
def strip_tags(soup, tags_to_strip):
	soup = BeautifulSoup(soup)
	for tag in soup.findAll(True):
		if tag.name in tags_to_strip:
			s = ""
			for c in tag.contents:
				if not isinstance(c, NavigableString):
					c = strip_tags(unicode(c), tags_to_strip)
				s += unicode(c)
			tag.replaceWith(s)
	return soup

def get_only_p_tags(html):
	soup = BeautifulSoup(html)
	soup.find('p').getText()
	return soup

def get_og_img(html):
	soup = BeautifulSoup(html)
	try:	
		metaimg = soup.find("meta", {"property": "og:image"})['content']
	except:
		metaimg = False
	# print 'og img'
	return metatag

def get_post_imgs(html):
	soup = BeautifulSoup(html)
	try:
		imgtag = soup.find("img")
	except:
		imgtag = False
	return imgtag

def get_og_description(html):
	soup = BeautifulSoup(html)
	try:	
		metatag = soup.find("meta", {"property": "og:description"})['content']
	except:
		metatag = False
	# print 'description tag'
	return metatag	

def get_article_stuff(html):
	article_imgs_desc = {}
	soup = BeautifulSoup(html.decode('utf-8'))
	try:	
		metadesc = soup.find("meta", {"property": "og:description"})['content']
	except:
		metadesc = False

	article_imgs_desc['description'] = metadesc 

	try:
		imgtag = soup.find("img")
	except:
		imgtag = False

	article_imgs_desc['imgs'] = imgtag 

	try:	
		metaimg = soup.find("meta", {"property": "og:image"})['content']
	except:
		metaimg = False

	article_imgs_desc['imgs'] = metaimg

	print article_imgs_desc

	return article_imgs_desc


def ungzipResponse(r,b):
    headers = r.info()
    if headers['Content-Encoding']=='gzip':
        import gzip
        gz = gzip.GzipFile(fileobj=r, mode='rb')
        html = gz.read()
        gz.close()
        headers["Content-type"] = "text/html; charset=utf-8"
        r.set_data( html )
        b.set_response(r)
    else:
    	pass



def scrape_links(links):
	# links = [{"url": "http://cnn.it/RMDdbp", "text": "RT @cnnbrk: Jodie Foster married her girlfriend Alexandra Hedison over the weekend, Foster's rep said. http://t.co/kP4w8yGhkW http://t.co/u\u2026", "score": 163, "ht": "CNN", "datetime": "Wed Apr 23 21:29:05 +0000 2014"}, {"url": "http://talkingpointsmemo.com/livewire/bob-goodlatte-obama-clemency-initiative", "text": "Where in the Constitution does it say the president can just decide who gets out of jail? Oh, right there. Huh. http://t.co/JwZgl2mdMB", "score": 20, "ht": "Benjy Sarlin", "datetime": "Wed Apr 23 21:26:48 +0000 2014"}, {"url": "http://bit.ly/1poD8cz", "text": "RT @PBSAmerMasters: We're screening @fiercegreenfilm with the filmmaker (and he's taking your questions!) in 5 mins! Join us here: http://t\u2026", "score": 2, "ht": "PBS", "datetime": "Wed Apr 23 21:26:35 +0000 2014"}, {"url": "http://huff.to/1jPy21U", "text": "GOP lawyers keep silent on Republican governors' attack against the legal profession http://t.co/kW3NhE0U9G", "score": 7, "ht": "HuffPost Politics", "datetime": "Wed Apr 23 21:26:08 +0000 2014"}, {"url": "http://politi.co/1hoFdLG", "text": ".@RealRobinWright will be featured guest at Capitol File event http://t.co/nZGfVckfTZ", "score": 1, "ht": "POLITICO", "datetime": "Wed Apr 23 21:25:56 +0000 2014"}, {"url": "http://slate.me/1lGeHGd", "text": "Should you buy illegal foreign sunscreens on the black market? http://t.co/DZPZoq2e4L", "score": 1, "ht": "Slate", "datetime": "Wed Apr 23 21:25:31 +0000 2014"}, {"url": "http://n.pr/Pup6pk", "text": "RT @allsongs: Stream Rodrigo y Gabriela's '9 Dead Alive' This album is stripped down, truly a treat @RodGab  http://t.co/MfM91jJmPG http://\u2026", "score": 40, "ht": "NPR News", "datetime": "Wed Apr 23 21:23:24 +0000 2014"}, {"url": "http://www.npr.org/blogs/monkeysee/2014/04/23/306166533/on-television-more-transgender-characters-come-into-focus?utm_source=twitter.com&utm_medium=social&utm_campaign=atc&utm_term=nprnews&utm_content=20140423", "text": "RT @npratc: \"trans ppl are being written into the narrative of American culture...as valued &amp; beloved central players\" @ulabeast http://t.c\u2026", "score": 14, "ht": "NPR News", "datetime": "Wed Apr 23 21:23:15 +0000 2014"}, {"url": "http://www.nytimes.com/2014/04/24/business/media/felix-salmon-to-take-on-web-based-role-at-fusion.html", "text": "Whoa. Felix Salmon to Fusion. http://t.co/zgu56SJRmd", "score": 5, "ht": "Josh Barro", "datetime": "Wed Apr 23 21:20:40 +0000 2014"}, {"url": "http://apne.ws/1jB91pV", "text": "Amazon and HBO strike deal to make classic shows like 'The Sopranos' and 'The Wire' available on Prime: http://t.co/OeVmlLcD2Z", "score": 121, "ht": "The Associated Press", "datetime": "Wed Apr 23 21:20:03 +0000 2014"}, {"url": "http://slate.me/1nH2CgN", "text": "What happens when constitutional vigilantes go mainstream: http://t.co/X0FjEtsobS", "score": 6, "ht": "Slate", "datetime": "Wed Apr 23 21:20:01 +0000 2014"}, {"url": "http://bit.ly/VoteRandE", "text": "RT @ReligionEthics: Get us to the promised land! Currently in 2nd with 2 days to vote @TheWebbyAwards! http://t.co/iSfyGxF97D http://t.co/2\u2026", "score": 4, "ht": "PBS", "datetime": "Wed Apr 23 21:19:57 +0000 2014"}, {"url": "http://ow.ly/w5N8r", "text": "RT @frontlinepbs: FRONTLINE's \"Concussion Watch\" is up for a #Webby! Vote by midnight tomorrow to help us win: http://t.co/r0Wr1Z3qzx http:\u2026", "score": 10, "ht": "PBS", "datetime": "Wed Apr 23 21:19:44 +0000 2014"}, {"url": "http://slate.me/1lGeHWt", "text": "How to get your new Twitter profile: http://t.co/PIWqnNEuxd http://t.co/995J0PF6XG", "score": 25, "ht": "Slate", "datetime": "Wed Apr 23 21:19:36 +0000 2014"}, {"url": "http://n.pr/1hkS71I", "text": "Why Are We Spiteful, Even Though It Bites Us Back? http://t.co/EvTL1By5lM", "score": 32, "ht": "NPR News", "datetime": "Wed Apr 23 21:19:12 +0000 2014"}, {"url": "http://n.pr/1hkS5qu", "text": "Scientists Pinpoint Source Of Antarctic 'Quack' http://t.co/pYoiEHYepg", "score": 13, "ht": "NPR News", "datetime": "Wed Apr 23 21:19:11 +0000 2014"}, {"url": "http://n.pr/1hkS6uC", "text": "Brazil Becomes One Of The First To Adopt Internet 'Bill Of Rights' http://t.co/A5ckGD6fvA", "score": 48, "ht": "NPR News", "datetime": "Wed Apr 23 21:19:10 +0000 2014"}, {"url": "http://wapo.st/1jPrwZ6", "text": "What difference does it make? RT @ktumulty: So, what did Hillary Clinton accomplish at the State Department? http://t.co/5Bbir2doJv", "score": 1, "ht": "Igor Bobic", "datetime": "Wed Apr 23 21:18:40 +0000 2014"}]
	# links = [{"url": "http://talkingpointsmemo.com/livewire/sarah-palin-waterboarding", "text": "What difference does it make? RT @ktumulty: So, what did Hillary Clinton accomplish at the State Department? http://t.co/5Bbir2doJv", "score": 1, "ht": "Igor Bobic", "datetime": "Wed Apr 23 21:18:40 +0000 2014"}]
	br = mech.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]   
	# content = []
	# naivesum = NaiveSummarizer()
	# rake = Rake('stoplist.txt')
	# keywords = []
	for i in range(len(links)):
		if links[i]['url'] == False:
			pass
		else:
			response = br.open(links[i]['url'])
			# print response
			html = response.read()
			html = Document(html).summary()
			text = strip_html_tags(html)
			print text
			links[i]['article-text'] = text
			# print len(text)
			# if len(text) < 400:
			# 	links[i]['keywords'] = []
			# else:
			# 	tb = TextBlob(text)
			# 	keywords = tb.np_counts
			# 	keywords = sorted(keywords.iteritems(), key=operator.itemgetter(1), reverse=True)
			# 	links[i]['keywords'] = keywords[0:20]
			# 	print keywords

	print links
	return StreamingHttpResponse(json.dumps(links), content_type="application/json")


def tweet_into_text(tweets):
	tweet_text = ""
	for i in range(len(tweets)):
		for j in range(len(tweets[i])):
			text = tweets[i][j]['text']
			tweet_text += " " + text +"."
		print text
	return tweet_text


def get_handles(tweet_text):
	# handle_regex = u'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9_]+)'
	handle_regex = r'@([a-z0-9_]+)'
	handles = re.findall(handle_regex, tweet_text.lower())
	return handles

def get_hashtags(tweet_text):
	hashtag_regex = r'#[0-9a-zA-Z+_]*'
	hashtags = re.findall(hashtag_regex, tweet_text.lower())
	return hashtags	

def remove_hashtags(tweet_text):
	hashtag_regex = r'#[0-9a-zA-Z+_]*'
	no_hashtags = re.sub(hashtag_regex, " ", tweet_text)
	return no_hashtags

def remove_handles(tweet_text):
	# handle_regex = u'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)'
	handle_regex = u'@([a-zA-Z0-9_]+)'
	no_handles = re.sub(handle_regex, " ", tweet_text)
	return no_handles

def remove_links(tweet_text):
	link_regex = r'(?i)((?:https?://|www\d{0,3}[.])?[a-z0-9.\-]+[.](?:(?:international)|(?:construction)|(?:contractors)|(?:enterprises)|(?:photography)|(?:immobilien)|(?:management)|(?:technology)|(?:directory)|(?:education)|(?:equipment)|(?:institute)|(?:marketing)|(?:solutions)|(?:builders)|(?:clothing)|(?:computer)|(?:democrat)|(?:diamonds)|(?:graphics)|(?:holdings)|(?:lighting)|(?:plumbing)|(?:training)|(?:ventures)|(?:academy)|(?:careers)|(?:company)|(?:domains)|(?:florist)|(?:gallery)|(?:guitars)|(?:holiday)|(?:kitchen)|(?:recipes)|(?:shiksha)|(?:singles)|(?:support)|(?:systems)|(?:agency)|(?:berlin)|(?:camera)|(?:center)|(?:coffee)|(?:estate)|(?:kaufen)|(?:luxury)|(?:monash)|(?:museum)|(?:photos)|(?:repair)|(?:social)|(?:tattoo)|(?:travel)|(?:viajes)|(?:voyage)|(?:build)|(?:cheap)|(?:codes)|(?:dance)|(?:email)|(?:glass)|(?:house)|(?:ninja)|(?:photo)|(?:shoes)|(?:solar)|(?:today)|(?:aero)|(?:arpa)|(?:asia)|(?:bike)|(?:buzz)|(?:camp)|(?:club)|(?:coop)|(?:farm)|(?:gift)|(?:guru)|(?:info)|(?:jobs)|(?:kiwi)|(?:land)|(?:limo)|(?:link)|(?:menu)|(?:mobi)|(?:moda)|(?:name)|(?:pics)|(?:pink)|(?:post)|(?:rich)|(?:ruhr)|(?:sexy)|(?:tips)|(?:wang)|(?:wien)|(?:zone)|(?:biz)|(?:cab)|(?:cat)|(?:ceo)|(?:com)|(?:edu)|(?:gov)|(?:int)|(?:mil)|(?:net)|(?:onl)|(?:org)|(?:pro)|(?:red)|(?:tel)|(?:uno)|(?:xxx)|(?:ac)|(?:ad)|(?:ae)|(?:af)|(?:ag)|(?:ai)|(?:al)|(?:am)|(?:an)|(?:ao)|(?:aq)|(?:ar)|(?:as)|(?:at)|(?:au)|(?:aw)|(?:ax)|(?:az)|(?:ba)|(?:bb)|(?:bd)|(?:be)|(?:bf)|(?:bg)|(?:bh)|(?:bi)|(?:bj)|(?:bm)|(?:bn)|(?:bo)|(?:br)|(?:bs)|(?:bt)|(?:bv)|(?:bw)|(?:by)|(?:bz)|(?:ca)|(?:cc)|(?:cd)|(?:cf)|(?:cg)|(?:ch)|(?:ci)|(?:ck)|(?:cl)|(?:cm)|(?:cn)|(?:co)|(?:cr)|(?:cu)|(?:cv)|(?:cw)|(?:cx)|(?:cy)|(?:cz)|(?:de)|(?:dj)|(?:dk)|(?:dm)|(?:do)|(?:dz)|(?:ec)|(?:ee)|(?:eg)|(?:er)|(?:es)|(?:et)|(?:eu)|(?:fi)|(?:fj)|(?:fk)|(?:fm)|(?:fo)|(?:fr)|(?:ga)|(?:gb)|(?:gd)|(?:ge)|(?:gf)|(?:gg)|(?:gh)|(?:gi)|(?:gl)|(?:gm)|(?:gn)|(?:gp)|(?:gq)|(?:gr)|(?:gs)|(?:gt)|(?:gu)|(?:gw)|(?:gy)|(?:hk)|(?:hm)|(?:hn)|(?:hr)|(?:ht)|(?:hu)|(?:id)|(?:ie)|(?:il)|(?:im)|(?:in)|(?:io)|(?:iq)|(?:ir)|(?:is)|(?:it)|(?:je)|(?:jm)|(?:jo)|(?:jp)|(?:ke)|(?:kg)|(?:kh)|(?:ki)|(?:km)|(?:kn)|(?:kp)|(?:kr)|(?:kw)|(?:ky)|(?:kz)|(?:la)|(?:lb)|(?:lc)|(?:li)|(?:lk)|(?:lr)|(?:ls)|(?:lt)|(?:lu)|(?:lv)|(?:ly)|(?:ma)|(?:mc)|(?:md)|(?:me)|(?:mg)|(?:mh)|(?:mk)|(?:ml)|(?:mm)|(?:mn)|(?:mo)|(?:mp)|(?:mq)|(?:mr)|(?:ms)|(?:mt)|(?:mu)|(?:mv)|(?:mw)|(?:mx)|(?:my)|(?:mz)|(?:na)|(?:nc)|(?:ne)|(?:nf)|(?:ng)|(?:ni)|(?:nl)|(?:no)|(?:np)|(?:nr)|(?:nu)|(?:nz)|(?:om)|(?:pa)|(?:pe)|(?:pf)|(?:pg)|(?:ph)|(?:pk)|(?:pl)|(?:pm)|(?:pn)|(?:pr)|(?:ps)|(?:pt)|(?:pw)|(?:py)|(?:qa)|(?:re)|(?:ro)|(?:rs)|(?:ru)|(?:rw)|(?:sa)|(?:sb)|(?:sc)|(?:sd)|(?:se)|(?:sg)|(?:sh)|(?:si)|(?:sj)|(?:sk)|(?:sl)|(?:sm)|(?:sn)|(?:so)|(?:sr)|(?:st)|(?:su)|(?:sv)|(?:sx)|(?:sy)|(?:sz)|(?:tc)|(?:td)|(?:tf)|(?:tg)|(?:th)|(?:tj)|(?:tk)|(?:tl)|(?:tm)|(?:tn)|(?:to)|(?:tp)|(?:tr)|(?:tt)|(?:tv)|(?:tw)|(?:tz)|(?:ua)|(?:ug)|(?:uk)|(?:us)|(?:uy)|(?:uz)|(?:va)|(?:vc)|(?:ve)|(?:vg)|(?:vi)|(?:vn)|(?:vu)|(?:wf)|(?:ws)|(?:ye)|(?:yt)|(?:za)|(?:zm)|(?:zw))(?:/[^\s()<>]+[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019])?)'
	no_links = re.sub(link_regex, " ", tweet_text)
	return no_links

def clean_twitter_text(tweet_text):
	# twitter_cleanup_regex = r'\b(rt|RT|mt|MT)\b'
	words = r"(\bRT\b)|(\bmt\b)|(\brt\b)|(\bMT\b)|(\bhttp\b)|(\bHTTP\b)|(\bBREAKING\b)|(\bPHOTO\b)|(\bWATCH\b)|(\bVIDEO\b)|(\bICYMI\b)|"
	punctuation = r"(\.\.\.)|(\()|(\))|(\:)|(\,)|(\/\/\.\.\.)|(\bhttp\:\/\/\.\.\.)|(/@)|(\/)|(\<)|(\>)|(\=)|(\+)|(\")|(\')|(\u2026)"
	clean_text = re.sub(punctuation, " ", tweet_text)
	clean_text = re.sub(words, "", clean_text)
	return clean_text#.lower()


def get_keywords(tweet_text):
	rake = Rake('stoplist.txt')
	#rake.stop_words_path('ryan-stoplist.txt')
	keywords = rake.run(tweet_text)
	# terms = go_terms(tweet_text)
	return keywords

def tweet_object(tweets):
	tweet_object_list = []
	for i in range(len(tweets)):
		for ld in range(len(tweets[i])):
			try:
				name = tweets[i][ld]['user']['name']
			except:
				name = False
			
			try:
				datetime = tweets[i][ld]['created_at']
			except:
				datetime = False

			try:
				user_mentions = tweets[i][ld]['entities']['user_mentions']
			except:
				user_mentions = False

			try:
				favorite_count = tweets[i][ld]['favorite_count']
			except:
				favorite_count = 0

			try:
				retweet_count = tweets[i][ld]['retweet_count']
			except:
				retweet_count = 0

			try:
				text = tweets[i][ld]['text']
			except:
				text = False

			try:
				url = tweets[i][ld]['entities']['urls'][0]['expanded_url']
			except:
				url = False

			try:
				image = tweets[i][ld]['entities']['urls'][0]['media_url']
			except:
				image = False				

			try:
				tweet_id = tweets[i][ld]['id']
			except:
				tweet_id = False
			
			d = {
				'tweet_id': tweet_id,
				'text': text,
				'user_mentions': user_mentions,				
				'url': url,
				'image': image,
				'ht': name,
				'datetime': datetime,
				'score': favorite_count + retweet_count,
			}

			# print d

			tweet_object_list.append(d)

	return tweet_object_list



def get_noun_phrase_chunks(text):
	tb = TextBlob(text)
	np = tb.noun_phrases
	return np





