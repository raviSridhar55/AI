# import itertools
#
#
# def get_value(word, substitution):
#     s = 0
#     factor = 1
#     for letter in reversed(word):
#         s += factor * substitution[letter]
#         factor *= 10
#     return s
#
#
# def solve2(equation):
#     # split equation in left and right
#     left, right = equation.lower().replace(' ', '').split('=')
#     # split words in left part
#     left = left.split('+')
#     # create list of used letters
#     letters = set(right)
#     for word in left:
#         for letter in word:
#             letters.add(letter)
#     letters = list(letters)
#
#     digits = range(10)
#     for perm in itertools.permutations(digits, len(letters)):
#         sol = dict(zip(letters, perm))
#
#         if sum(get_value(word, sol) for word in left) == get_value(right, sol):
#             print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))
#
# if __name__ == '__main__':
#     solve2('SEND + MORE = MONEY')
import itertools
def solve2():
    letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol['s'] == 0 or sol['m'] == 0:
            continue
        send = 1000 * sol['s'] + 100 * sol['e'] + 10 * sol['n'] + sol['d']
        more = 1000 * sol['m'] + 100 * sol['o'] + 10 * sol['r'] + sol['e']
        money = 10000 * sol['m'] + 1000 * sol['o'] + 100 * sol['n'] + 10 * sol['e'] + sol['y']
        if send + more == money:
          print(" send"," more"," money")
          return send, more, money
print(solve2())