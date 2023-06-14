import utilities
import chatGPT

GDPR_text = utilities.read_txt('GDPR_clean.txt')

GDPR_all_text_per_article_dict = {}
temp_text = ''
for i in range(len(GDPR_text)):

    if i != len(GDPR_text) - 1:

        if GDPR_text[i].startswith('Article ') and GDPR_text[i] == 'Article 1':
            temp_text = ''

        elif GDPR_text[i].startswith('Article ') and GDPR_text[i] != 'Article 1':
            index = int(GDPR_text[i].replace('Article ', '')) - 1
            GDPR_all_text_per_article_dict.update({index: temp_text})
            temp_text = ''

        else:
            temp_text += GDPR_text[i]

    elif i == len(GDPR_text) - 1:
        GDPR_all_text_per_article_dict.update({99: temp_text})

#utilities.write_pickle(GDPR_all_text_per_article_dict, 'GDPR_all_text_per_article_dict.pkl')

articles_of_interest = utilities.read_txt('uniquely_referenced_articles.txt', 'out_files/')

for i in range(len(articles_of_interest)):
    articles_of_interest[i] = int(articles_of_interest[i].replace('\n', ''))

chatgpt_predictions_list = []

for article in articles_of_interest:
    GDPR_article_text = GDPR_all_text_per_article_dict[article]

    prompt = f"Open-textured concepts are concepts that are inherently vague or indeterminate. One can find them using the following four questions:\n" \
             f"Question 1) Is there more than one quantity associated with the word?\n" \
             f"Question 2) Does the term include a broad spectrum of meanings?\n" \
             f"Question 3) Is there no agreement on a single version of the definition or standard?\n" \
             f"Question 4) Does the word represent a value or is it value-laden, for example because it presupposes the acceptance of specific moral principles or beliefs?\n" \
             f"For example, in the following sentence, “Bald” is an open-textured concept in the following sentence because it matches with question 1: “Peter is bald.”\n" \
             f"In the following text, please find all open-textured concepts by using the five questions and also indicate which question was used for each of the open-textured concepts identified:\n" \
             f"{GDPR_article_text}" \
             f"For your response ONLY provide me with a list with the following format:\n" \
             f"'(Open-texture-word)[Based-on-question]'\n" \
             f"Provide no text other than the list of words."

    response_list = chatGPT.predict_ot_words(prompt).replace("'", '')

    if '\n' in response_list:
        response_list = response_list.split('\n')
    else:
        response_list = response_list.split(',')

    for line in response_list:
        if '[' in line:
            chatgpt_predictions_list.append(
                [line.split('[')[0], line.split('[')[1].replace(']', '').split(','), article]
            )
        elif '(' in line:
            chatgpt_predictions_list.append(
                [line.split('(')[0], line.split('(')[1].replace(')', '').split(','), article])

predictions_df = utilities.list_to_csv(chatgpt_predictions_list, ["Word", "Based on question", "Reference article"])


utilities.write_excel(
    dataframe=predictions_df,
    file_name="chatGPT_OT_predictions.xlsx",
    file_path='C:/Users/john1/PycharmProjects/GDPR_scrapping/chatGPT_OT_prediction/out_files/'
)
utilities.write_txt(
    out_txt=chatgpt_predictions_list,
    file_name="chatGPT_predictions.txt",
    file_path='C:/Users/john1/PycharmProjects/GDPR_scrapping/chatGPT_OT_prediction/out_files/'
)
