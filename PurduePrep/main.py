# Classes:
# Page {url, body(extracted info from scrape)}
# Question {url from page, question body}


# Step 0: Initialize the website?
# This is handled in app.py

# Step 1: Retrieve input from the user (text, pdf, or image)
def get_saved_text():
    try:
        with open('input_text.txt', 'r') as fp:
            input_text = fp.read()
            return input_text
    except FileNotFoundError:
        return None


# UI handler ---(input)---> Input handler
# Step 2: Input handler processes input and formats as we need it


# Input handler ---(string)---> Querry builder
# Step 3: Querry builder processes all user's gibberish, extracts relevant info, forms querry string


# Querry builder ---(querry string)---> Web crawler
# Step 4: Web crawler uses the querry string to produce a list of relevant websites


# Web crawler ---(relevant sites list)---> Scraper
# Step 6: Web scraper extracts information from websites


# Web scraper ---(extracted text)---> Question ID
# Step 7: Use NLP to identify questions


# Question ID ---(question objects)---> Relevance checker
# Step 8: Question objects go to relevance checker to be evaluated for content

# Relevance checker ---(list of question objects)---> Output handler
# Step 9: Output handler loops through list of question objects and packages to the website

# Output handler ---(output)---> Website

if __name__ == '__main__':
    input_text = get_saved_text()
    if input_text:
        print(f"Processing the input text: {input_text}")
    else:
        print("No text available")