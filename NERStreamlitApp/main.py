# import dictionaries for basic streamlit app
import streamlit as st
import pandas as pd

# introduce app and create name
st.title("Named Entity Recognition (NER) App")
st.write("This app uses a custom entity ruler to analyze any piece of text you may need! This could be anything from a short text/tweet to a chapter of a book! First, let's create your customer ruler!")

# import dictionaries for NER
import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.pipeline import EntityRuler
from spacy import displacy

patterns = [] # initialize empty list of patters

# introduce structure, initialize by uploading/pasting the text
st.markdown("#### First, you need to input your text!")
title = st.text_input("Name of Text:")
uploaded_file = st.file_uploader("Upload Text (in .txt format):", type="txt")
input_text = st.text_input("Or, write your own text here!")

st.markdown("#### Now, let's create your patterns.")
num_entities = st.number_input("Number of entity types:", min_value=1, step=1) # establish number of entities in total patterns
for i in range(int(num_entities)): # iterate over number of patterns/entity types (custom number of entities)
    st.markdown(f"##### Pattern {i+1}") # distinguish between patterns, each entity type separated by header
    label = st.text_input(f"Label {i+1}") # create label for i+1 entity type
    num_words = st.number_input(f"Number of words in pattern for {label}", min_value=1, step=1, key=f"num_words_{i}") # establish number of words within each entity pattern

    for j in range(int(num_words)): # iterate over number of words
        word=st.text_input(f"Word {j+1} for {label}:", key=f"word_{i}_{j}") # input each word within pattern
        if word: # resolves error if no word has been inputted yet
            words=word.lower().split() # splits the input if there are multiple words, removes case sensitivity
            indv_pattern=[{"lower": w} for w in words] # creates individual pattern for text input such that it is a list of each individual word
            patterns.append({"label": label, "pattern": indv_pattern}) # adds custom patterns of all of the lists of words for this entity type to list of all patterns

if "entity_ruler" not in nlp.pipe_names:
    my_ruler = nlp.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True}) # intialize entity ruler, complete before the established EntityRuler such that custom labels report when contradicting initial labels
else:
    ruler = nlp.get_pipe("entity_ruler")

my_ruler.add_patterns(patterns) # add list of patterns to initialized ruler

# use if else loop so that there is not an error when a no file has been uploaded/pasted yet (provides options between upload and typing text)
if uploaded_file: # if something has been uploaed via st.file_uploader...
    text1 = uploaded_file.read().decode("utf-8") # use plain text decoder according to my Finder to change .txt file into text
    doc1 = nlp(text1) # make spacy doc from spacy text
    entities_doc1 = [] # create empty list of entities
# entity ruler analysis for uploaded file
    entities_doc1 = [] # create empty list of entities
    for ent in doc1.ents: # iterate over recognized entities in the doc, adding labeled entities to originally empty list
        entities_doc1.append({
            'text': ent.text,
            'label': ent.label_
        })

    ent_df1 = pd.DataFrame(entities_doc1) # create dataframe of entities with their labels
    ent_df1 # display dataframe in streamlit app

## visualization for uploaded file
    html = displacy.render(doc1, style = "ent")
    st.write("Diplay of Annotated Text")
    st.markdown(html, unsafe_allow_html=True)

# by repeating for ent in doc.ents loop, as well as df and display.render, one can analyze both an uploaded text and an inputted text with the same entity ruler at the same time
# otherwise, the input text would replace the uploaded file text
if input_text: # if instead text has been typed into text input
    text2 = input_text # name input text as "text" for nlp conversion into doc
    doc2 = nlp(text2) # create spacy doc with spacy text
## entity ruler analysis for inputted text
    entities_doc2 = [] # create empty list of entities 
    for ent in doc2.ents: # iterate over recognized entities inthe doc, adding labeled entities to original empty list
        entities_doc2.append({
            'text': ent.text,
            'label': ent.label_
        })
    
    ent_df2 = pd.DataFrame(entities_doc2) # create dataframe of entities with their labels
    ent_df2 # display dataframe in streamlit

## visualization for inputted text
    html = displacy.render(doc2, style="ent")
    st.write(f"Display of Annotated Text: {title}")
    st.markdown(html, unsafe_allow_html=True)
else:
    text = "No Text Inputted"
    doc = nlp(text)

# write into streamlit the sample texts which can be copied/pasted into the text input
st.markdown("#### Sample Texts!")
st.write("Here are some interesting example texts you could test out!")
# distinguish between texts with markdown headers
st.markdown("##### Text 1: School Subjects")
st.write("In the United States education system, topics are split up into school subjects. My favorite subject is science, because I can learn more about the world with hands on experimentation. My best friend's favorite subject is art, because she is really good at drawing. She uses pencils, paint, and clay. It can be hard to choose a favorite school subject, because they are all so interesting. What is yours?")
st.markdown("###### Possible Patterns to Create:")
# use markdown syntax to create  unordered list
st.markdown("""
            - **Label** SUBJ, **Words:** science, english, math, art, history
            - **Label** SUPPLIES, **Words:** pencils, paint, clay
            """)

st.markdown("##### Text 2: My Introduction")
st.write("My name is Julia Dunn. I am a physics major at the University of Notre Dame, originally from Connecticut, where I attended Glastonbury High School. The weather in Indiana is different from what I am used to. Today, it was cool but sunny. In my physics class today, we discussed the different wavelengths of light and how they relate to color. My favorite color is green. However, the color of the highest energy is purple. This is because it has a high frequency and a low wavelength.")
st.markdown("###### Possible Patterns to Create:")
st.markdown("""
            - **Label**: COLOR, **Words**: red, orange, yellow, green, blue, purple
            - **Label**: PHYS, **Words**: energy, frequency, wavelength, light
            - **Label**: SCHOOL, **Words**: University of Notre Dame, Glastonbury High School
            """)

st.markdown("##### Text 3: DPAC Advertisement")
st.write("At the Debartolo Performing Arts Center, we put on many different types of shows. We have kids movies, such as Alice in Wonderland and Annie. We have musicals, such as Big Fish and An Evening with Mandy Patinkin. We have concerts, such as the South Bend Symphony Orchestra and the Notre Dame Winds and Band. The next show is Jesus Christ Superstar on Thursday, April 17th.")
st.markdown("###### Possible Patterns to Create")
st.markdown("""
            - **Label**: PERFTYPE, **Words**: movies, musicals, concerts
            - **Label**: MOVIE, **Words**: Alice in Wonderland, Annie, Jesus Christ Superstar
            - **Label**: MUSICAL, **Words**: Big Fish, An Evening with Mandy Patinking
            - **Label**: CONCERT, **Words**: South Bend Symphony Orchestra, Notre Dame Winds and Band
            """)