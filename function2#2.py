 def highScoreMov():
     a = []
     for i in range(len(movies)):
         if movies[i]["imdb"] > 5.5:
             a.append(movies[i]["name"])
            
     print(a)
 highScoreMov()
