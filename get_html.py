# Get Html for all the websites

import os, re
import requests
from bs4 import BeautifulSoup
from datetime import date

root_folder = "./Produtos/"
pattern_file = r"\blist_\w+"
pattern_link = r"https?://(?:www\.)?([^/.]+)\."

def main():
    date_today = date.today().strftime("%Y_%m_%d")

    files_web_links = get_link_files()

    for file_path in files_web_links:
        file_path_folder = file_path.rsplit('/', 1)[0]
        file_links  = read_file_links(file_path)
 
        for link in file_links:
            match_link = re.search(pattern_link, link) 
            response = requests.get(link)
            if response.status_code == 200:
               write_html_to_path(response.content.decode(), date_today, file_path_folder, match_link.group(1))
            else:
                print("Failed Request: ", link)

# Não é uma forma eficiente de fazer isto
# 
# Guardar o caminho relativos dos ficheiros em uma
# ou
# Agrupar estes ficheiros numa pasta à parte
def get_link_files() -> list[str]:
    list_files = []
    for root, dirs, files in os.walk(root_folder):
       for filename in files:
            matches_list = re.findall(pattern_file, filename)
            if len(matches_list) == 1:
                file_web_links = matches_list[0]
                file_path = os.path.join(root, filename)
                list_files.append(file_path)
    return list_files

def read_file_links(file_path) -> list[str]:
    with open(file_path, 'r') as file:
        content = file.read()
        links = content.split()
    return links

def write_html_to_path(html, date, path, site):
    path_folder = path + "/" + site
    path_file = path_folder + "/" + date + ".txt"

    if not os.path.exists(path_folder):
        os.makedirs(path_folder)

    if os.path.exists(path_file):
        print(f"File {path_file} already exists", path_file)
    else:
        with open (path_file, 'w') as file:
            file.write(html)
            print(f"File {path_file} written")









if __name__ == "__main__":
    main()
