# Maisey Waller.
# 25/01/2025.

# Prints the name of my music quiz.
print('Maiseys music quiz.')
print('###################')

# Store the answers in Variables.
strA1 = str('Kurt Cobain')
strA2 = str('The Cranberries')
strA3 = str('Black')

# Ask question 1 and take the users input.
strQ1 = str(input('Who is the lead singer of Nirvana: '))
# Compare Q1 with A1 using case insensitive matching.
if (strQ1.casefold() == strA1.casefold()):
    # The answer was correct.
    print('Correct!')
else:
    # The answer was incorrect show the correct answer.
    print('Incorrect, the correct answer is', strA1)

# Ask question 2 and take the users input.
strQ2 = str(input('Who sang the song Linger: '))
# Compare Q2 with A2 using case insensitive matching.
if (strQ2.casefold() == strA2.casefold()):
     # The answer was correct.
    print('Correct!')
else:
     # The answer was incorrect show the correct answer.
    print('Incorrect, the correct answer is', strA2)

# Ask question 3 and take the users input.
strQ3 = str(input('What colour parade is a title of a My Chemical Romance album: '))
# Compare Q3 with A3 using case insensitive matching.
if (strQ3.casefold() == strA3.casefold()):
     # The answer was correct.
    print('Correct!')
else:
     # The answer was incorrect show the correct answer.
    print('Incorrect, the correct answer is', strA3)