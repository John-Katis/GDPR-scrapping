#import PyPDF2

#pdf = PyPDF2.PdfReader(r"C:\Users\john1\Desktop\Work\sentence_extraction_GDPR\EU_GDPR_Full_Text_EN.pdf")

#print(len(pdf.pages))

#page = pdf.pages[1]

#page_txt = page.extract_text()
#for line in page_txt.split('\n'):
#    print(line)
#print(type(page_txt))

import xmltodict
import pickle

with open("C:/Users/john1/Desktop/Work/sentence_extraction_GDPR/GDPR-xml/consolidated-with-corrected-preamble/gdpr-consolidated-with-corrected-preamble-en.xml", 'r') as f:
    xml_GDPR = f.read()

GDPR_dict = xmltodict.parse(xml_GDPR)
print(len(GDPR_dict['CONS.ACT']['CONS.DOC']['ENACTING.TERMS']['DIVISION']))
print(GDPR_dict['CONS.ACT']['CONS.DOC']['ENACTING.TERMS']['DIVISION'][0]['ARTICLE'][1]['PARAG'][1]['ALINEA'].keys())

# ['DIVISION'] is a list of 11 items (= number of GDPR chapters)
# ['ARTICLE'] is a list of articles per chapter (varies)
# Each ARTICLE contains a number of paragraphs (list format) (Maybe there are some with one paragraph only)
# Text is to be found in 'ALINEA' tags or in <P> and <TXT> tags within the <ALINEA> one

# Some 'ALINEA' tags are dictionaries with a list of entries -> <TXT> tags contain the text
# Some 'ALINEA' tags contain plain text (str type)


print((GDPR_dict['CONS.ACT']['CONS.DOC']['ENACTING.TERMS']['DIVISION'][-1]['ARTICLE'][-1]))
# 2,3,5,6 has 'DIVISION' with list of 'ARTICLES'
count = 0
for i in range(11):
    print(f'~~ {i} ~~')
    if i in [2,3,5,6]:
        for div in GDPR_dict['CONS.ACT']['CONS.DOC']['ENACTING.TERMS']['DIVISION'][i]['DIVISION']:
            print(len(div['ARTICLE']))
            count += len(div['ARTICLE'])
    else:
        print(len(GDPR_dict['CONS.ACT']['CONS.DOC']['ENACTING.TERMS']['DIVISION'][i]['ARTICLE']))
        count += len(GDPR_dict['CONS.ACT']['CONS.DOC']['ENACTING.TERMS']['DIVISION'][i]['ARTICLE'])

#print(count)

# USE TO LOAD THE DICTIONARY
# IT CONTAINS THE DIFFERENT SHEETS AS DICTIONARY KEYS
# EACH KEY CONTAINS A DICTIONARY THAT CONTAINS ALL THE WORDS IN GDPR
# EACH WORD IN GDPR CONTAINS EITHER A SINGLE DICTIONARY OR A LIST OF DICTIONARIES
# EACH OF THEM CONTAIN 4 KEYS (article, section, paragraph, subparagraph)
# EACH OF THE 4 KEYS CAN HAVE A VALUE OR None
with open(
            r'C:\Users\john1\PycharmProjects\GDPR_scrapping\sheet_to_word_to_reference_list_dictionary.pkl',
            'rb'
    ) as f:
    dictionary1 = pickle.load(f)

#for key in dictionary1.keys():
#    print('###########################')
#    print(key)
#    for word in dictionary1[key].keys():
#        print('----------------')
#        print(word)
#        print(dictionary1[key][word])
