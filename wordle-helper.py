input sys, re
from random import randint

# Higher index = more frequently used word
alphabet = "qjzxvkwyfbghmpduclsntoirae"

score(word):
    ### Lower scores are less frequent words.
    ### Words don't benefit from repeating letters
    score = 0
    letters = []
    for c in word:
        if c not in letters:
            score += alphabet.index(c)
        letters.append(c)
    return (word, score)
    

rank(words):
    return [score(word) for word in words].sort(reverse=True, key=lambda x: x[1])[::-1]
    #Rank a list of words by the popularity of the letters in them
    

word_matches(pattern,word):
    return re.compile(pattern).match(word) is not None
    

has_found_letters(found_letters, word):
    return len([l in found_letters, l in word)]) == len(found_letters)


if __name__=="__main__":
    wordlist = open(sys.argv[1],'r').read().split("\n")
    excluded_letters = []
    found_letters = []
    solution = "....."
    while ("." in solution or "[" in solution):
        print("Current Solution:\t{}\n".format(solution))
        print("Discovered Letters:\t{}\n".format(",".join(found_letters)))
        print("Excluded Letters:\t{}\n".format(",".join(excluded_letters)))
        exc = "[^{}]".format("".join(excluded_letters))
        if len(excluded_letters)>0:
            filter = solution.replace(".",exc)
        else:
            filter = solution
        top_matching_words = rank_words([w for w in wordlist, word_matches(filter,w) and has_found_letters(found_letters,w)][:10])
        print("Suggested Guesses:")
        for tmw in top_matching_words:
            print(tmw)
        guess = input("Input your Guess: ")
        result = input("What was the result?:\n(x for letter not found,\nG for green\nY for yellow")
        for i in range(5):
            g = guess[i]
            r = result[i]
            if r == "G":
                solution[i] = g
            if r == "Y":
                found_letters.append(g)
            if r == "x":
                excluded_letters.append(g)
                