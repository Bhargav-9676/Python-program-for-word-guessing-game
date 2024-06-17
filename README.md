Python is a powerful multi-purpose programming language used by multiple giant companies. It has simple and easy-to-use syntax making it the perfect language for someone trying to learn computer programming for the first time. It is a high-level programming language, and its core design philosophy is all about code readability and syntax that allows programmers to express concepts in a few lines of code.

In this article, we will use the random module to make a word-guessing game. This game is for beginners learning to code in python and to give them a little brief about using strings, loops, and conditional(If, else) statements.

random module: Sometimes we want the computer to pick a random number in a given range, pick a random element from a list, pick a random card from a deck, flip a coin, etc. The random module provides access to functions that support these types of operations. One such operation is random.choice() method (returns a random item from a list, tuple, or string.) that we are going to use in order to select one random word from a list of words that we’ve created.


In this game, there is a list of words present, out of which our interpreter will choose 1 random word. The user first has to input their names and then, will be asked to guess any alphabet. If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. The user will be given 12 turns(which can be changed accordingly) to guess the complete word

Time Complexity: O(k)

Here k is the length of the word.

Auxiliary Space: O(n)

Here n is the size of the list.

Code Explanation:

The code starts by asking the user to enter their name.
The code then prints a message saying “Good Luck!”
and sets a variable called name to the inputted name.
Next, the code creates a list of words using the built-in function word().
This function takes in an input string and returns a list of strings.
In this case, the list will contain five strings: rainbow, computer, science, programming, and python.
The next part of the code is where the randomness happens.
The code will randomly choose one string from the list of words and store it in word variable.
Then it will print out that word along with a space at the end.
After printing out each word, the code checks to see if any user has entered an incorrect letter by comparing each character in guess with those in word .
If they don’t match up then guess is set to “Wrong” and turns is decreased by 1 .
If there are no more letters left in guess , then Guess You Lose is printed .
Otherwise turn s is increased by 1 and loop continues until either Guess You Win or Wrong is printed .
Finally , if turn s equals 0 , then you have won !
Otherwise Wrong will be
The code will randomly choose one word from a list of words.
The user is then asked to enter the characters for that word.
Once the user enters all of the characters, the code checks to see if those characters are in the word that was chosen.
If they are not, it prints out “Wrong” and decreases the number of turns left for the user by 1.
If all turns have been used, then the code will print “You Lose.”
Example 2: Word guessing game using python
In this game, the user needs to enter 5 letter word, if any alphabet is present in the magic word that word will be shown yellow and if the alphabet is present at the same position alphabet will turn green, and if the alphabet is not present in the word then alphabet will become black.
FOR MORE INFORMATION
https://www.geeksforgeeks.org/python-program-for-word-guessing-game/?ref=lbp


word document link 
https://1drv.ms/w/c/6d092c83b203e1e1/EWdI2V38WK1MlfxG-3111QkBc_wWpivHnOsTgdnGdQqPeQ?e=UFBmcG
