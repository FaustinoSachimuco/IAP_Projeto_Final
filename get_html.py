# Get Html for all the websites

import os, re
import requests
from bs4 import BeautifulSoup
from datetime import date

root = "/home/royo/Documents/IAP_Projeto_Final/Produtos"
pattern_file = r"\blist_\w+"
pattern_link = r"https?://(?:www\.)?([^/.]+)\."

def main():
    date_today = date.today().strftime("%Y_%m_%d")

    files_web_links = get_pattern_files(root, pattern_file)

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


def get_pattern_files(root_folder, pattern) -> list[str]:
    list_files = []
    for folder in os.listdir(root_folder):
        folder_path = root_folder + folder
        for filename in os.listdir(folder_path):
            matches_list = re.findall(pattern, filename)
            if len(matches_list) == 1:
                file_web_links = matches_list[0]
                file_path = os.path.join(folder_path, filename)
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
        print(f"File {path_file} already exists")
    else:
        with open (path_file, 'w') as file:
            file.write(html)
            print(f"File {path_file} written")


if __name__ == "__main__":
    main()
