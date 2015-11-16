import random
HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

  +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
	   
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
 

def getrandomword(wordlist):
	secretword = random.choice(open("secretwords.txt").readlines())

def showdisplay(HANGMANPICS, missedletters, correctletters, secretword):
	print(HANGMANPICS[len(missedletters)])
	print()
	
	print("Missed Letters:", end=" ")
	for letter in missedletters:
		print(letter, end=" ")
	print()
		
	blanks = "_" * (len(secretword) - 1)
	
	for i in range(len(secretword)):
		if secretword[i] in correctletters:
			blanks = blanks[:i] + secretword[i] + blanks[i + 1:]
	
	for letter in blanks:
		print(letter, end=" ")
	print()
	
def getguess(alreadyguessed):
	while True:
		print("Guess a letter.")
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print("Please enter only one letter.")
		elif guess in alreadyguessed:
			print("You've already guess that letter.  Guess again.")
		elif guess not in "abcdefghijklmnopqrstuvwxyz":
			print("Please choose a letter in the Enlgish alphabet.")
		else:
			return guess
		
def playagain():
	print("Do you want to play again? (Yes or No?)")
	return input().lower().startswith("y")

print("HANGMAN")
missedletters = ""
correctletters = ""
secretword = random.choice(open("secretwords.txt").readlines())
gameisdone = False

while True:
		showdisplay(HANGMANPICS, missedletters, correctletters, secretword)
		
		guess = getguess(missedletters + correctletters)
		
		if guess in secretword:
			correctletters = correctletters + guess
		
			foundallcorrectletters = True
			for i in range(len(secretword)-1):
				if secretword[i] not in correctletters:
					foundallcorrectletters = False
					break
			if foundallcorrectletters:
				print('Yes! The secret word is "' + secretword + '" you have won!')
				gameisdone = True
		else:
			missedletters = missedletters + guess
	
			if len(missedletters) == len(HANGMANPICS) - 1:
				showdisplay(HANGMANPICS, missedletters, correctletters, secretword)
				print('You have run out of guesses!\nAfter ' + str(len(missedletters)) + ' missed guesses and ' + str(len(correctletters)) + ' correct guesses, the word was "' + secretword + '"')
				gameisdone = True
		
		if gameisdone:
			if playagain():
				missedletters = ""
				correctletters = ""
				gameisdone = False
				secretword = random.choice(open("secretwords.txt").readlines())
			else:
				break
				
			