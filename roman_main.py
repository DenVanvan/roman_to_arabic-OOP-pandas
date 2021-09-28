import pandas as pd
from roman_class import RomanInt

with open('p089_roman.txt', 'r') as file:
    input_roman = file.readlines()
    input_roman = [item.replace('\n','') for item in input_roman]

output_roman = [RomanInt(roman_int).result for roman_int in input_roman]
output_arabic = [RomanInt(roman_int).integer for roman_int in input_roman]

df = pd.DataFrame({'Input Roman':input_roman, 'Output Arabic': output_arabic, 'Output Roman': output_roman})
df['True'] =df['Input Roman'] != df['Output Roman']
level_map = {True: 'changed', False: None}
df['Changed'] = df['True'].map(level_map)

df = df[['Input Roman', 'Output Arabic', 'Output Roman', 'Changed']]

df.to_csv('roman_out.txt', index=False, columns=None)
