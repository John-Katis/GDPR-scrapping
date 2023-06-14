import pickle
import pandas as pd


""" READ PICKLE TO DICTIONARY / WRITE DICTIONARY TO PICKLE """


def read_pickle(file_name: str, file_path="C:/Users/john1/PycharmProjects/GDPR_scrapping/"):
    with open(
            fr'{file_path}{file_name}',
            'rb'
    ) as f_in:
        dictionary_to_return = pickle.load(f_in)

    f_in.close()
    return dictionary_to_return


def write_pickle(dictionary_to_save: dict, file_name: str, file_path="C:/Users/john1/PycharmProjects/GDPR_scrapping/"):
    with open(
                fr'{file_path}{file_name}',
                'wb'
    ) as f_out:
        pickle.dump(dictionary_to_save, f_out)


""" READ TXT TO LIST / WRITE LIST TO TXT """


def write_list_to_file(data_list, file):
    for item in data_list:
        if isinstance(item, list):
            write_list_to_file(item, file)
        else:
            file.write("%s " % str(item))


def read_txt(file_name: str, file_path="C:/Users/john1/PycharmProjects/GDPR_scrapping/"):
    with open(fr'{file_path}{file_name}', 'r', encoding='utf-8') as f_in:
        in_txt = f_in.readlines()

    f_in.close()
    return in_txt


def write_txt(out_txt: list or str, file_name: str, file_path="C:/Users/john1/PycharmProjects/GDPR_scrapping/"):
    with open(fr'{file_path}{file_name}', 'w', encoding='utf-8') as f_out:
        if type(out_txt) == list:
            for line in out_txt:
                if type(line) == list:
                    write_list_to_file(line, f_out)
                    f_out.write('\n')
                elif type(line) == str:
                    f_out.write(line+'\n')
        else:
            f_out.write(out_txt)


""" READ EXCEL TO DATAFRAME / WRITE DATAFRAME TO EXCEL """


def read_excel(file_name: str, file_path="C:/Users/john1/PycharmProjects/GDPR_scrapping/"):
    in_excel = pd.read_excel(fr'{file_path}{file_name}', sheet_name=None)
    return in_excel


def write_excel(dataframe: pd.DataFrame, file_name: str, file_path="C:/Users/john1/PycharmProjects/GDPR_scrapping/"):
    dataframe.to_excel(fr'{file_path}{file_name}', index=False)


""" READ / WRITE CSV """


def read_csv(file_name: str, file_path="C:/Users/john1/PycharmProjects/GDPR_scrapping/"):
    in_csv = pd.read_csv(fr'{file_path}{file_name}')
    return in_csv


def write_csv(dataframe: pd.DataFrame, file_name: str, file_path="C:/Users/john1/PycharmProjects/GDPR_scrapping/"):
    dataframe.to_csv(fr'{file_path}{file_name}', index=False)


""" LIST TO DATAFRAME / SERIES TO LIST """


def list_to_csv(data_list: list[list], columns: list[str]):
    df = pd.DataFrame(data=data_list, columns=columns)
    return df


def series_to_list(df_col: pd.Series):
    return df_col.to_list()
