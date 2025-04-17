# Ashtavakra Gita

##  Summary

This script extracts verses from the Ashtavakra Gita text available online. Here's what it does, step by step:

1. It downloads the text file from the GRETIL website using the provided URL.

2. It looks for the section in the file where the actual content starts, right after the line that says `# Text`.

3. It searches through the content and finds verses using a regular expressions pattern. (We use unicode strings since the verse contain Sanskrit characters). Each verse is expected to have two lines, followed by `//` and a verse number like `Avg_1.1`.

4. Each matched verse is saved in a list along with its index.

5. After collecting the verses, the script removes them from the original content by storing their start and stop indices, so we’re left with only the unmatched or extra parts of the text.

6. Finally, it saves the extracted verses to a file called `verses.json`, and the leftover content to `remaining_content.txt` for reference. (Again we save it in UTF-8 because of Sanskrit characters)
