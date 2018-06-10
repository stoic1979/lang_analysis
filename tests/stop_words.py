#
# stop words filteration tests
# stop words are the words that we dont need in the analysis of text, eg. a, the etc.
#
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

some_text = "Hello world, what are you doing today ? The weather today is wonderful and I love sunny days. The sky is blue and birds are flying"

# define the set of stop words in English language
eng_stop_words = set(stopwords.words("english"))


def main():
    print ("----------[ STOP WORDS TESTS ]-------------")

    word_list = word_tokenize(some_text)

    # removing stop words from the word list
    filtered_word_list = [ w for w in word_list if w not in eng_stop_words]
    
    # getting stop words
    stop_word_list = [ w for w in word_list if w in eng_stop_words]

    print("Actual Text:", some_text)
    print("Stop Words:", stop_word_list)
    print("Filtered Words:", filtered_word_list)
    print("Filtered Text:", " ".join(filtered_word_list))


if __name__ == "__main__":
    main()
