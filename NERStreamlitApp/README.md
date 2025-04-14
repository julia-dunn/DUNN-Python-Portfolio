# NER App Project README

Welcome to the home page README for my Named Entity Recognition App project. This page is meant to provide insight into how to use my app, as well as how it was created and why.

### Contents:

- [Project Overview](##project-overview)
- [Instructions](##instructions)
- [App Features](##app-features)
- [References](##references)
- [Examples](##examples) 

## Project Overview

### Purpose:

The purpose of this project was to develop my skills both in creating named entity recognition software and in connecting my new skills with my knowledge in streamlit. By using streamlit to make a platform in which a user can interact with a custom entity ruler, I was forced to think from a user's perspective. This was especially important when it came to formatting, as well as potential uses. I needed to ensure users could create rulers with as many entity types, labels, and patterns as necessary for their text analysis. 

### spaCy Overview:

spaCy is a very specific dictionary which requires attention to detail, especially regarding formatting and syntax. In creating this NER app, the most challenging part was ensure text inputs aligned with the expected format for spaCy. A typical entity ruler follows this pattern:

```
{
    "label": "POS"
    "pattern": {"lower": word.lower()}
}
```

spaCy approaches Named Entity Recognition by using a dictionary of labels and patterns to analyze and match. By using the entity ruler, or dictionary of patterns, the program recognizes the entities, or key words, in a text and depicts their context. 

## Instructions 

Required Libraries:
- Streamlit
- Pandas
- spaCy

Installation Commands to run in Terminal:
```
{
    pip install streamlit
    pip install pandas
    pip install spacy
    python -m spacy download en_core_web_sm
}
```

Finally, to run the app locally, run in integrated terminal:
```
{
    streamlit run main.py
}
```

## App Features

Ability to upload text
- With this app, you can upload a local .txt file. 
- This allows for NER analysis of long format text, as opposed to only short format text which is typed directly into the app.

Ability to type/paste text
- With this app, you can also type into the textbox with custom texts. 
- This allows for quick analyisis of short phrases, without needing to create .txt files on your local device.

Ability to create an entity ruler with any number of patterns
- Because you can select the number of entities, you are not limited. If your dataset required 50 entities, that is technically possible. Or, if your dataset only needs 1, that is also possible.
- This allows for customization and flexibility depending on the size and complexity of the doc.

Ability to use multi-word patterns
- The patterns can be lists of objects of multiple words. For exaple, one pattern demonstrated below is labeled  "MUSICAL" and includes the patterns: ["An Evening with Mandy Patinkin", "Big Fish"]
- Allows for further customization
-Allows user to override preexisting entity rules

Visualizes Analyzed Text
- With the highlighted HTML visualization of the text, a user can easily see if the correct entities have been identified. 

Display of Entity Ruler Pattern
- Although collapsable, the app also visualizes the pattern such that the user can ensure they are testing for the correct labels and patterns. 

## References

- [Linked Headings](https://gist.github.com/rachelhyman/b1f109155c9dafffe618)
- [Code Markdown Syntax](https://www.markdownguide.org/extended-syntax/)
- [Standard Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
- [.strip() for error resolution](https://www.w3schools.com/python/ref_string_strip.asp)
- [Rendering with displacy](https://medium.com/@groxli/create-a-spacy-visualizer-with-streamlit-8b9b41b36745)
- [Iterating over dictionaries, "key=..."](https://realpython.com/iterate-through-dictionary-python/#swapping-keys-and-values-through-iteration)
- [spaCy Entity Ruler](https://spacy.io/api/entityruler)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)

## Examples

### Example 1: DPAC Advertisement

1. Input and Title Text

<img width="728" alt="Screenshot 2025-04-14 at 5 03 47 PM" src="https://github.com/user-attachments/assets/29d05ff9-7b98-4295-aced-97792efc08c2" />

2. Create Label and Pattern

<img width="728" alt="Screenshot 2025-04-14 at 5 04 08 PM" src="https://github.com/user-attachments/assets/6b5e1aae-02a5-4194-94ec-7c1ff31f0802" />

3. DataFrame of Entities

<img width="381" alt="Screenshot 2025-04-14 at 5 04 16 PM" src="https://github.com/user-attachments/assets/d28b3dc9-db93-4b3a-9346-8b3d44035b2c" />

4. DisplaCy Visualization of NER

<img width="736" alt="Screenshot 2025-04-14 at 5 04 24 PM" src="https://github.com/user-attachments/assets/3d6b7918-def1-49be-adf3-eba1ff90af95" />

### Example 2: My Introduction

1. Upload and Title Text

<img width="725" alt="Screenshot 2025-04-14 at 5 17 48 PM" src="https://github.com/user-attachments/assets/b1556e7b-34da-4c64-a90f-f7f57345beb5" />

2. Create Label and Pattern

<img width="724" alt="Screenshot 2025-04-14 at 5 17 59 PM" src="https://github.com/user-attachments/assets/033ef52b-0075-4f72-b2c6-8e2a06328b29" />

3. Dataframe of Entities

<img width="302" alt="Screenshot 2025-04-14 at 5 18 07 PM" src="https://github.com/user-attachments/assets/4d6fe527-e7d9-421c-9cec-deb06e2e4bc2" />

4. DisplaCy Visualization of NER

<img width="720" alt="Screenshot 2025-04-14 at 5 18 13 PM" src="https://github.com/user-attachments/assets/4f23e66b-4a95-4fdd-913b-3130fd4c00ce" />
