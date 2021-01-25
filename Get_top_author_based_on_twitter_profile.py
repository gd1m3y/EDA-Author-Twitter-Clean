def clean_numbers(x):
  new_num = ""
  # print(type(x))
  if type(x) != type(1.0):
    for i in x:
      if i.isnumeric():
        new_num+=i
    return int(new_num)
  else:
    return None


def normal_eda(frame,query = 'followers'):
  """
  returns the top 5 authors depending upon the query 
  followers,no_of_posts,likes

  """

  if query == 'followers':
    frame.followers = frame.followers.apply(clean_numbers)
    sorted_frame = frame.sort_values('followers',ascending=False)
  elif query == 'no_of_posts':
    frame.no_of_posts = frame.no_of_posts.apply(clean_numbers)
    sorted_frame = frame.sort_values('no_of_posts',ascending=False)
  else:
    frame.likes = frame.likes.apply(clean_numbers)
    sorted_frame = frame.sort_values('likes',ascending=False)
  try:
    sorted_frame = sorted_frame.drop("Unnamed: 0",axis =1)
  except:
    pass
  return sorted_frame.head()
