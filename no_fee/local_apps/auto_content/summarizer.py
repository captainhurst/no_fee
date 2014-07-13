import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist 
from nltk.corpus import stopwords


class NaiveSummarizer:


	def summarize(self, input, num_sentences ):
		punt_list=['.',',','!','?']
		summ_sentences = []
		sentences = sent_tokenize(input)
		lowercase_sentences =[sentence.lower()
			for sentence in sentences]
		lowercase_sentences = list(set(lowercase_sentences))
		#print lowercase_sentences

		s=list(input)
		ts=''.join([ o for o in s if not o in  punt_list ]).split()
		lowercase_words=[word.lower() for word in ts]
		words = [word for word in lowercase_words if word not in stopwords.words()]
		word_frequencies = FreqDist(words)
		most_frequent_words = [pair[0] for pair in word_frequencies.items()[:100]]
		for word in most_frequent_words:
			for i in range(0, len(lowercase_sentences)):
				if len(summ_sentences) < num_sentences:
					if (lowercase_sentences[i] not in summ_sentences and word in lowercase_sentences[i]):
						summ_sentences.append(sentences[i])
						break
		words_sentences = []
		words_sentences.append(most_frequent_words)
		# reorder the selected sentences
		print "summarizer"
		summ_sentences.sort( lambda s1, s2: input.find(s1) - input.find(s2) )
		summ_sentences = list(set(summ_sentences))
		words_sentences.append(summ_sentences)
		return words_sentences


def go_terms(text):
	# Used when tokenizing words
	sentence_re = r'''(?x)      # set flag to allow verbose regexps
	      ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
	    | \w+(-\w+)*            # words with optional internal hyphens
	    | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
	    | \.\.\.                # ellipsis
	    | [][.,;"'?():-_`]      # these are separate tokens
	''' 
	lemmatizer = nltk.WordNetLemmatizer()
	stemmer = nltk.stem.porter.PorterStemmer()
	 
	#Taken from Su Nam Kim Paper...
	grammar = r"""
	    NBAR:
	        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
	        
	    NP:
	        {<NBAR>}
	        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
	"""
	chunker = nltk.RegexpParser(grammar)
	 
	toks = nltk.regexp_tokenize(text, sentence_re)
	postoks = nltk.tag.pos_tag(toks)
	 
	# print postoks
	 
	tree = chunker.parse(postoks)

	print tree

	from nltk.corpus import stopwords
	stopwords = stopwords.words('english')
	 
	 
	def leaves(tree):
	    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
	    for subtree in tree.subtrees(filter = lambda t: t.node=='NP'):
	        yield subtree.leaves()
	 
	def normalise(word):
	    """Normalises words to lowercase and stems and lemmatizes it."""
	    word = word.lower()
	    word = stemmer.stem_word(word)
	    word = lemmatizer.lemmatize(word)
	    return word
	 
	def acceptable_word(word):
	    """Checks conditions for acceptable word: length, stopword."""
	    accepted = bool(2 <= len(word) <= 40
	        and word.lower() not in stopwords)
	    return accepted
	 
	 
	def get_terms(tree):
		keyword = []
		for leaf in leaves(tree):
			term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
			print term
			keyword.append(term)
		return keyword
  
# for term in terms:
#     for word in term:
#         print word,
#     print