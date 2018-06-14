import re


def find_words(a, b, text, c=''):

    pattern = r"%(a)s[аэыуояеёюи%(c)s]{2}%(b)s\w*|%(a)s%(b)s[^йцкншщзхфвпрлджчсмтб]\w*|%(a)s[аэыуояеёюи]%(b)s\w*" % {
        'a': a,
        'b': b,
        'c': c
    }
    text = [x.lower() for x in text]
    results = []

    for string in text:
        if re.findall(pattern, string):
            results.append(string)

    return results


test_voc_1 = ["вампир", "ампир", "выпь", "сыпь", "гроздь", "трость", "вплоть", "вплавь", "рясно", "впрок", "амбидекстер",
              'вопос', 'вопрос', "провоп", "вмапир"]

test_voc_2 = ["пила", "площадь", "плакать", "поле", "оплеуха", "ополчение", "половина", "прямо", "плитка", "плпо", "эпнл",
              "лпок", "опемле"]

print(find_words("п", "л", test_voc_2, "м"))
