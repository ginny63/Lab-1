 def solve(numheads, numlegs):
     num_chickens = 0
     num_rabbits = 0
     for i in range(1, numheads + 1):
         num_chickens = i
         num_rabbits = numheads - i
         if(num_chickens * 2 + num_rabbits * 4 == numlegs):
             break
     print(f"Number of rabbits = {num_rabbits} and Number of chicks = {num_chickens}")