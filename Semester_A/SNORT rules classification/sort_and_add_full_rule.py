# Read the URLs from the file
with open("url_links.txt", "r") as file:
    urls = file.readlines()

# Remove duplicates
unique_urls = list(set(urls))

# Define a sorting key function
def custom_sort_key(url):
    if "1-" in url:
        # For URLs with "1-XX" format, extract the number and sort numerically
        return (0, int(url.split("1-")[1]))
    else:
        # For other URLs, put them after the ones with "1-XX" format
        return (1, url)

# Sort the URLs
unique_urls.sort(key=custom_sort_key)


# Read Snort rules from the second file
with open("SNORT rules classification\snort3-community.rules", "r") as file:
    snort_rules = file.readlines()


# Combine URLs and Snort rules into tuples
for url in unique_urls:
    ruleId = url.split("-")[1].split("\n")[0]
    for sid in snort_rules:
        if ruleId in sid:
            with open("SNORT rules classification/sorted_urls.txt", "a") as file:
                file.write(f"{url.strip()}, {sid.strip()}\n")
            break



        # with open("SNORT rules classification/sorted_urls.txt", "w") as file:
        #     file.write(f"{unique_urls.strip()}, {sid.strip()}\n")



# # Combine URLs and Snort rules into tuples
# data = list(zip(unique_urls, snort_rules))

# # Sort the data based on URL and rule
# data.sort(key=lambda x: (x[0], x[1]))

# # Write the sorted data back to a file
# with open("SNORT rules classification/sorted_urls.txt", "w") as file:
#     for url, rule in data:
#         file.write(f"{url.strip()}, {rule.strip()}\n")
