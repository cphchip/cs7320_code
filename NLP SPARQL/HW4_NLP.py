import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords


test_sent = "The news says Ralph lives in Dallas in a house."

def create_triples(sentence):

           
   tagged_sent = pos_tag(word_tokenize(sentence))
   tree = nltk.ne_chunk(tagged_sent)

   # Number_items in the tree = number words in the sentence
   number_items = len(sentence.split())
   
   # Each tree item is available using an index 0..number_items
   idx_list = []
   phrase = ""
   for idx in range(number_items):
      if (type(tree[idx]) == nltk.Tree 
         and tree[idx].label() == 'PERSON'
      ):
         idx_list.append(idx)

      # Find second tree type - end of string index
      # This may need to be changed to not just find nltk.tree types
      elif (type(tree[idx]) == nltk.Tree and idx_list):
         idx_list.append(idx)

   if not idx_list or len(idx_list) < 2:
      return ''

   entities, relationships = [], []
   
   for idx in range(idx_list[0], idx_list[1] + 1):

      if type(tree[idx]) == nltk.Tree:
         phrase += tree[idx][0][0] + " "
         entities.append(tree[idx][0][0])
      else:
          phrase += tree[idx][0] + " "
          relationships.append(tree[idx][0])
    
   foaf_dict = {'lives in': 'foaf:based_near',
               'works at': 'schema:worksFor',
               'is employed at': 'schema:worksFor',
               'knows': 'foaf:knows',
               'works with': 'foaf:knows',
               'has friend': 'foaf:knows',
               'hangs out with': 'foaf:knows',
               'likes': 'foaf:knows',
               'loves': 'foaf:knows',
               'talks to': 'foaf:knows',
               'is employed at': 'schema:worksFor'}
   
   relationship = ''
   word_tokens = word_tokenize(phrase)
   for x in range(1, len(word_tokens) - 1):
       relationship += word_tokens[x] + ' '
       
   ''' This part may not be needed for now
   word_tokens = word_tokenize(phrase)
   stop_words = set(stopwords.words('english'))

   filtered_phrase = [word for word in word_tokens 
                      if word not in stop_words]
   '''
   
   filtered_phrase = [word_tokens[0], 
                      relationship.strip(), 
                      word_tokens[len(word_tokens) - 1]]
                     
   triple = ''
   for word in filtered_phrase:
      if word in foaf_dict:
         word = foaf_dict[word]
      # This is a cludge but it works
      elif type(nltk.ne_chunk(pos_tag([word]))) == nltk.Tree:
          word = ':' + word

      triple += word + " "

   print(triple)

   # Change this to write to file

   return

with open('hw4.facts.txt') as facts:
      for line in facts:
         create_triples(line)


