#
# tokenizer tests
#
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

some_text = "Hello world, what are you doing today ? The weather today is wonderful and I love sunny days. The sky is blue and birds are flying"


def main():
    print ("----------[ TOKENIZE TESTS ]-------------")
    print("Sentences:", sent_tokenize(some_text))
    print("Words:", word_tokenize(some_text))
    print("POS:", pos_tag(word_tokenize(some_text)))


if __name__ == "__main__":
    main()
