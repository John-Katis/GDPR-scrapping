import pandas as pd
from string import ascii_lowercase
import pickle


def save_in_project(dictionary_to_save, dict_name):
    with \
            open(
                fr'C:\Users\john1\PycharmProjects\GDPR_scrapping\{dict_name}.pkl',
                'wb'
            ) \
    as f:
        pickle.dump(dictionary_to_save, f)


all_sheets = pd.read_excel(r'C:\Users\john1\Desktop\Work\sentence_extraction_GDPR\all_referenced.xlsm', sheet_name=None)
sheet_keys = ['G', 'H', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
# removed 'Z', 'I', 'J', 'R'

# Some "Reference article" start with "Art. " (and one " Art. ")- account for that
# Interesting columns: "Word" and "Reference article"
# Sheets M, N, U have more than one "Reference article"
# Sheets M, N, U have many articles separated by '/'

# Sheet I, J, R has no word column
# Sheet Z has no "Reference article"

sheet_to_word_to_article_dict = {}
# store lists of dictionaries with article, section and paragraph number

for key in sheet_keys:
    #temp_word_dict_list = []
    # initializing empty dictionary to update later
    sheet_to_word_to_article_dict[key] = {}

    for index, row in all_sheets[key].iterrows():
        word = ''
        article = None
        section = None
        paragraph = None
        temp_word_dict = {}
        temp_references_list = []
        temp_dict = {}

        if row['Reference law'] == 'GDPR':
            word = row['Word']
            #print(key, word)
            temp_reference_article = row['Reference article']

            if isinstance(temp_reference_article, int):
                article = temp_reference_article

                temp_dict['article'] = article
                temp_dict['section'] = section
                temp_dict['paragraph'] = paragraph
                temp_references_list.append(temp_dict)

                temp_word_dict[word] = temp_references_list
                sheet_to_word_to_article_dict[key].update(temp_word_dict)

            elif temp_reference_article.startswith('Art. '):
                temp_reference_article = temp_reference_article.replace('Art. ', '')

                if '/' in temp_reference_article:
                    all_referenced = temp_reference_article.split('/')

                    for reference in all_referenced:
                        article = None
                        section = None
                        paragraph = None
                        temp_dict = {}
                        if reference.startswith('Art. '):
                            reference = reference.replace('Art. ', '')

                        if '(' not in reference:
                            article = int(reference)

                        elif '(' in reference:
                            reference = reference.replace(')', '')
                            reference_parts = reference.split('(')

                            if len(reference_parts) == 2:
                                article = int(reference_parts[0])
                                if reference_parts[1] not in ascii_lowercase:
                                    section = int(reference_parts[1])
                                else:
                                    section = reference_parts[1]

                            elif len(reference_parts) == 3:
                                article = int(reference_parts[0])
                                if reference_parts[1] not in ascii_lowercase:
                                    section = int(reference_parts[1])
                                else:
                                    section = reference_parts[1]
                                paragraph = reference_parts[2]

                        temp_dict['article'] = article
                        temp_dict['section'] = section
                        temp_dict['paragraph'] = paragraph
                        temp_references_list.append(temp_dict)

                else:
                    if '(' not in temp_reference_article:
                        article = int(temp_reference_article)

                    elif '(' in temp_reference_article:
                        temp_reference_article = temp_reference_article.replace(')', '')
                        temp_reference_article_parts = temp_reference_article.split('(')

                        if len(temp_reference_article_parts) == 2:
                            article = int(temp_reference_article_parts[0])
                            if temp_reference_article_parts[1] not in ascii_lowercase:
                                section = int(temp_reference_article_parts[1])
                            else:
                                section = temp_reference_article_parts[1]

                        elif len(temp_reference_article_parts) == 3:
                            article = int(temp_reference_article_parts[0])
                            if temp_reference_article_parts[1] not in ascii_lowercase:
                                section = int(temp_reference_article_parts[1])
                            else:
                                section = temp_reference_article_parts[1]
                            paragraph = temp_reference_article_parts[2]

                    temp_dict['article'] = article
                    temp_dict['section'] = section
                    temp_dict['paragraph'] = paragraph
                    temp_references_list.append(temp_dict)

                temp_word_dict[word] = temp_references_list
                sheet_to_word_to_article_dict[key].update(temp_word_dict)

            else:
                if '/' in temp_reference_article:
                    all_referenced = temp_reference_article.split('/')

                    for reference in all_referenced:
                        article = None
                        section = None
                        paragraph = None
                        temp_dict = {}
                        if reference.startswith('Art. '):
                            reference = reference.replace('Art. ', '')

                        if '(' not in reference:
                            article = int(reference)

                        elif '(' in reference:
                            reference = reference.replace(')', '')
                            reference_parts = reference.split('(')

                            if len(reference_parts) == 2:
                                article = int(reference_parts[0])
                                if reference_parts[1] not in ascii_lowercase:
                                    section = int(reference_parts[1])
                                else:
                                    section = reference_parts[1]

                            elif len(reference_parts) == 3:
                                article = int(reference_parts[0])
                                if reference_parts[1] not in ascii_lowercase:
                                    section = int(reference_parts[1])
                                else:
                                    section = reference_parts[1]
                                paragraph = reference_parts[2]

                        temp_dict['article'] = article
                        temp_dict['section'] = section
                        temp_dict['paragraph'] = paragraph
                        temp_references_list.append(temp_dict)

                else:
                    if '(' not in temp_reference_article:
                        article = int(temp_reference_article)

                    elif '(' in temp_reference_article:
                        temp_reference_article = temp_reference_article.replace(')', '')
                        temp_reference_article_parts = temp_reference_article.split('(')

                        if len(temp_reference_article_parts) == 2:
                            article = int(temp_reference_article_parts[0])
                            if temp_reference_article_parts[1] not in ascii_lowercase:
                                section = int(temp_reference_article_parts[1])
                            else:
                                section = temp_reference_article_parts[1]

                        elif len(temp_reference_article_parts) == 3:
                            article = int(temp_reference_article_parts[0])
                            if temp_reference_article_parts[1] not in ascii_lowercase:
                                section = int(temp_reference_article_parts[1])
                            else:
                                section = temp_reference_article_parts[1]
                            paragraph = temp_reference_article_parts[2]

                    temp_dict['article'] = article
                    temp_dict['section'] = section
                    temp_dict['paragraph'] = paragraph
                    temp_references_list.append(temp_dict)

                temp_word_dict[word] = temp_references_list
                sheet_to_word_to_article_dict[key].update(temp_word_dict)

# USE FOR PRINTING THE OUTPUT DICTIONARY
#for key in sheet_to_word_to_article_dict.keys():
#    print('###########################')
#    print(key)
#    for word in sheet_to_word_to_article_dict[key].keys():
#        print('----------------')
#        print(word)
#        print(sheet_to_word_to_article_dict[key][word])

save_in_project(sheet_to_word_to_article_dict, 'sheet_to_word_to_reference_list_dictionary')
