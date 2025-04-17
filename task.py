import requests
import re
import json

# Downloading Text
url = "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_aSTAvakragItA.txt"
response = requests.get(url)

if response.status_code != 200:
    raise Exception("Unable to Download File")

data = response.text

# We need to extract all the data after # Text
_, content = data.split("# Text", 1)
content = content.strip()

# Extracting the pattern we want using regular expressions
verse_pattern = re.compile(r"(.+?)\n(.+?)\s+//\s+Avg_(\d+\.\d+)", re.UNICODE)

# Getting the verses as well as the verse indices to later remove from our main data
verses = []
spans_to_remove = []

for match in verse_pattern.finditer(content):
    line1, line2, index = match.groups()
    full_verse = f"{line1.strip()}\n{line2.strip()}"
    verses.append({"verse": full_verse, "index": index})    
    spans_to_remove.append((match.start(), match.end()))

# Subtracting the verses from the main content to get the remaining content
rem_content = content 
for start, end in reversed(spans_to_remove):
    rem_content = rem_content[:start] + rem_content[end:]
rem_content = rem_content.strip()


# Save verses to JSON
with open("verses.json", "w", encoding="utf-8") as f:
    json.dump(verses, f, ensure_ascii=False, indent=2)

# Save remaining content in case we missed any data to another txt file
with open("remaining_content.txt", "w", encoding="utf-8") as f:
    f.write(rem_content)