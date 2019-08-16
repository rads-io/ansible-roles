from bs4 import BeautifulSoup
import requests
import re
import os
print("STATUS: import complete")

url = 'https://cran.r-project.org/src/contrib/'
ext = 'tar.gz'

def listFD(url, ext=''):
    page = requests.get(url).text
    # print(page)
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

print("STATUS: loading data from the server url")
res = listFD(url, ext)

print("STATUS: fetching the requrired data")
res_e_ver = ""
res_class_int = ""
for file in res:
    if re.match(r"^https://cran\.r-project\.org/src/contrib//e[0-9].*\.tar\.gz$", file):
        res_e_ver = file.split(r"//")[2]
    elif re.match(r"https://cran\.r-project\.org/src/contrib//classInt_.*\.tar\.gz", file):
        res_class_int = file.split(r"//")[2]

print(f"STATUS:\n\t{res_e_ver}\n\t{res_class_int}")

old_e_ver = "      - e1071_1.7-2.tar.gz"
old_classInt = "      - classInt_0.3-3.tar.gz"
new_e_ver = f"      - {res_e_ver}"
new_classInt = f"      - {res_class_int}"
file_path = r"dependencies/tasks/r-cran.yml"

os.system(f'sed --in-place "s/{old_e_ver}/{new_e_ver}/g" "{file_path}"')
os.system(f'sed --in-place "s/{old_classInt}/{new_classInt}/g" "{file_path}"')

