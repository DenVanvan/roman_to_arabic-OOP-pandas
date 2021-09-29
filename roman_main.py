from os import path
from numpy import character, number
import pandas as pd
from roman_class import RomanInt
from prettytable import PrettyTable

with open('p089_roman.txt', 'r') as file:
    input_roman = file.readlines()
    input_roman = [item.replace('\n','') for item in input_roman]

output_roman = [RomanInt(roman_int).result for roman_int in input_roman]
output_arabic = [RomanInt(roman_int).integer for roman_int in input_roman]

df = pd.DataFrame({'Input Roman':input_roman, 'Output Arabic': output_arabic, 'Output Roman': output_roman})
df['True'] =df['Input Roman'] != df['Output Roman']
level_map = {True: 'changed', False: ''}
df['Changed'] = df['True'].map(level_map)
df['Output Arabic'] = df['Output Arabic'].apply(str)

df = df[['Input Roman', 'Output Arabic', 'Output Roman', 'Changed']]

df_2 = PrettyTable(border = False, header = False)
df_2.add_rows(df.values)
df_2.field_names = df.columns
print(df_2)

with open('roman_out.txt', 'w') as file:

    df_2 = df_2.get_string()
    file.write(df_2)
    file.write('\n')





