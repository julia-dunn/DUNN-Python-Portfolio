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
![First step of NER](NERStreamlitApp/Screenshot 2025-04-14 at 5.03.47 PM.png)
2. Create Label and Pattern
![Second step of NER](NERStreamlitApp/Screenshot 2025-04-14 at 5.04.08 PM.png)
3. DataFrame of Entities
![Dataframe of Entities](NERStreamlitApp/Screenshot 2025-04-14 at 5.04.16 PM.png)
4. DisplaCy Visualization of NER
![Visualization](NERStreamlitApp/Screenshot 2025-04-14 at 5.04.24 PM.png)