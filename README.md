# Wordle Helper
A Python script for helping you make educated Wordle guesses


## How to Use

Download the code using git or the download link. Then `cd` into the directory with the script file in the terminal of your choice and run `wordle-helper.py`, with the provided `5letterwords` file as the only argument. You could provide your own if you want.

```
$ cd wordle-helper
$ python3 wordle-helper.py 5letterwords
```

You will see this output:
```
Current Solution:       .....

Discovered Letters:

Excluded Letters:

Suggested Guesses:
('irate', 114)
('orate', 113)
('arise', 112)
('raise', 112)
('arose', 111)
('aster', 110)
('rates', 110)
('ratio', 110)
('stare', 110)
('tares', 110)
Input your Guess:
```

Input a guess in the Wordle game and record it at the prompt. You'll see a response like this.
```
Input your Guess: irate
What was the result?
(x for letter not found,
G for green
Y for yellow):
```

Look at your Wordle board. What colors did your letters turn when you posted your guess? At this prompt you will type five characters, in the order of your letters in your last guess in the Wordle game. If you guessed I R A T E, and the I was gray, the R was green, the A was yellow, the T was gray, and the E was yellow, you would type xGYxY.

The script will interpret your response and store the result. It will know the letters I and T are to be excluded, while a and e might be in there somewhere, and R is definitely in the second position. You will see this print out:

```
What was the result?
(x for letter not found,
G for green
Y for yellow): xGYxY
Current Solution:       .r...

Discovered Letters:     a,e

Excluded Letters:       i,t

Suggested Guesses:
('arose', 111)
('crane', 107)
('arced', 102)
('crape', 101)
('cream', 100)
('drape', 99)
('armed', 98)
('dream', 98)
('grace', 98)
('argue', 97)
Input your Guess:
```

When you finally solve the puzzle, the script ends.
