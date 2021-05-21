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