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


## Instructions 

## App Features

## References

- [Linked Headings](https://gist.github.com/rachelhyman/b1f109155c9dafffe618)
- [Code Markdown Syntax](https://www.markdownguide.org/extended-syntax/)
- [Standard Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
- [.strip() for error resolution](https://www.w3schools.com/python/ref_string_strip.asp)
- [Rendering with displacy](https://medium.com/@groxli/create-a-spacy-visualizer-with-streamlit-8b9b41b36745)

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

2. Create Label and Pattern

3. Dataframe of Entities

4. DisplaCy Visualization of NER
