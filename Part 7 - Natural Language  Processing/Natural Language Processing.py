# Natural Language Processing

# Step 1 - Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Step 2 - Importing the dataset

filepath = 'Dataset/Restaurant Reviews.tsv'

# We need to add some additional parameters to specify that we are importing .tsv file
# "delimiter" specifies that we're importing a .tsv file
# "quoting" to avoid problems with double-quotes, we're ignoring double-quotes. It's not compulsory, but good to do to make sure everything works properly.
dataset = pd.read_csv(filepath, delimiter = '\t', quoting = 3)

# Step 3 - Cleaning the texts

# This is compulosry step in Natural Language Processing which consists of cleaning the text to make it ready for future machine learning algorithms
# "re" library has some great tools to clean some texts effeciently 
import re
import nltk

# "stopwords" is a packacge (contains a list of words) which contains all the words that are generically irrelevant in a review or any text you know to predict 
# the category in which to review or that text belongs
nltk.download('stopwords')

# Importing "stopwords" package
from nltk.corpus import stopwords

# Importing "PorterStemmer" class
from nltk.stem.porter import PorterStemmer

# 1.
# 1st parameter - Only keeping the letters from a to z whether it's capital or not
# 2nd parameter - Adding an space in between after removing non-significant characters
review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0])

# 2. Convert all the uppercase letters to lowercase
review = review.lower()

# 3. Remove non-significant/irrelevant words (i.e., articles, prepositions)

# Split the "review" string into individual words
review = review.split()

# 4. Stemming - Only keeping the root of the different words to simplify the review even more. If we keep all the different versions of the same word that 
# means the same thing. Well, the problem is that in the end in our process in our sparse matrix we'll have tons of words and therefore huge sparsity and 
# therefore our algorithm will have trouble to run as we'll simply have too many columns. In the sparse matrix each word will have its own column. 
# Example: "loved", "loving" come from the same root word "love"
# Creating an object of "PorterStemmer" class
porterStemmer = PorterStemmer()

# 5. Since "stopwords" is a package containing different lists of words in different languages. Here's the reviews are in English we need to make it easier 
# for our program by telling it to only look at the English words and to specify this we need to explicitly mention it
review = [porterStemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]

# 6. Joining back different words of this review list separated by a space
review = ' '.join(review)