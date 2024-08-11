import requests
import json
from bs4 import BeautifulSoup
import csv
import os

URL = "https://attack.mitre.org/techniques/enterprise/"
URL2 = "https://attack.mitre.org/techniques/"

techniques_ID = ""


def get_full_techniques_description(URL_full):
    """
    Get technique description from MITRE's ATT&CK website.
    :param url: The URL of the page to scrape.
    """
    response_full = requests.get(URL_full + "/")

    # Parse the HTML content
    soup = BeautifulSoup(response_full.content, "html.parser")

    # Find the section containing the techniques
    techniques_description = soup.find("div", class_="description-body")

    return techniques_description.text.strip()


def get_techniques(url, output_folder):
    """
    Get technique data from MITRE's ATT&CK website.
    :param url: The URL of the page to scrape.
    """
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the section containing the techniques
    techniques_section = soup.find("table", class_="table-techniques")

    # Check if techniques_section exists
    if techniques_section:
        # Extract technique names and descriptions
        techniques = []
        for row in techniques_section.find_all("tr")[1:]:  # Skip the header row
            cells = row.find_all("td")
            if len(cells) == 3:
                techniques_ID = cells[0].text.strip()
                ID = techniques_ID
                name = cells[1].text.strip()
                URL_full = URL2 + ID
                description = get_full_techniques_description(URL_full)
            else:
                ID = techniques_ID + cells[1].text.strip()
                name = cells[2].text.strip()
                URL_full = URL2 + techniques_ID +"/" + cells[1].text.strip()[1:]
                description = get_full_techniques_description(URL_full)
            techniques.append((ID, name, description))
            #print(f"finish id: {ID}")

        # Write data to CSV
        with open(f"{output_folder}/mitre_attack_enterprise_full.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Technique Name", "Description"])
            writer.writerows(techniques)
    else:
        print("Techniques section not found. Check if the page structure has changed.")



if "__main__" == __name__:
    output_folder = "Pre fine tuning DB"
    os.makedirs(output_folder, exist_ok=True)

    get_techniques(URL, output_folder)

