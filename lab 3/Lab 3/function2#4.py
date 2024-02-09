 def tuble():
     imdb = 0
     for i in range(len(movies)):
         imdb += movies[i]["imdb"]
     avg = imdb / len(movies)
     print(avg)

 tuble()