# Bee Species Identification
To predict the species of a bee, given its description in text format, using Information Retrieval, Natural Language Processing and Machine Learning.

Deployed app: [bees-identifier.herokuapp.com](https://bees-identifier.herokuapp.com/)

### Local Deployment
1. Clone the git repository.
2. Change directory to `Code` and create a virtual environment.
3. Activate the virtual environment
```
source env/bin/activate
```
4. Install dependencies using `requirements.txt`
```
pip install -r requirements.txt
```
5. Start the application
```
flask run
```
6. Go to the local host server and use the app!

### File Structure
```
.
│--Code 
|  |--templates
|  |  |--index.html
|  |--static
|  |  |--loader.gif
|  |  |--svg.png 
|  |--app.py
│  |--Procfile
|  |--app.py
|  |--bees.ipynb
|  |--bees.py
|  |--dataset bees.txt
|  |--nltk.txt
|  |--readme.txt
|  |--requirements.txt
|--Documents
│  │--Poster: Automatic Bee Species Identification
│  │--Report: Automatic Bee Species Identification
│  │--readme.txt
|--README.md
```

Detailed report can be viewed here: `Documents/Report - Automatic Bee Species Identification.pdf`

## Introduction

There are over 20,000 known species of bees, however many species possess similar characteristics which can make the task of bee identification/taxonomy difficult. For example, almost all of the species of honey bees have varying dark and light striations. In the recent few years, many species of bees have been enlisted as endangered, so it has become important to correctly classify bees to enable proper surveying and studying. But, due to such a large number of known species, it is infeasible to manually identify and classify all the bees, based on their physical traits. 

To overcome this challenge, we have created an automated bee identification system. We have employed Information Retrieval, Natural Language Processing and Machine Learning techniques to automate this process. Using a list of features as queries/inputs, we aim to predict the species of the bee.

## Methodology
jupyter notebook: `Code/bees.ipynb`  
### 1. Dataset Creation

We scraped and collected data from several websites, research papers, field guides, books and articles. We also implemented Image to Text conversion methods to extract text from older editions of books. After compiling all the resources the title i.e. the name of the species and the description of the species were separated. We eventually prepared a sample dataset containing 102 species of bees and their detailed description in order to create the algorithm and validate it using those samples. 

Data can be found at: `Code/dataset bees.txt`

### 2. Dataset Preprocessing

The obtained text descriptions of the species were then preprocessed using the following steps:

1. Tokenization: the string containing the text was broken down into smaller strings by the space character (' ') and the obtained description was stored in an array.  
2. Lower casing: the words in the array were then converted to the lowercase in order to maintain uniformity among the words. For instance, “NorthWestern”, “Northwestern”, and “northwestern”. 
3. Removal of extra spaces: the extra space between words were removed to avoid in subsequent processes.
4. Removal of stop-words: irrelevant words which do not add to the meaning of the sentence (such as: the, a, then, etc.) were removed so that only the meaningful keywords remain in the dataset.
5. Lemmatization: the remaining words were then converted to their root form.

### 3. Ranks Prediction

In order to create a predicted rank list, we applied three ranking algorithms to the list of queries and merged them all into one, to finally return the top 15 most likely species. The three rank lists are individually made by raw TF-IDF extraction, binary TF-IDF extraction and log-normalized TF-IDF extraction.


### 4. Machine Learning Models
We trained 6 models which had the species of the bees in the form of one hot encoded classes as the ‘y’, and the vectorised description of the species as ‘x’. We then trained:
- Naive Bayes
- Support Vector Machine with 'linear' kernel and degree 3
- Random Forest
- K-Nearest Neighbors
- Logistic Regression 
- Neural Network model with maximum iterations = 500,

with the above mentioned dataset. The test query text was a sequence of random words along with some words from the description of the species in a jumbled fashion. 

## Results
The accuracies obtained by the machine learning models were : 

Model | Accuracy
--- | ---                 
Multinomial Naive Bayes  | 77.78 | Content Cell
SVM Classifier |  77.78
Random Forest Classifier |  55.56
KNN Classifier | 11.12
Logistic Regressor | 88.89
MLP Classifier | 77.78

## References
```
[1] B. Armouty and S. Tedmori. ‘Automated keyword extraction using support vector machine from Arabic news documents’. In: 2019 IEEE Jordan International Joint Conference on Electrical Engineering and Information Technology (JEEIT). IEEE. 2019, pp. 342–346.
[2] C. Bingham. ‘The Fauna of British India, Including Ceylon and Burma. Hymenoptera-Vol.1. Wasps and Bees.’ In: (1897).
[3] S. Bob. HYMENOPTERA Bees, Wasps, Sawflies &; Ants. May 2014, bobs-bugs.info/2014/01/02/hymenoptera-bees-wasps-ants-etc.
[4] S. Kincaid. Common Bee Pollinators of Oregon Crops. 2017, oregon.gov
[5] C. D. Michener. The bees of the world. Vol. 1. JHU press, 2000.
[6] J. Ramos et al. ‘Using tf-idf to determine word relevance in document queries’. In: Proceedings of the first instructional conference on machine learning. Vol. 242. 1. Citeseer. 2003, pp. 29–48.
[7] About Bees, https://idtools.org/id/bees/exotic/bees classification.php.
[8] Alper. NLP: Classification and Recommendation Project. July 2020, towardsdatascience.com/nlp-classification-recommendation-project-cae5623ccaae.
[9] Palaearctic Osmiine Bees, blogs.ethz.ch/osmiini/phylogeny-and-classification.
[10] The Most Beneficial Types of Bees (With Identification Guide and Pictures). Apr. 2021, leafyplace.com/types-of-bees.
[11] Wood Wasps and Sawflies, amentsoc.org/insects/fact- files/orders/hymenoptera-symphyta.html.
```
