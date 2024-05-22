import pandas as pd
import json
import ast

def unflatten_dict(dictionary, separator='.'):
    result_dict = dict()
    for key, value in dictionary.items():
        parts = key.split(separator)
        d = result_dict
        for part in parts[:-1]:
            if part not in d:
                d[part] = dict()
            d = d[part]
        d[parts[-1]] = value
    return result_dict

def convert_value(value):
    try:
        if value.startswith('[') and value.endswith(']'):
            return ast.literal_eval(value)
        else:
            return ast.literal_eval(value)
    except Exception as e:
        print(f"Error converting value: {value}, error: {e}")
        # 可以选择返回原始值或 None
        return value  # 或者 return None

lang = 'vi'
excel_filename = lang+'_exported_data.xlsx'

df = pd.read_excel(excel_filename)
data_dict = df.set_index('Key')['Value'].apply(convert_value).to_dict()

unflattened_dict = unflatten_dict(data_dict)

with open(lang+'2.ts', 'w', encoding='utf-8') as file:
    file.write('export default ' + json.dumps(unflattened_dict, ensure_ascii=False, indent=2) + ';')

print(f'TypeScript file {lang}2.ts has been created.')