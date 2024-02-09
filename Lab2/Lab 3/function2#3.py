def categ():
     a = []
     x = input()
     for i in range(len(movies)):
         if movies[i]["category"] == x:
             a.append(movies[i]["name"])
     print(a)
 categ()