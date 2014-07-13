def scrape_links(links):
	#links = [{"url": "http://cnn.it/RMDdbp", "text": "RT @cnnbrk: Jodie Foster married her girlfriend Alexandra Hedison over the weekend, Foster's rep said. http://t.co/kP4w8yGhkW http://t.co/u\u2026", "score": 163, "ht": "CNN", "datetime": "Wed Apr 23 21:29:05 +0000 2014"}, {"url": "http://talkingpointsmemo.com/livewire/bob-goodlatte-obama-clemency-initiative", "text": "Where in the Constitution does it say the president can just decide who gets out of jail? Oh, right there. Huh. http://t.co/JwZgl2mdMB", "score": 20, "ht": "Benjy Sarlin", "datetime": "Wed Apr 23 21:26:48 +0000 2014"}, {"url": "http://bit.ly/1poD8cz", "text": "RT @PBSAmerMasters: We're screening @fiercegreenfilm with the filmmaker (and he's taking your questions!) in 5 mins! Join us here: http://t\u2026", "score": 2, "ht": "PBS", "datetime": "Wed Apr 23 21:26:35 +0000 2014"}, {"url": "http://huff.to/1jPy21U", "text": "GOP lawyers keep silent on Republican governors' attack against the legal profession http://t.co/kW3NhE0U9G", "score": 7, "ht": "HuffPost Politics", "datetime": "Wed Apr 23 21:26:08 +0000 2014"}, {"url": "http://politi.co/1hoFdLG", "text": ".@RealRobinWright will be featured guest at Capitol File event http://t.co/nZGfVckfTZ", "score": 1, "ht": "POLITICO", "datetime": "Wed Apr 23 21:25:56 +0000 2014"}, {"url": "http://slate.me/1lGeHGd", "text": "Should you buy illegal foreign sunscreens on the black market? http://t.co/DZPZoq2e4L", "score": 1, "ht": "Slate", "datetime": "Wed Apr 23 21:25:31 +0000 2014"}, {"url": "http://n.pr/Pup6pk", "text": "RT @allsongs: Stream Rodrigo y Gabriela's '9 Dead Alive' This album is stripped down, truly a treat @RodGab  http://t.co/MfM91jJmPG http://\u2026", "score": 40, "ht": "NPR News", "datetime": "Wed Apr 23 21:23:24 +0000 2014"}, {"url": "http://www.npr.org/blogs/monkeysee/2014/04/23/306166533/on-television-more-transgender-characters-come-into-focus?utm_source=twitter.com&utm_medium=social&utm_campaign=atc&utm_term=nprnews&utm_content=20140423", "text": "RT @npratc: \"trans ppl are being written into the narrative of American culture...as valued &amp; beloved central players\" @ulabeast http://t.c\u2026", "score": 14, "ht": "NPR News", "datetime": "Wed Apr 23 21:23:15 +0000 2014"}, {"url": "http://www.nytimes.com/2014/04/24/business/media/felix-salmon-to-take-on-web-based-role-at-fusion.html", "text": "Whoa. Felix Salmon to Fusion. http://t.co/zgu56SJRmd", "score": 5, "ht": "Josh Barro", "datetime": "Wed Apr 23 21:20:40 +0000 2014"}, {"url": "http://apne.ws/1jB91pV", "text": "Amazon and HBO strike deal to make classic shows like 'The Sopranos' and 'The Wire' available on Prime: http://t.co/OeVmlLcD2Z", "score": 121, "ht": "The Associated Press", "datetime": "Wed Apr 23 21:20:03 +0000 2014"}, {"url": "http://slate.me/1nH2CgN", "text": "What happens when constitutional vigilantes go mainstream: http://t.co/X0FjEtsobS", "score": 6, "ht": "Slate", "datetime": "Wed Apr 23 21:20:01 +0000 2014"}, {"url": "http://bit.ly/VoteRandE", "text": "RT @ReligionEthics: Get us to the promised land! Currently in 2nd with 2 days to vote @TheWebbyAwards! http://t.co/iSfyGxF97D http://t.co/2\u2026", "score": 4, "ht": "PBS", "datetime": "Wed Apr 23 21:19:57 +0000 2014"}, {"url": "http://ow.ly/w5N8r", "text": "RT @frontlinepbs: FRONTLINE's \"Concussion Watch\" is up for a #Webby! Vote by midnight tomorrow to help us win: http://t.co/r0Wr1Z3qzx http:\u2026", "score": 10, "ht": "PBS", "datetime": "Wed Apr 23 21:19:44 +0000 2014"}, {"url": "http://slate.me/1lGeHWt", "text": "How to get your new Twitter profile: http://t.co/PIWqnNEuxd http://t.co/995J0PF6XG", "score": 25, "ht": "Slate", "datetime": "Wed Apr 23 21:19:36 +0000 2014"}, {"url": "http://n.pr/1hkS71I", "text": "Why Are We Spiteful, Even Though It Bites Us Back? http://t.co/EvTL1By5lM", "score": 32, "ht": "NPR News", "datetime": "Wed Apr 23 21:19:12 +0000 2014"}, {"url": "http://n.pr/1hkS5qu", "text": "Scientists Pinpoint Source Of Antarctic 'Quack' http://t.co/pYoiEHYepg", "score": 13, "ht": "NPR News", "datetime": "Wed Apr 23 21:19:11 +0000 2014"}, {"url": "http://n.pr/1hkS6uC", "text": "Brazil Becomes One Of The First To Adopt Internet 'Bill Of Rights' http://t.co/A5ckGD6fvA", "score": 48, "ht": "NPR News", "datetime": "Wed Apr 23 21:19:10 +0000 2014"}, {"url": "http://wapo.st/1jPrwZ6", "text": "What difference does it make? RT @ktumulty: So, what did Hillary Clinton accomplish at the State Department? http://t.co/5Bbir2doJv", "score": 1, "ht": "Igor Bobic", "datetime": "Wed Apr 23 21:18:40 +0000 2014"}]
	links = [{"url": "http://www.businessinsider.com/tim-cook-ipad-sales-2014-4", "text": "What difference does it make? RT @ktumulty: So, what did Hillary Clinton accomplish at the State Department? http://t.co/5Bbir2doJv", "score": 1, "ht": "Igor Bobic", "datetime": "Wed Apr 23 21:18:40 +0000 2014"}]
	# print links
	br = mech.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]   
	content = []
	# naivesum = NaiveSummarizer()
	for i in range(len(links)):
		response = br.open(links[i]['url'])
		# ungzipResponse(response, br)
		html = response.read()
		article_imgs_desc =  get_article_stuff(html.decode('utf-8'))
		# og_img = get_og_img(html)
		# og_description = get_og_description(html)
		try:		
			article_title = Document(html).short_title()	
		except:
			article_title = False
		
		print article_title

		try:				
			html = Document(html).summary()
			tags_to_strip =         ['html', 'body', 'body div', 'div', 'span', 'object', 'iframe', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'pre', 'abbr', 'address', 'cite', 'code', 'del', 'dfn', 'em', 'img', 'ins', 'kbd', 'q', 'samp', 'small', 'strong', 'sub', 'sup', 'var', 'b', 'i', 'dl', 'dt', 'dd', 'ol', 'ul', 'li', 'fieldset', 'form', 'label', 'legend', 'table', 'caption', 'tbody', 'tfoot', 'thead', 'tr', 'th', 'td', 'article', 'aside', 'figure', 'footer', 'header', 'menu', 'nav', 'section', 'time', 'mark', 'audio', 'video', 'details', 'summary', 'p']
			# tags_to_strip_summary = ['html', 'body', 'body div', 'div', 'span', 'object', 'iframe', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'pre', 'abbr', 'address', 'cite', 'code', 'del', 'dfn', 'em', 'img', 'ins', 'kbd', 'q', 'samp', 'small', 'strong', 'sub', 'sup', 'var', 'b', 'i', 'dl', 'dt', 'dd', 'ol', 'ul', 'li', 'fieldset', 'form', 'label', 'legend', 'table', 'caption', 'tbody', 'tfoot', 'thead', 'tr', 'th', 'td', 'article', 'aside', 'figure', 'footer', 'header', 'menu', 'nav', 'section', 'time', 'mark', 'audio', 'video', 'details', 'summary']
			clean_soup = strip_tags(html, tags_to_strip)
			clean_soup = _remove_attrs(clean_soup).decode('utf-8')
			# print 'clean_soup'
			# print clean_soup
			# clean_soup_summary = strip_tags(html, tags_to_strip_summary)
			# clean_soup_summary = str(_remove_attrs(clean_soup_summary))
			# print 'clean_soup_summary'
			# print clean_soup_summary
			# print 'summary'
			# top_sentences = naivesum.summarize(clean_soup_summary, 4)
			# print 'top_sentences'
			# print top_sentences
		except:
			# top_sentences = False
			clean_soup = False

		html_title = br.title()
		# print 'title'
		# print 'url:' + links[i]['url']
		c ={
			'tweet_id': links[i]['tweet_id'],
			'url': links[i]['url'],
			'ht': links[i]['ht'],
			'datetime': links[i]['datetime'],
			'score': links[i]['score'],
			'tweet_text': links[i]['text'],
			# 'og_img': og_img,
			# 'og_description': og_description,
			'page_title': html_title,
			'article_title': article_title,
			'article_text': clean_soup,
			'article_imgs_desc': article_imgs_desc,
			# 'article_summary': top_sentences,
		}
		# print c
		content.append(c)
	return StreamingHttpResponse(content)


