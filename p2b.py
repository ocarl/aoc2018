from difflib import SequenceMatcher


def compare_words(word1, word2):
    return SequenceMatcher(None, word1, word2).get_matching_blocks()


def find_match(inlist: list):
    for i, word1 in enumerate(inlist):
        for word2 in inlist[i+1:]:
            diff = compare_words(word1, word2)
            if len(diff) == 3:
                if diff[0][2]+diff[1][2] == len(word2)-1:
                    return word2[:diff[0][2]]+word2[diff[0][2]+1:]
    return 'NOOOOOOOOO'

print(find_match(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']))
assert find_match(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']) == 'fgij'


with open('2.txt') as f:
    a = f.readlines()
    print(find_match(a))

