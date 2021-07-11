import random
import string
WORDLIST_FILENAME = 'home/mahir/Desktop/progrmming/PYTHON/MIT CODING/ps2/words.txt'


###########################FUNCTION-load words#################################
# Problem Set 2, hangman.py
###########################FUNCTION-LOADING WORDS#################################
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('words.txt')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()
secret_word=(choose_word(wordlist))
##########################FUNCTION-1################################# 
def is_word_guessed(secret_word, letters_guessed):
          '''
        secret_word: string, the word the user is guessing; assumes all letters are
          lowercase
        letters_guessed: list (of letters), which letters have been guessed so far;
          assumes that all letters are lowercase
        returns: boolean, True if all the letters of secret_word are in letters_guessed;
          False otherwise
          ''' 
          result=all(elem in letters_guessed for elem in secret_word)

          if result:
              
              return('YOU SAVED YOURSELF')
          else:
              return('THE ARROW IS COMING, BETTER HURRY UP.')
          return result
#print(is_word_guessed('ab',['a']))

###########################FUNCTION-2################################# 
def get_guessed_word (secret_word,letters_guessed):
    secret_word=list(secret_word )
    secret_word_copy=secret_word[:]
    for i in range(len(secret_word_copy)):

            
        if secret_word_copy[i] not in letters_guessed:
            secret_word.remove(secret_word[i])
            secret_word.insert(i,'_ ')
    secret_word_2='' .join(secret_word)
    return(secret_word_2)
    
###########################FUNCTION-3################################# 
def get_available_letters(letters_guessed):
    letters_guessed=list(letters_guessed)
    result=string.ascii_lowercase
    result=list(result)
    result_copy=result[:]
    for i in result_copy:
        if i  in letters_guessed:
            result.remove(i)
            
    return(''.join(result))

##############################################HINT FUNCTION-1##################################
def match_with_gaps (my_word,other_word):
    list(my_word)
    p=0
    l1=[]
    my_word=my_word.replace(' ','')
    if len(my_word)==len(other_word):
        
        for x in my_word:
            if x !=('_'):
                if x==other_word[my_word.find(x,p)]:
                    l1.append('TRUE')

                    if my_word.count(x)>0:
                        if my_word.count(x)!=other_word.count(x):
                            l1.append('FALSE')
                        
                else:
                    l1.append('FALSE')
            p+=1




    else:
        l1.append('FALSE')
    length=len(l1)
    if length==l1.count('TRUE'):
        return('TRUE')
    else:
        return("FALSE")



letters_guessed=[]
#######HINT FUNCTION-2###################
def show_possible_matches(my_word):

    l5=[]
    l7=[]
#we created two empty lists to use after
    for r in wordlist:

        
        if match_with_gaps(my_word,r)==('TRUE'):
#refers to a function we used before, if you did not check it out yet, you should.
                    l5.append(r)
#we added those words that seem to be a possible match with our secret word.
    l6=l5[:]
#we created a copy in order to iterate over the list.
    for e in l6:
#at this point, I realized that there was another problem with our code.
#our code puts the words which include the letters that are not in the secret word 
#Into the category of possible match if they match_with_gaps()=='TRUE'
#This was a property I did not add to my last function so I decided to add this to this one.

            for i in letters_guessed:
                if i!= "HINT":
                    if i != "QUIT":
                        if i  not in secret_word:
                            if i in e:
                                l7.append(e)
    for x in l7:
        if x in l5:
            l5.remove(x)
                                

        
    if l5==[]:
        return('NO MATCHES', l5)
    else:
        return('POSSIBLE MATCHES:', l5,)
#########################################PROGRAM PART###########################    
def hangman_with_hints(secret_word)   :
    warnings=3
    
    a=input(str('COMPUTER:Do you want to start the game? YES or NO:'))
    wovels=['a','e','i','o','u',]
    hangman_chance_protected=['hint','quit']


    
    if a==str('YES') :
            mode=input(str('COMPUTER:CHOOSE YOUR GAME MODE:\nA-EASY\nB-MEDIUM\nC-HARD\nWRITE YOUR ANSWER, AS A,B OR C:'))
            if mode==('A'):
             chances=10
            if mode==('B'):
             chances=8
            if mode==('C'):
             chances=6
            else:
                 print('YOU SHOULD ANSWER AS INSTRUCTED, RUN THE CODE AGAIN')


