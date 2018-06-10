#
# POS - Part Of Speech Tests
#

from nltk import pos_tag_sents
from nltk.tokenize import sent_tokenize, word_tokenize


some_text = "The goal was to best the competition. His latest song was a personal best. Hence, he received the best song of the year award. He played best after a couple of martinis."
 

def main():
    print ("----------[ POS TESTS ]-------------")

    text_sentence_tokens = sent_tokenize(some_text)
    print (text_sentence_tokens)

    text_word_tokens = []
    for sentence_token in text_sentence_tokens:
        text_word_tokens.append(word_tokenize(sentence_token))
 
    print (text_word_tokens)    

    text_tagged = pos_tag_sents(text_word_tokens)
    print (text_tagged)


if __name__ == "__main__":
    main()
