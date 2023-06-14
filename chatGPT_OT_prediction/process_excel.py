import pandas as pd
import utilities

all_referenced = utilities.read_excel('all_referenced.xlsm')
sheet_keys = ['G', 'H', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
# removed 'I', 'J', 'R', 'Z'

GDPR_only_csv = pd.DataFrame(columns=all_referenced['G'].columns)

for key in sheet_keys:
    GDPR_only_csv = GDPR_only_csv.append(all_referenced[key].loc[all_referenced[key]['Reference law'] == 'GDPR'])

reference_articles_list = utilities.series_to_list(GDPR_only_csv['Reference article'])
for i in range(len(reference_articles_list)):
    if type(reference_articles_list[i]) == str:
        if '(' in reference_articles_list[i]:
            reference_articles_list[i] = reference_articles_list[i].split('(')[0]

        if reference_articles_list[i].startswith('Art. '):
            reference_articles_list[i] = reference_articles_list[i].replace('Art. ', '')
        reference_articles_list[i] = reference_articles_list[i].replace(' ', '')
    else:
        reference_articles_list[i] = str(reference_articles_list[i])


unique_ref = list(set(reference_articles_list))
print(unique_ref)
unique_ref.remove(']')
print(unique_ref)

for i in range(len(unique_ref)):
    unique_ref[i] = int(unique_ref[i])

unique_ref = sorted(unique_ref)

for i in range(len(unique_ref)):
    unique_ref[i] = str(unique_ref[i])

utilities.write_excel(
    dataframe=GDPR_only_csv,
    file_name='all_referenced_GPDR_only.xlsx',
    file_path='C:/Users/john1/PycharmProjects/GDPR_scrapping/chatGPT_OT_prediction/out_files/'
)

utilities.write_txt(
    out_txt=unique_ref,
    file_name='uniquely_referenced_articles.txt',
    file_path='C:/Users/john1/PycharmProjects/GDPR_scrapping/chatGPT_OT_prediction/out_files/'
)

n = utilities.read_txt(
    file_name='uniquely_referenced_articles.txt',
    file_path='C:/Users/john1/PycharmProjects/GDPR_scrapping/chatGPT_OT_prediction/out_files/'
)
print([int(p.replace('\n', '')) for p in n])
