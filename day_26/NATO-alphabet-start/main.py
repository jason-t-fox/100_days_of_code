import pandas
import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
# nato_dict = {key: value for key, value in nato_df[['letter', 'code']].values}
# iterrow loops through each row and gives you the columns in the dataframe you want.
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)

name = 'jason'.upper()
nato = [nato_dict[letter] for letter in name]
# for letter in name:
#     nato = nato_dict[letter]
print(nato)
