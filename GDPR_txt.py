from string import ascii_lowercase
from read_excel import save_in_project


def clean_key(key_string):
    key_string = key_string.replace('(', '')
    key_string = key_string.replace(')', '')
    key_string = key_string.replace('.', '')
    key_string = key_string.replace('Article ', '')
    key_string = key_string.replace(' ', '')
    return key_string


GDPR_dict = {}
with open(r"C:\Users\john1\Desktop\Work\sentence_extraction_GDPR\GDPR_clean.txt", 'r', encoding='utf-8') as f:
    GDPR = f.readlines()

outer_key = None
inner_key = None
inner_subkey = None

for line in GDPR:
    line = line.replace('\n', '')

    if line.startswith('Article ') and line == 'Article 1':
        outer_key = int(clean_key(line))
        paragraph_dict = {}
        article_text = {}

    elif line.startswith('Article ') and line != 'Article 1':
        GDPR_dict[outer_key] = {}
        if len(article_text) != 0:
            GDPR_dict[outer_key].update(article_text)
        GDPR_dict[outer_key].update(paragraph_dict)
        outer_key = int(clean_key(line))
        paragraph_dict = {}
        article_text = {}

    elif line == "This Regulation shall be binding in its entirety and directly applicable in all Member States. Done at Brussels, 27 April 2016.":
        GDPR_dict[outer_key] = {}
        if len(article_text) != 0:
            GDPR_dict[outer_key].update(article_text)
        GDPR_dict[outer_key].update(paragraph_dict)

    elif '\t' in line:
        temp_line_key = clean_key(line.split('\t')[0])
        temp_line_text = line.split('\t')[1].replace('\n', '')

        if temp_line_key not in ascii_lowercase and temp_line_key != '-':
            inner_key = int(temp_line_key)
            paragraph_dict[inner_key] = {}
            paragraph_dict[inner_key].update({'text': temp_line_text})

        else:
            inner_subkey = temp_line_key
            paragraph_dict[inner_key].update({inner_subkey: temp_line_text})

    else:
        article_text = {'text': line}

save_in_project(GDPR_dict, 'GDPR_articles_dictionary')
