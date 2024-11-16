import re
import os

# Define the folder containing the text files
folder_path = 'course_material'  # Make sure this is the path to your folder

# Define keywords for excluding self-promotional or personal references
exclusion_keywords = [
    'subscribe', 'youtube', 'channel', 'like this video', 'show some love', 
    'comment', 'share this video', 'hit the bell', 'link', 'download', 
    'great learning'
]

# Compile a regex pattern to match any exclusion keywords (case-insensitive)
pattern = re.compile('|'.join(re.escape(keyword) for keyword in exclusion_keywords), re.IGNORECASE)

# Process each .txt file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(folder_path, filename)
        output_file_path = os.path.join(folder_path, f"cleaned_{filename}")
        
        # Open the input file, filter lines, and write to the output file
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
            for line in infile:
                # Write the line to the output file if it doesn't contain any exclusion keywords
                if not pattern.search(line):
                    outfile.write(line)
        
        print(f"File '{filename}' has been cleaned and saved as 'cleaned_{filename}'")
