"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    print('Hollo. Welcome to play guessing game')
    print('If you geuss less than 3 times. You\'ll get high point!')
    num_min, num_max = 1, 10
    answer = random.randrange(num_min,num_max+1)

    total = 0
    while True:
      try:
        guess = int(input(f'Guess the number. It\'s between {num_min} and {num_max}'))
      except ValueError:
        print('That is not a valid value. Please try again.')
        raise
      else:
        total += 1
        if guess < num_min or guess > num_max:
          print('Out of the range. Please try again.')
        elif guess == answer:
          print(f'Bingo! You totally tried {total} times.')
          break
        elif guess > answer:
          num_max = guess
          print('It\'s lower.')
        elif guess < answer:
          num_min = guess
          print('It\'s higher.')
      finally:
        print('finally')

      print('where am I')
      
    
    while True:
      try:
        again = input('Do you want to play again? YES? or NO?')
      except:
        print('That is not a valid value. Please try again.')
      else:
        if again.lower() == 'yes':
          print('OK Try a new noe.')
          start_game()
        elif again.lower() == 'no':
          print('Bye Have a nice day.')
          break
        else:
          print('That is not a valid value. Please try again.')
        
        
# Kick off the program by calling the start_game function.
start_game()
