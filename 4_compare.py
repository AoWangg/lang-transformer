import json
import pandas as pd
import re

lang1 = 'en'
lang2 = 'vi'

with open(lang1+'.json', 'r', encoding='utf-8') as file:
    file_content1 = file.read()

with open(lang2+'.json', 'r', encoding='utf-8') as file:
    file_content2 = file.read()

try:
    data_dict1 = json.loads(file_content1)
    print(data_dict1)
    data_dict2 = json.loads(file_content2)

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

flat_dict1 = flatten_dict(data_dict1)
flat_dict2 = flatten_dict(data_dict2)

print(flat_dict1)
print(flat_dict2)

df1 = pd.DataFrame(list(flat_dict1.items()), columns=['Key', 'Value'])
df2 = pd.DataFrame(list(flat_dict2.items()), columns=['Key', 'Value'])

print(df1)

df2_keys = df2['Key'].tolist()

for index, row in df1.iterrows():
    key_to_check = row['Key']  

    if key_to_check not in df2_keys:
        # 如果 df2 中不存在这个 'Key', 则添加这个 'Key' 和 'Value'
        df2 = pd.concat([df2, pd.DataFrame([row])], ignore_index=True)
        # df2 = pd.concat([df2, pd.DataFrame([[row['Key'], row['Value']]])], ignore_index=True)

print(df2)

excel_filename = lang2+'_exported_data.xlsx'
df2.to_excel(excel_filename, index=False)

print(f'Excel file {excel_filename} has been created.')