# def get_keywords(tweets):
# 	tweet_text = ""
# 	for i in range(len(tweets)):
# 		for j in range(len(tweets[i])):
# 			text = tweets[i][j]['text']
# 			tweet_text += " " + text
# 		print i





    # return re.compile(regex_str, re.IGNORECASE)
    # stripped_text = re.sub(stopwordpattern, " ", text)
    # # print stripped_text
    # return stripped_text
    #     print regex_list

# def build_stop_word_regex():
#     pass




# def build_stop_word_regex(stop_word_file_path):
#     stop_word_list = load_stop_words(stop_word_file_path)
#     stop_word_regex_list = []
#     for word in stop_word_list:
#         word_regex = '(\\b' + word + '\\b)'
#         # print word_regex        
#         stop_word_regex_list.append(word_regex)
#     # return stop_word_regex_list
#     regex_str = ""
#     # list_range = range(len(stop_word_regex_list))
#     # print list_len
#     for w in range(len(stop_word_regex_list)):
#         if w == 0:
#             regex_str += stop_word_regex_list[w]
#         else:
#             regex_str += "|"+stop_word_regex_list[w]
#     # regex_list = stop_word_regex_list()
#     # print regex_list
#     # print regex_str
#     # regex_list = re.compile(regex_str, re.IGNORECASE)
#     # print regex_list
#     # lists_of_regex = regex_list.chunks(list_range, 100))
#     # print lists_of_regex
#     # return re.compile(regex_str, re.IGNORECASE)
#     # return re.compile(regex_str, re.IGNORECASE)
#     # print stop_word_regex_list
#     #stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
#     #return r"%s", regex_str
#     #return stop_word_pattern



    # print sentences_list
    # phrases = []
    # for s in range(len(stop_word_regex_list)):
    #     regex_str2 = ""
    #     for w in range(len(stop_word_regex_list[s])):
    #         if w == 0:
    #             regex_str2 += stop_word_regex_list[s][w]
    #         else:
    #             regex_str2 += "|"+stop_word_regex_list[s][w]

    #     strip_list = re.compile(regex_str2, re.IGNORECASE)
    #     # keywords = generate_candidate_keywords(sentences_list, strip_list)
    #     # print keywords
    #     phrases = generate_candidate_keywords(sentences_list, strip_list)
        # print phrases

        # def generate_candidate_keyword_scores(phrase_list, word_score):
