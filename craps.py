from random import choice

dice1=choice(range(1,7))
dice2=choice(range(1,7))

if (dice1+dice2) in [2,3,12]:
    print(f'The sum of dice is {dice1} + {dice2} = {dice1+dice2} \nYou lose')
elif (dice1+dice2) in [7,11]:
    print(f'The sum of dice is {dice1} + {dice2} = {dice1+dice2} \nYou won')
else:
    goal=dice1+dice2
    print(f'The sum of dice is {dice1} + {dice2} = {goal}')
    print(f'Now your goal number is {goal}')
    while True:
      dice1=choice(range(1,7))
      dice2=choice(range(1,7))
      if (dice1+dice2)==goal:
          print(f'The sum of dice is {dice1} + {dice2} = {dice1+dice2} \nYou won')
          break
      elif (dice1+dice2)==7:
          print(f'The sum of dice is {dice1} + {dice2} = 7 \nYou lose')
          break
      else:
          print(f'The sum of dice is {dice1} + {dice2} = {dice1+dice2}')









        
    