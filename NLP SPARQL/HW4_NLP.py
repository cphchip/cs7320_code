import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords


def create_triples(sentence):
           
   tagged_sent = pos_tag(word_tokenize(sentence))
   tree = nltk.ne_chunk(tagged_sent)

   # Number_items in the tree = number words in the sentence
   number_items = len(sentence.split())
   
   idx_list = []
   for idx in range(number_items):
      # Find index of first entity that's a person
      if (type(tree[idx]) == nltk.Tree 
         and tree[idx].label() == 'PERSON'
      ):
         idx_list.append(idx)

      # Find second tree type - end of string index
      elif (type(tree[idx]) == nltk.Tree and idx_list):
         idx_list.append(idx)

   # Remove unwanted phrases by returning empty line
   if not idx_list or len(idx_list) < 2:
      return ''

   entities = []
   # Use identified indices to capture the phrase
   phrase = ''
   relationship = ''
   for idx in range(idx_list[0], idx_list[1] + 1):

      if type(tree[idx]) == nltk.Tree:
         phrase += tree[idx][0][0] + " "
         entities.append(tree[idx][0][0])
      else:
         phrase += tree[idx][0] + ' '
         relationship += tree[idx][0] + ' '
    
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

   # Replace the relationship with foaf definition
   relationship = relationship.strip()
   if relationship in foaf_dict:
      relationship = foaf_dict[relationship]
          
   triple = ''
   triple = (':' 
             + entities[0] 
             + ' '  
             + relationship 
             + ' :' 
             + entities[1])
   
   return triple

def main():
   triple_list = []
   # Read sentences from file
   with open('hw4.facts.txt') as facts:
         for line in facts:
            triple_list.append(create_triples(line))

   # Write completd triples to n3 file if they aren't blank
   with open('test.n3', 'w') as n3:
      for triple in triple_list:
         if triple != '':
            n3.write(triple + '\n')
         else:
            next

main()
