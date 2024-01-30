import requests
import json
from bs4 import BeautifulSoup
import csv
import os

URL = "https://attack.mitre.org/techniques/enterprise/"

techniques_ID = ""

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
                description = cells[2].text.strip()
            else:
                ID = techniques_ID + cells[1].text.strip()
                name = cells[2].text.strip()
                description = cells[3].text.strip()
            techniques.append((ID, name, description))

        # Write data to CSV
        with open(f"{output_folder}/mitre_attack_enterprise.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Technique Name", "Description"])
            writer.writerows(techniques)
    else:
        print("Techniques section not found. Check if the page structure has changed.")



if "__main__" == __name__:
    output_folder = "Pre fine tuning DB"
    os.makedirs(output_folder, exist_ok=True)

    get_techniques(URL, output_folder)

