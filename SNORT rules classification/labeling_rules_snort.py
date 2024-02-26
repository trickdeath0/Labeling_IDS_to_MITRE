# import requests
# from bs4 import BeautifulSoup
# import re


# def save_mitre_details(url, mitre_details):
#     with open('mitre_details.txt', 'a') as file:
#         file.write(f"URL: {url}\n")
#         file.write(f"MITRE Details: {mitre_details}\n")
#         file.write("-------------------\n")


# def extract_mitre_links(url):
#     # Fetch the HTML content of the URL
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Failed to fetch content from {url}")
#         return []

#     # Parse the HTML content
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Check if the element with ID "tab-mitre" exists
#     mitre_details_tab = soup.find('div', class_='mitre-legacy')
#     if mitre_details_tab:
#         # Extract the URL or other information as needed
#         return "MITRE Details found"

#     # Find the div with class "additional-link"
#     additional_links_div = soup.find('div', class_='additional-link')
#     if additional_links_div is None:
#         print("No additional links found")
#         return []

#     # Find all links within the div
#     links = additional_links_div.find_all('a')
    
#     # Filter links that start with "attack.mitre.org"
#     mitre_links = [link['href'] for link in links if link['href'].startswith("https://attack.mitre.org")]

#     return mitre_links




# # Function to search for MITRE details from page 1 to 60000
# def search_mitre_details():
#     base_url = "https://snort.org/rule-docs/1-"
#     for page_number in range(1, 10): # 300841
#         url = f"{base_url}{page_number}"
#         mitre_details = extract_mitre_links(url)
#         if mitre_details:
#             save_mitre_details(url, mitre_details)

# # Execute the search
# search_mitre_details()









import requests
from bs4 import BeautifulSoup
import re


def save_mitre_details(url, tactic, technique, technique_url):
    with open('mitre_details.txt', 'a') as file:
        file.write(f"URL: {url}\n")
        file.write(f"Tactic: {tactic}\n")
        file.write(f"Technique: {technique}\n")
        file.write(f"Technique URL: {technique_url}\n")
        file.write("-------------------\n")


def extract_mitre_links(url):
    # Fetch the HTML content of the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch content from {url}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check if the tab-mitre-details class is active
    tab_mitre_details_active = soup.find('li', class_='tab-mitre-details active')
    if tab_mitre_details_active is None:
        print("MITRE Details tab is not active")
        return []

    # Find the div with class "additional-link"
    additional_links_div = soup.find('div', class_='additional-link')
    if additional_links_div is None:
        print("No additional links found")
        return []

    # Find all links within the div
    links = additional_links_div.find_all('a')
    
    # Filter links that start with "attack.mitre.org"
    mitre_links = [link['href'] for link in links if link['href'].startswith("https://attack.mitre.org")]

    return mitre_links



# Function to search for MITRE details from page 1 to 60000
def search_mitre_details():
    base_url = "https://snort.org/rule-docs/1-"
    for page_number in range(1, 6): # 300841
        url = f"{base_url}{page_number}"
        mitre_details = extract_mitre_links(url)
        if mitre_details:
            if mitre_details == "MITRE Details found":
                print(f"MITRE Details found for {url}")
            else:
                for link in mitre_details:
                    print(f"Found MITRE link: {link}")

# Execute the search
search_mitre_details()



