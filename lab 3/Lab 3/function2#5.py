 def cate():
     a = 0
     x = input()
     for i in range(len(movies)):
         if movies[i]["category"] == x:
             a += movies[i]["imdb"]
     print(a)
 cate()