from random import randint

#The words which one of them will be chosen
words_list=['book','ball','foot','take','went','base','cart','boot','head','hand']
#The randomly chosen word
x=words_list[randint(0,len(words_list)-1)]
#The variable to count the correct guesses
correct_guesses=0
#The variable to count the lmiit for words used
words_used=0
#the variable to see which letter was used before
used_letters=[]
#To show how many letters the word has
print(f"The word has {len(x)} letters.")
#Only stop the game at guessing the word or reaching the words limit
while correct_guesses<len(x) and words_used<6:
  word=input("Enter a word: ")
  #go through all the words in the inputted word
  for y in word:
    if y not in used_letters:
      z=0
      #go trhough all the letters in the chosen word
      for letter in x:
    
        if y==letter:
          print(f"{y}'s position is {z+1}.")
          correct_guesses=correct_guesses+1
        z=z+1
      if y not in x:
          print(f"{y} is wrong.")
      used_letters.append(y)
    else:
      print(f"You have used {y} before.")
  words_used+=1
  if correct_guesses<4:
    print(f"You have {6-words_used} guesses left.")
  if correct_guesses==4:
    print("You win")
    print(f"The word is {x}")
  elif words_used==6:
    print("you lose")
    print(f"The word is {x}")

