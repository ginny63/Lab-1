def highScoreMov():
     num = int(input())
     if movies[num]["imdb"] > 5.5:
         return True
     else:
         return False

 res = highScoreMov()
 print(res)