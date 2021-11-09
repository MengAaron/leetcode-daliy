import logging

from stanfordcorenlp import StanfordCoreNLP

if __name__ == '__main__':
    sentence = 'hello'
    nlp = StanfordCoreNLP(r'D:\Downloads\stanford-corenlp-4.3.1', lang='zh', logging_level=logging.INFO)
    ann = nlp.ner(sentence)
    print(ann)
    nlp.close()

