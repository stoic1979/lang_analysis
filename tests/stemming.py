#
# Stemming tests
# stem is rid in words like ride, riding, ridden etc.
#
# Stemmers remove morphological affixes from words, leaving only the word stem. 
#

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

some_words = ["pythoners", "python", "pythonic", "pythoned", "pythonly", "pythonated", "pythonology"]

plurals = ['caresses', 'flies', 'dies', 'mules', 'denied', 'died', 'agreed', 'owned', 'humbled', 'sized', 'meeting', 'stating', 'siezing', 'itemization', 'sensational', 'traditional', 'reference', 'colonizer', 'plotted']


def main():
    print ("----------[ STEMMING TESTS ]-------------")

    ps = PorterStemmer()

    # lets get stems of some word
    stems = [ps.stem(w) for w in some_words]
    print("Stems:", stems)

    # lets mame singles from plurals
    singles = [ps.stem(plural) for plural in plurals]
    print("Singles:", singles)


if __name__ == "__main__":
    main()
