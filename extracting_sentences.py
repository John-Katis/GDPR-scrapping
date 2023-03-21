import pickle
from nltk import tokenize
import pandas as pd


def load_pickle(name_to_load):
    with open(
            fr'C:\Users\john1\PycharmProjects\GDPR_scrapping\{name_to_load}.pkl',
            'rb'
    ) as f:
        dictionary_to_return = pickle.load(f)

    f.close()
    return dictionary_to_return


GDPR_dict = load_pickle('GDPR_articles_dictionary')
reference_to_extract = load_pickle('sheet_to_word_to_reference_list_dictionary')

# keys: article, section, paragraph
word_sentence_list = []
for key in reference_to_extract.keys():
    for keyword in reference_to_extract[key].keys():
        for dictionary in reference_to_extract[key][keyword]:
            if dictionary['paragraph'] != None:
                if ' ' in dictionary['paragraph']:
                    dictionary['paragraph'] = dictionary['paragraph'].replace(' ', '')
                temp_text = GDPR_dict[dictionary['article']][dictionary['section']][dictionary['paragraph']]
                temp_text = tokenize.sent_tokenize(temp_text)

                for sentence in temp_text:
                    if keyword.lower() in sentence.lower():
                        word_sentence_list.append(
                            (keyword, sentence)
                        )

            elif dictionary['section'] != None:
                temp_text = GDPR_dict[dictionary['article']][dictionary['section']]['text']
                temp_text = tokenize.sent_tokenize(temp_text)

                for sentence in temp_text:
                    if keyword.lower() in sentence.lower():
                        word_sentence_list.append(
                            (keyword, sentence)
                        )

            elif dictionary['article'] != None:
                temp_text = GDPR_dict[dictionary['article']]['text']
                temp_text = tokenize.sent_tokenize(temp_text)

                for sentence in temp_text:
                    if keyword.lower() in sentence.lower():
                        word_sentence_list.append(
                            (keyword, sentence)
                        )


words_list = []
sentences_list = []
for item in word_sentence_list:
    words_list.append(item[0])
    sentences_list.append(item[1])

data = {
    'Word': words_list,
    'Sentence': sentences_list
}

df = pd.DataFrame(data)
df.to_excel(r'C:\Users\john1\Desktop\Work\sentence_extraction_GDPR\extracted_sentences.xlsx')
