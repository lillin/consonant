import re

file = open('zdf-win.txt', 'r')


def find_words(a, b, text, c=''):

    pattern = r"%(a)s[аэыуояеёюи%(c)s]{2}%(b)s\w*|%(a)s%(b)s[^йцкншщзхфвпрлджчсмтб]\w*|%(a)s[аэыуояеёюи]%(b)s\w*" % {
        'a': a,
        'b': b,
        'c': c
    }

    results = []

    for line in text:
        if re.findall(pattern, line):
            results.append(line.replace('\n', ''))

    return results


file.close()
