# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
filepath = 'Dataset/Restaurant Reviews.tsv'

# Parameters
# "delimiter" specifies that we're importing a .tsv file
# "quoting" to avoid problems with double-quotes, we're ignoring double-quotes
dataset = pd.read_csv(filepath, delimiter = '\t', quoting = 3)