#     keyword_candidates = {}
#     for phrase in phrase_list:
#         # print phrase
#         keyword_candidates.setdefault(phrase, 0)
#         word_list = separate_words(phrase, 0)
#         candidate_score = 0
#         # print word_list
#         for word in word_list:
#             print word
#             print word_score[word]
#             candidate_score += word_score[word]
#         keyword_candidates[phrase] = candidate_score
#     # print keyword_candidates
#     return keyword_candidates



# if test:
#     text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types of systems and systems of mixed types."

#     # Split text into sentences
#     sentenceList = split_sentences(text)
#     #stoppath = "FoxStoplist.txt" #Fox stoplist contains "numbers", so it will not find "natural numbers" like in Table 1.1
#     stoppath = "ryan-stoplist.txt"  #SMART stoplist misses some of the lower-scoring keywords in Figure 1.5, which means that the top 1/3 cuts off one of the 4.0 score words in Table 1.1
#     stopwordpattern = build_stop_word_regex(stoppath)

#     # generate candidate keywords
#     phraseList = generate_candidate_keywords(sentenceList, stopwordpattern)

#     # calculate individual word scores
#     wordscores = calculate_word_scores(phraseList)

#     # generate candidate keyword scores
#     keywordcandidates = generate_candidate_keyword_scores(phraseList, wordscores)
#     if debug: print keywordcandidates

#     sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)
#     if debug: print sortedKeywords

#     totalKeywords = len(sortedKeywords)
#     if debug: print totalKeywords
#     print sortedKeywords[0:(totalKeywords / 3)]

