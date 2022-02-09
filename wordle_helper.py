import sys, re
from random import randint

# Higher index = more frequently used word
alphabet = "qjzxvkwyfbghmpduclsntoirae"


def score(word):
    # Lower scores are less frequent words.
    # Words don't benefit from repeating letters
    score = 0
    letters = []
    for c in word:
        if c not in letters:
            score += alphabet.index(c)
        letters.append(c)
    return (word, score)


def rank(words):
    # Rank a list of words by the popularity of the letters in them
    return sorted([score(word) for word in words], reverse=True, key=lambda x: x[1])


def word_matches(pattern, word):
    return bool(re.match(pattern, word))


def has_found_letters(letters_found, word):
    return len([l for l in letters_found if l in word]) == len(letters_found)


if __name__ == "__main__":
    wordlist = open(sys.argv[1], 'r').read().split("\n")
    excluded_letters = []
    found_letters = []
    solution = list(".....")
    result = "xxxxx"
    while result != "GGGGG":
        for i in range(len(solution)):
            if solution[i] not in alphabet and (len(excluded_letters) + len(found_letters) > 0):
                exclude_here = excluded_letters + [l[0] for l in found_letters if l[1] == i]
                solution[i] = "[^{}]".format("".join(exclude_here))
        solution_regex = "^" + ("".join(solution)) + "$"
        print("Current Solution:\t{}\n".format(solution_regex))
        print("Discovered Letters:\t{}\n".format(", ".join([f[0] for f in found_letters])))
        print("Excluded Letters:\t{}\n".format(", ".join(excluded_letters)))

        top_matching_words = rank([w for w in wordlist if
                                   word_matches(solution_regex, w)
                                   and has_found_letters([f[0] for f in found_letters], w)])[:10]
        print("Suggested Guesses:")
        for tmw in top_matching_words:
            print(tmw)
        guess = input("Input your Guess: ")
        result = input("What was the result?\n(x for letter not found,\nG for green\nY for yellow): ")
        for i in range(5):
            g = guess[i]
            r = result[i]
            if r == "G":
                solution[i] = g
            if r == "Y":
                found_letters.append((g, i))
            if r == "x":
                excluded_letters.append(g)
