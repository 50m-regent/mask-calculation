import random as rand

class MaskCaluculation:
    def __init__(self, words, match):
        self.words = words
        self.match = match

    def result(self):
        nums = []

        for word in nums

    def print(self):
        for word in words:
            if word != words[0]:
                print(' * ', end='')
            print(word, end='')
        print('=' + self.result())

def get_input():
    words = list(map(int, input().split()))

    return words

def match_digits():
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    match  = {}
    for c in alphabets:
        match[c] = rand.randint(0, 9)

    return match

if __name__ == '__main__':
    words = get_input()
    match = match_digits()

    mask_calculation = MaskCaluculation(word, match)
    mask_calculation.print()
