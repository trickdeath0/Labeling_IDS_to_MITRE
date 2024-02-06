import requests
import json
from bs4 import BeautifulSoup
import csv
import os

URL = "https://attack.mitre.org/tactics/enterprise/"

techniques_ID = ""


def get_techniques(url, output_folder, tactic_name):
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
                description = cells[2].text.strip().split(".")[0]
            else:
                ID = techniques_ID + cells[1].text.strip()
                name = cells[2].text.strip()
                description = cells[3].text.strip().split(".")[0]
            techniques.append((ID, name, description))
            #print(f"finish id: {ID}")

        # Write data to CSV
        with open(f"{output_folder}/{tactic_name}.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Technique Name", "Description"])
            writer.writerows(techniques)
    else:
        print("Techniques section not found. Check if the page structure has changed.")


def split_and_write_json(data, max_chars, output_folder, output_filename_prefix):
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
            output_filename = f"{output_folder}/{output_filename_prefix}_{current_part}.json"
            with open(output_filename, "w", encoding="utf-8") as fp:
                fp.write("The information:\n")
                json.dump(current_data, fp, indent=4)
            output_files.append(output_filename)

            current_chars = 0
            current_part += 1
            current_data = {}

    # Write the remaining data to the last file
    if current_data:
        output_filename = f"{output_folder}/{output_filename_prefix}_{current_part}.json"
        with open(output_filename, "w", encoding="utf-8") as fp:
            fp.write("The information:\n")
            json.dump(current_data, fp, indent=4)
        output_files.append(output_filename)

    return output_files


def convertToJSON(output_folder, tactic_name):
    '''
    Converts the CSV file to a JSON file
    '''
    dictOfTechs = {}
    with open(f"{output_folder}/{tactic_name}.csv", "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        # Skip header row
        next(reader)
        for row in reader:
            dictOfTechs[row[0]] = (row[1], row[2])

    output_files = split_and_write_json(dictOfTechs, 3100, output_folder, f"{tactic_name}_part")



if "__main__" == __name__:
    output_folder = "Extract data from MITRE ATTACK"
    os.makedirs(output_folder, exist_ok=True)

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    technique_section = soup.find("table", class_="table table-bordered table-alternate mt-2")

    for row in technique_section.find_all("tr")[1:]:
        cells = row.find_all("td")
        tactic_name = cells[1].text.strip()
        tactics_url = URL[:-20] + cells[1].a['href']
        #print(tactic_name)
        #print(tactics_url)
        tactic_folder = output_folder + "\\" + tactic_name
        os.makedirs(tactic_folder, exist_ok=True)
        get_techniques(tactics_url, tactic_folder, tactic_name)
        convertToJSON(tactic_folder, tactic_name)