#     rake = Rake("./ryan-stoplist.txt")
#     keywords = rake.run(text)
#     print keywords





	# return StreamingHttpResponse(links)
		# article_imgs_desc =  get_article_stuff(html)
		# print article_imgs_desc
		# og_img = get_og_img(html)
		# og_description = get_og_description(html)
		# try:		
		# 	article_title = Document(html).short_title()	
		# except:
		# 	article_title = False
		
		# print article_title

		# try:				
		# 	html = Document(html).summary()
		# 	# print html
		# 	tags_to_strip =         ['html', 'body', 'body div', 'div', 'span', 'object', 'iframe', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'pre', 'abbr', 'address', 'cite', 'code', 'del', 'dfn', 'em', 'img', 'ins', 'kbd', 'q', 'samp', 'small', 'strong', 'sub', 'sup', 'var', 'b', 'i', 'dl', 'dt', 'dd', 'ol', 'ul', 'li', 'fieldset', 'form', 'label', 'legend', 'table', 'caption', 'tbody', 'tfoot', 'thead', 'tr', 'th', 'td', 'article', 'aside', 'figure', 'footer', 'header', 'menu', 'nav', 'section', 'time', 'mark', 'audio', 'video', 'details', 'summary', 'p']
		# 	# tags_to_strip_summary = ['html', 'body', 'body div', 'div', 'span', 'object', 'iframe', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'pre', 'abbr', 'address', 'cite', 'code', 'del', 'dfn', 'em', 'img', 'ins', 'kbd', 'q', 'samp', 'small', 'strong', 'sub', 'sup', 'var', 'b', 'i', 'dl', 'dt', 'dd', 'ol', 'ul', 'li', 'fieldset', 'form', 'label', 'legend', 'table', 'caption', 'tbody', 'tfoot', 'thead', 'tr', 'th', 'td', 'article', 'aside', 'figure', 'footer', 'header', 'menu', 'nav', 'section', 'time', 'mark', 'audio', 'video', 'details', 'summary']
		# 	clean_soup = _remove_attrs(clean_soup)
		# 	# print clean_soup
		# 	clean_soup = strip_tags(html, tags_to_strip)
		# 	print clean_soup
		# 	# keywords = rake.run(clean_soup)
		# 	print clean_soup
	# return StreamingHttpResponse(clean_soup)
			# print 'clean_soup'
			# print clean_soup
			# clean_soup_summary = strip_tags(html, tags_to_strip_summary)
			# clean_soup_summary = str(_remove_attrs(clean_soup_summary))
			# print 'clean_soup_summary'
			# print clean_soup_summary
			# print 'summary'
			# top_sentences = naivesum.summarize(clean_soup_summary, 4)
			# print 'top_sentences'
			# print top_sentences
		# except:
			# top_sentences = False
			# keywords = False

		# html_title = br.title()
		# # print 'title'
		# # print 'url:' + links[i]['url']
		# c ={
		# 	# 'tweet_id': links[i]['tweet_id'],
		# 	# 'url': links[i]['url'],
		# 	# 'ht': links[i]['ht'],
		# 	# 'datetime': links[i]['datetime'],
		# 	# 'score': links[i]['score'],
		# 	# 'tweet_text': links[i]['text'],
		# 	# 'og_img': og_img,
		# 	# 'og_description': og_description,
		# 	'page_title': html_title,
		# 	'article_title': article_title,
		# 	'article_text': keywords,
		# 	'article_imgs_desc': article_imgs_desc,
		# 	# 'article_summary': top_sentences,
		# }
		# # print c
		# content.append(c)
	# return StreamingHttpResponse(keywords)


# def get_keywords(tweets):
# 	tweet_text = ""
# 	for i in range(len(tweets)):
# 		for j in range(len(tweets[i])):
# 			text = tweets[i][j]['text']
# 			tweet_text += " " + text
# 		print i
# 	return tweet_text


			# kwords = tb.tags
			# print kwords
			# k = get_keywords(html)
			# keywords.append(k)
			# html = 


						# tbresults = tb.sentences
			# sentences = rake.run_p(text)
			# sentences = tb.sentences


						# links[i]['sentences'] = sentences
			# links[i].append(tbresults)


				#return HttpResponse(json.dumps(content), content_type="application/json")

    # readable_article = Document(html).summary()
    # readable_title = Document(html).short_title()
# def article_main(request):
# 	ecForm = EmailCaptureForm()
# 	featured = ArticleCategoryModel.objects.all().order_by('category_name')
# 	for f in featured:
# 		f.page = ArticlePageModel.objects.filter(category=f).filter(is_live=True).order_by('-created_datetime').exclude(publish_time__gt=datetime.now())[:5]
# 	context = {'featured': featured, 'ecForm': ecForm}
# 	return render(request, 'articles_directory.html', context)


			# text = clean_twitter_text(text)
			# text = striphtml(text)

						# paragraphs = get_only_p_tags(html)

			# ungzipResponse(response, br)
