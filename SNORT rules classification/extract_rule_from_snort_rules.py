import re
import requests
from bs4 import BeautifulSoup

# Read the file
with open("SNORT rules classification\snort3-community.rules", "r") as file:
    lines = file.readlines()

count = 1
# Search for the msg and send it to the URL
for line in lines:
    match = re.search(r'msg:"(.*?)"', line)
    print(f"Processing line {count}")
    if match:
        msg_text = match.group(1)
        url = f"https://snort.org/rule_docs?utf8=%E2%9C%93&search_type=standard&simple_search%5Bsid_or_explanation_or_message_or_cves_cve_key_i_cont%5D={msg_text}&submit_rule_search="
        try:
            response = requests.get(url)
            response.raise_for_status()  # This will raise an error for non-200 status codes
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching content from {url}: {e}")
            continue  # This will skip to the next iteration of the loop if an error occurs
        if response.status_code != 200:
            print(f"Failed to fetch content from {url}")
            continue

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the links with class "categories"
        link_elements = soup.find_all('a', class_='categories')

        # Iterate over the links and save them into a file
        with open("url_links.txt", "a") as file:
            for link_element in link_elements:
                link = link_element['href']
                try:
                    with open("SNORT rules classification\\url_links.txt", "r") as f:
                        if link in f.read():
                            continue
                except FileNotFoundError:
                    pass
                file.write(f"https://snort.org/{link}\n")

    count += 1
print("Done")