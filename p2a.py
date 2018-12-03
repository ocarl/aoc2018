from collections import defaultdict

def count_chars(word: str):
    word_count = defaultdict(lambda :0)
    for char in word:
        word_count[char] += 1
    return word_count

def check_sum(inlist: list):
    twos = 0
    threes = 0
    for word in inlist:
        counted = count_chars(word)
        if 2 in counted.values():
            twos += 1
        if 3 in counted.values():
            threes += 1
    return twos*threes


assert check_sum(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12


with open('2.txt') as f:
    a = f.readlines()
    print(check_sum(a))

