from  transliterate import CYRILLIC_TO_LATIN
from uzWords import words, latin_words
from difflib import get_close_matches

def has_cyrillic(word):
    cyrillic_letters = [keys for keys in CYRILLIC_TO_LATIN]
    for c in word:
        if c in cyrillic_letters:
            return True
    return False


def checkWord(word ,words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False # bunday so'z mavjud emas

    if word in matches:
        available = True # mavjud
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))

    return {'available': available, 'matches': matches}

def checkLatin(word, words=latin_words):
    word = word.lower()
    matches = set(get_close_matches(word, latin_words))
    available = False  # bunday so'z mavjud emas

    if word in matches:
        available = True  # mavjud
        matches = word
    elif 'h' in word:
        word = word.replace('h', 'x')
        matches.update(get_close_matches(word, latin_words))
    elif 'x' in word:
        word = word.replace('x', 'h')
        matches.update(get_close_matches(word, latin_words))

    return {'available': available, 'matches': matches}

if __name__ == '__main__':
    print(checkWord("ҳато"))
    print(checkWord("тариҳ"))
    print(checkWord("хато"))
    print(checkWord("олма"))
    print(checkWord("ҳат"))
    print(checkWord("ҳайт"))