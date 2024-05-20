import requests
from bs4 import BeautifulSoup
import re

def extract_mitre_links(url):
    # Fetch the HTML content of the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch content from {url}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element with class "additional-link" to extract MITRE links
    additional_links_div = soup.find('div', class_='additional-link')
    if additional_links_div is None:
        return []

    # Find all links within the div that start with "attack.mitre.org"
    links = additional_links_div.find_all('a', href=re.compile(r'^https://attack\.mitre\.org'))
    mitre_links = [link['href'] for link in links]
    return mitre_links

def search_mitre_details():
    with open("mitre_results.txt", "a") as file:  # Open the file in append mode
        base_url = "https://snort.org/rule-docs/1-"
        for page_number in range(1, 300841):
            url = f"{base_url}{page_number}"
            mitre_details = extract_mitre_links(url)
            if mitre_details:
                print(f"SID: {page_number}, MITRE URLs: {mitre_details}\n")
                file.write(f"SID: {page_number}, MITRE URLs: {mitre_details}\n")
            else:
                print("no results")



search_mitre_details()
