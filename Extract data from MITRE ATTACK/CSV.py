import requests
import json
from bs4 import BeautifulSoup
import csv

URL = "https://attack.mitre.org/techniques/enterprise/"


def get_techniques(url):
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
            ID = cells[0].text.strip()
            name = cells[1].text.strip()
            description = cells[2].text.strip().split(".")[0]
            if str(name).startswith(".0"):
                continue
            techniques.append((ID,name, description))

        # Write data to CSV
        with open("mitre_attack.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Technique Name", "Description"])
            writer.writerows(techniques)
    else:
        print("Techniques section not found. Check if the page structure has changed.")


def split_and_write_json(data, max_chars, output_filename_prefix):
    """
    Split a dictionary into multiple JSON files.
    :param data: The dictionary to split.
    """
    output_files = []
    current_chars = 0
    current_part = 1
    current_data = {}

    for key, value in data.items():
        current_chars += len(json.dumps({key: value}))
        current_data[key] = value

        if current_chars >= max_chars:
            output_filename = f"{output_filename_prefix}_{current_part}.json"
            with open(output_filename, "w", encoding="utf-8") as fp:
                json.dump(current_data, fp, indent=4)
            output_files.append(output_filename)

            current_chars = 0
            current_part += 1
            current_data = {}

    # Write the remaining data to the last file
    if current_data:
        output_filename = f"{output_filename_prefix}_{current_part}.json"
        with open(output_filename, "w", encoding="utf-8") as fp:
            json.dump(current_data, fp, indent=4)
        output_files.append(output_filename)

    return output_files


def convertToJSON():
    '''
    Converts the CSV file to a JSON file
    '''
    dictOfTechs = {}
    with open("mitre_attack.csv", "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        # Skip header row
        next(reader)
        for row in reader:
            dictOfTechs[row[0]] = (row[1], row[2])

    output_files = split_and_write_json(dictOfTechs, 3000, "mitre_attack_split")


if "__main__" == __name__:
    get_techniques(URL)
    convertToJSON()
