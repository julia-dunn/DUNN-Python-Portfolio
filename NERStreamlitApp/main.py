import streamlit as st
import pandas as pd

st.title("Named Entity Recognition (NER) App")
st.write("This app uses a custom entity ruler to analyze any piece of text you may need! This could be anything from a short text/tweet to a chapter of a book! First, let's create your customer ruler!")

import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.pipeline import EntityRuler

patterns = []

st.write("To create an entity ruler, first input the name of your text and create your first entity pattern.")
title = st.text_input("Name of Text")
uploaded_file = st.file_uploader("Upload Text (in .txt format):", type="txt")
st.write("First Entity:")
label1 = st.text_input("Label:")
num_objects1 = st.number_input(f"Number of words in pattern for {label1}:", min_value=1, step=1)
pattern1 = []
for i in range(int(num_objects1)):
    word = st.text_input(f"Word {i+1}:", key=f"first_word_{i}")
    pattern1.append({"text": word})

patterns.append({'label': label1, 'pattern': pattern1})

st.write("Additional Entities:")
num_entities = st.number_input("Number of additional entity types:", min_value=0,step=1)
for i in range(int(num_entities)):
    label = st.text_input(f"Label {i+2}:")
    num_words = st.number_input(f"Number of words in pattern for {label}", min_value=1, step=1, key=f"num_words_{i}")

    pattern = []
    for j in range(int(num_words)):
        word = st.text_input(f"Word {j+1} for {label}:", key=f"word_{i}_{j}")
        pattern.append({"text": word})
    patterns.append({'label': label, "pattern": pattern})
st.write("Generated Patterns:")
st.json(patterns)

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    doc = nlp(text)

entities_doc = []
for ent in doc.ents:
    entities_doc.append({
        'text': ent.text,
        'label': ent.label
    })
ent_df = pd.DataFrame(entities_doc)
ent_df