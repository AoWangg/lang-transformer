import json
import pandas as pd
import re

lang = 'ja'

with open(lang+'.json', 'r', encoding='utf-8') as file:
    file_content = file.read()

try:
    data_dict = json.loads(file_content)
except json.JSONDecodeError:
    print("The file content is not a valid JSON.")
    exit()

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flat_dict = flatten_dict(data_dict)

df = pd.DataFrame(list(flat_dict.items()), columns=['Key', 'Value'])

excel_filename = lang+'_exported_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f'Excel file {excel_filename} has been created.')