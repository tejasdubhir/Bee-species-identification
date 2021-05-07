# Bee-species-identification
Predicting the species of bees, given a physical description in words. 


#**Introduction**:

Bees are insects that play a significant role in the pollination of food crops and the production of honey and wax. Because of this, they are considered a crucial ecological and economic resource.However, many species possess similar characteristics which can make the task of bee identification or bee taxonomy difficult. For example, almost all of the species of honey bees have varying dark and light striations. Bumblebees also have black and yellow stripes but are often larger than honey bees.Unfortunately, many species of bees are now enlisted as ‘endangered. Many scientists believe this is due to various agricultural practices and the use of insecticides. Thus, in the past few years, it has become important to correctly classify bees as it would help in their proper surveying, studying and monitoring. But, due to such a large number of known species, it is infeasible to manually identify and classify all the bees, based on their physical traits. 
To overcome this challenge, we have created an automated bee identification system. We have employed Information Retrieval, Natural Language Processing and Machine Learning techniques to automate this process. Using a list of features as queries/inputs, we aim to predict the species of the bee.

#**Dataset creation**:

We first scraped and collected data from several websites, research papers, field guides, books and articles and tried to separate the species description from the titles and created a dataset.
We also implemented Image to Text conversion methods using python’s cv2 library (pytesseract) to extract text from older editions of books, for which a text format was not available. One book that we used majorly for the extraction of data was ‘The Bees of the World’ (Second Edition) by Charles D. Michener. We first converted the pages of the PDF to image and then extracted the text.

After compiling all the resources the format of the dataset was decided - the title i.e. the name of the species followed by the description of the species containing the physical characteristics of the bees which would then be compared with the input query text. This step took most of the time as the number of bees species available is around 20,000 and manually collecting such a large amount of data was a tedious event. 

We eventually prepared a sample dataset containing 102 species of bees and their detailed description in order to create the algorithm and validate it using those samples. 


#**Dataset Preprocessing:**

The obtained text descriptions of the species were then preprocessed using the following steps:

Tokenization: the string containing the text was broken down into smaller strings by the space character (‘ ‘). Then the obtained description was stored in an array.  

Lower casing: the words in the array were then converted to the lowercase in order to maintain uniformity among the words which were the same but differed in their capitalisation. For instance, “NorthWestern”, “Northwestern”, and “northwestern”. 

Remove extra spaces: the extra space between words needed to be removed as it could have led to confusion in subsequent processes (ex: whether the white space character is a part of the word or not). We felt that this could also later help us in bi-gram indexing, which is a future aspect of this project.

Remove stop-words: irrelevant words which do not add to the meaning of the sentence (such as: the, a, then, etc.) had to be removed so that only the meaningful keywords remain in the dataset. 

Lemmatization: the remaining words were then converted to their root form. This means that words like ‘pollinated’, and  ‘pollinating’ were represented by one word - ‘pollinate’ - and hence were considered the same.


#**Ranks Prediction:**

In order to create a predicted rank list, we applied three ranking algorithms to the list of queries and merged them all into one, to finally return the top 15 most likely species. The three rank lists are individually made by raw TF-IDF extraction, binary TF-IDF extraction and log-normalized TF-IDF extraction.

