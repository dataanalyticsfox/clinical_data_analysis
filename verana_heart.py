import pandas as pd

def open_and_clean(csv_file):
    # open csv file as a dataframe
    heart_df = pd.read_csv(csv_file)

    # set column headers to lower for consistency
    heart_df.columns = heart_df.columns.str.lower()

    # drop columns with all null values, keep patient_id and note columns
    heart_df.dropna(axis=1, how='all', inplace=True)

    return heart_df

# function to search for keywords in csv
def contains_keyword(note):
    keywords = [
    'heart attack', 'pain in chest', 'pain in the chest', 'fluttering', 
    'pressure in chest', 'tightness in chest', 'chest pain', 'pressure in the chest'
]
    note = note.lower()
    return any(keyword in note for keyword in keywords)

def main():
    # user defined file path 
    csv_file = '/Users/carrieminerich/Desktop/verana/patient_note.csv'

    # run open_and_clean function
    heart_df = open_and_clean(csv_file)

    # create final_heart_df by including only keywords from heart_df
    final_heart_df = heart_df[heart_df['note'].apply(contains_keyword)]

    # count of rows in final_heart_df
    print(f"Count of rows in final_heart_df: {len(final_heart_df)}")

    final_heart_df.to_csv('filterd_heart_dataset.csv', index=False) 

if __name__ == "__main__":
    main()