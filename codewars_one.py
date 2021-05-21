# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help
# with an application form that will tell prospective members which category they will be placed.
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club,
# handicaps range from -2 to +26; the better the player the lower the handicap.
# INPUT
# Input will consist of a list of lists containing two items each. Each list contains information for a single
# potential member. Information consists of an integer for the person's age and an integer for the person's handicap.
# Note for F#: The input will be of (int list list) which is a List<List>

# EXAMPLE INPUT
# [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
# OUTPUT
# Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective
# member is to be placed in the senior or open category.
#
# EXAMPLE OUTPUT
# ["Open", "Open", "Senior", "Open", "Open", "Senior"]


def open_or_senior(data):
    print(["Senior" if list[0] >= 55 and list[1] > 7 else "Open" for list in data])

open_or_senior([[53, 23],[64, 1],[51, 23],[72, 8],[66, 22],[10, 24]])


# This time no story, no theory. The examples below show you how to write function accum:
# EXAMPLES:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(word):
    result = ""
    for index, letter in enumerate(word, start=1):
        result += (letter*index).capitalize() + "-"
    print(result.strip("-"))

accum('abcd')
accum('RqaEzty')
accum('cwAt')

# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to
# an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with
# a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings
# representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter
# (direction) and you know it takes you one minute to traverse one city block, so create a function that will return
# true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, '
# of course, return you to your starting' point. Return false otherwise.
#
# Note: you will always receive a valid array containing a random assortment of direction letters
# ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
def is_valid_walk(walk):
    if len(walk) == 10:
        if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
            print(True)
        else:
            print(False)
    print(False)

is_valid_walk(['n', 's', 'e'])
is_valid_walk(['s', 's', 'e', 'e', 'w', 's'])


# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas except for the last two names,
# which should be separated by an ampersand.
# EXAMPLE:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# returns 'Bart'

# namelist([])
# returns ''

def namelist(names):
    words = ""
    if not names:
        print(words)
    else:
        raw = ""
        for item in names:
            for value in item.values():
                if len(names) == 1:
                    words += value
                else:
                    raw += value + " & "
                    words = raw.replace(' & ', ', ', len(names) - 2).strip(' & ')
    print(words)


namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}])
namelist([{'name': 'Bart'}])
namelist([])

# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    out = []
    for item in a:
        if not item in b:
            out.append(item)
    print(out)

array_diff([1, 2], [1])
array_diff([1, 2, 2, 2, 3], [2])
array_diff([1, 2, 2], [1])