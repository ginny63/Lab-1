def cant():
     print("Hello! What is your name?")
     a = input()
     print(f"""Well, {a}, I am thinking of a number between 1 and 20.
 Take a guess.""")
    
     rand = random.randint(1, 20)
    
     for i in range(20):
         num = int(input())
         if num == rand:
             print(f"Good job, KBTU! You guessed my number in {i+1} guesses!")
             break
        
         elif num < rand:
             print("""Your guess is too low.
 Take a guess""")
            
         elif num > rand:
             print("""Your guess is too high.
 Take a guess""")
            
 guess()
            