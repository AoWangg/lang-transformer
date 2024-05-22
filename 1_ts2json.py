import re
lang = 'vi'

with open(lang+'.ts', 'r') as file:
    data = file.read()

data = re.sub(r'(`[^`]*`)', r'"\1"', data)   #处理反引号
data = re.sub(r'(\w+)\s*:(\s+)', r'"\1":\2', data)   #key加上双引号
data = re.sub(r'(?<!:),\s*(?=\s*[}\]])', '', data)  #去掉尾随逗号
data = re.sub(r':\s*\'([^\']+)\'', r': "\1"', data)  #单引号变双引号

data = data.replace('export default ', '').strip()  
if data and data[-1] == ';':  
    data = data[:-1]

with open(lang+'.json', 'w') as file:
    file.write(data)


print(f'Json file has been created.')