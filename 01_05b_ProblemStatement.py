# Part - 1

text = 'Ram goes to college everyday by car.'

# Importing spacy and getting all attributes.

nlp = English()

# Creating doc object

doc = nlp(text)

for token in doc:
  
  # Getting token’s text, part of speech tags and dependency labels
  
  token_text = token.text # Getting the corresponding text
  
  token_dep = token.dep_ # Getting the Dependency label
  
  token_pos = token.pos_ # Getting the POS Tag

  # Printing entities text and label attributes
  
  print(token_text, token_dep, token_pos)


# Part - 2

text = 'Ram goes to college everyday by car.'

# Importing spacy and getting all attributes.

nlp = English()

doc = nlp(text)

for token in doc:
  
  # Printing the entity text and label
  
  print(entity.text, entity.label_)