#            print('COMPUTER:HANGMAN IS STARTED, RULES:\n1)YOU HAVE',chances,' GUESSES\n2)YOU HAVE 3 WARNINGS, YOU CAN ONLY TYPE LETTERS OR ELSE, YOU WILL BE BANNED\n3)YOU CAN LEARN THE POSSIBLE MATCHES FOR YOUR WORD BY TYPING HINT.\N4)YOU CAN QUIT BY TYPING QUIT.')
    
            L0=[]
            while is_word_guessed(secret_word,letters_guessed)=='THE ARROW IS COMING, BETTER HURRY UP.':
#                for r in letters_guessed:
#                    if r in string.ascii_letters:
#                            
#                    
#                score=chances*
                print('---------------ROUND START-------------------')
                secret_word=secret_word
                ##################  GRAPHICS ###########
                secret_word_2=get_guessed_word(secret_word,letters_guessed)
                if chances==10:
                    print(" [-_-]          <<-----\n   |                  \n  /| /            \n   |              \n  /^/             \n")
                    print('COMPUTER:I am thinking of a',len(secret_word),'letter word,do you want to guess?')
                if chances==9:
                    print(" [-_-]         <<------\n   |                  \n  /| /            \n   |              \n  /^/             \n")
                if chances==8:
                    print(" [-_-]       <<------< \n   |                  \n  /| /            \n   |              \n  /^/             \n")
                    print('COMPUTER:I am thinking of a',len(secret_word),'letter word,do you want to guess?')
                if chances==7:
                    print(" [-_-]      <<------<  \n   |                  \n  /| /            \n   |              \n  /^/             \n")
                if chances==6:
                    print('COMPUTER:I am thinking of a',len(secret_word),'letter word,do you want to guess?')
                    print(" [-_-]     <<------<   \n   |                  \n  /| /            \n   |              \n  /^/            \n")
                if chances==5:
                    print(" [-_-]    <<------<    \n   |                  \n  /| /            \n   |              \n  /^/             \n")      
                if chances==4:
                    print(" [-_-]   <<------<     \n   |                  \n  /| /            \n   |              \n  /^/             \n")      
                if chances==3:
                    print(" [-_-]  <<------<      \n   |                  \n  /| /            \n   |              \n  /^/             \n")
                if chances==2:
                    print(" [-_-] <<------<       \n   |                  \n  /| /            \n   |              \n  /^/             \n") 
                if chances==1:
                    print(" [-_-]<<------<        \n   |                  \n  /| /            \n   |               \n  /^/              \n")
                if chances==0 or chances<0:
                    print(" [*_*<<------<         \n   |                  \n  /| /            \n   |               \n  /^/              \n")
                    print('secret word:',secret_word)
                    print('COMPUTER:YOU REACHED THE END, WELCOME DEATH')

                    break    
                if warnings<1:
                    print('COMPUTER:CHEATER, YOUR GUESS NUMBER IS DECREASED BY ONE')
                    chances-=1
                    warnings=3           
                
     
                
                ########TAKES AN INPUT, LETTER  ##########    
                a=input(str('Which letter do you want to guess:'))
                    
    
    
                ###### WARNINGS AND CHANCES #######
                a=str.lower(a)
                letters_guessed.append(a)
                number=letters_guessed.count(letters_guessed[len(letters_guessed)-1])
                if a == ('quit'):
                    print('YOU QUITED')
                    break
                if a == ('hint'):
                        print(show_possible_matches(secret_word_2))
                        print(secret_word_2)
                if a not in hangman_chance_protected:
                    if number>1:
                        chances=chances
                        print('ERROR:DO NOT TYPE THE SAME LETTER')
                    else:
                        
                        if a not in secret_word:
                            if a in string.ascii_letters:
                                if a in wovels:
                                    chances=chances-2
                                else:
                                    chances=chances-1
                            else:
                                warnings=warnings-1
                                print('ERROR1: OOOPS, THIS IS NOT AN ALPHABETICAL CHARECTER.')
                        else:
                            chances=chances
                            
                    
                              
                print('            YOUR SCORE TABLE')

                print('guesses left:,', chances)
                print('warnings left:',warnings)
                print('letters available:',get_available_letters(letters_guessed))
                print('letters guessed:',letters_guessed)
                print('YOUR WORD:',get_guessed_word(secret_word,letters_guessed))
                print(is_word_guessed(secret_word,letters_guessed))
                if is_word_guessed(secret_word,letters_guessed)==str('YOU SAVED YOURSELF'):
                    print('COMPUTER:I LOST, HUMAN MIND IS THE BEST ')
           
    elif a==str('NO'):
        print('COMPUTER:OK. IT WAS NICE TO SEE YOU ANYWAY.')
    else:
        print('ERROR:YOU SHOULD ENTER YES OR NO, WITH CAPITALS.')
        
hangman_with_hints(secret_word)

























