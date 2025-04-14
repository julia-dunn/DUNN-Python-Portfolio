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

## Examples
