def get_keywords(doc,n):
  total_words = doc.split()
  total_word_length = len(total_words)
  
  total_sentences = tokenize.sent_tokenize(doc)
  total_sent_len = len(total_sentences)

  tf_score = {}
  for each_word in total_words:
      each_word = each_word.replace('.','')
      if each_word not in stop_words:
          if each_word in tf_score:
              tf_score[each_word] += 1
          else:
              tf_score[each_word] = 1

  # Dividing by total_word_length for each dictionary element
  tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
  idf_score = {}
  for each_word in total_words:
      each_word = each_word.replace('.','')
      if each_word not in stop_words:
          if each_word in idf_score:
              idf_score[each_word] = check_sent(each_word, total_sentences)
          else:
              idf_score[each_word] = 1

  # Performing a log and divide
  idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())
  tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}

  return get_top_n(tf_idf_score,n)

  
def check_sent(word, sentences): 
  final = [all([w in x for w in word]) for x in sentences] 
  sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
  return int(len(sent_len))

def get_top_n(dict_elem, n):
    result = sorted(dict_elem.items(), key = itemgetter(1), reverse = True)
    return_dict = {}
    for x,y in result:
      if len(return_dict) >=n:
        return return_dict
      if len(x) >3:
        return_dict[x] = y
      
    return return_dict




def get_top_author_keywords(author_frame,n):
  """
  authorframe: frame representing the author
  n:no of keywords
  takes in the author frame and returns top n keywords used by author
  """
  print("Top {} keywords used by {} in their recent tweets".format(n,author_frame.author_name.iloc[0]))
  doc = ""
  for i in range(len(author_frame.tweet.iloc[0])):
    doc+=author_frame.tweet.iloc[0][str(i)]['text']
  print(get_keywords(doc,n))
