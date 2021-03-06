MBTI Classification
================================

In this project I go over the MBTI dataset in [Kaggle](https://www.kaggle.com/datasnaek/mbti-type) created by Mitchell J.

My goal is to analyze this dataset and see if a text classification model can determine each MBTI type just by looking at the person's posts in the Personality Cafe forum.

The process I follow is:
* **Problem Identification** – this step involves identifying the correct problem to solve and setting goals for your project. [PDF](https://github.com/DSJourney/MBTI/blob/master/reports/0.%20Problem%20Identification/Problem%20Identification%20-%20MBTI.pdf)


* **Data Wrangling** – this step involves the collection, organization, and definition of a dataset or datasets. [Notebook](https://nbviewer.jupyter.org/github/DSJourney/MBTI/blob/master/notebooks/1.%20Data%20Wrangling/MBTI_Data_Wrangling.ipynb)


* **Exploratory Data Analysis** – this step involves creating plots and charts to understand the relationship between data and the features of that data. [Notebook](https://nbviewer.jupyter.org/github/DSJourney/MBTI/blob/master/notebooks/2.%20EDA/MBTI_EDA_Clean.ipynb)

![Image of EDA](https://github.com/DSJourney/MBTI/blob/master/notebooks/2.%20EDA/Figures/countplot_types_comparison_population.png)


* **Feature Engineering & Pre-processing** – this step involves standardizing the dataset and creating features. Here you will find text preprocessing (tokenization, removing stopwords, stemming, etc.), the creating of part of speech tags, new features created with the textstat library, and perhaps more insteresting, the use of a Multinomial Naive Bayes model to determine the best predictive words for each MBTI attribute, the following word cloud is an output of that model. [Notebook](https://nbviewer.jupyter.org/github/DSJourney/MBTI/blob/master/notebooks/3.%20Feature%20Engineering%20and%20Pre-processing/Preprocessing.ipynb)

<p align="center"><img src="https://github.com/DSJourney/MBTI/blob/master/notebooks/3.%20Feature%20Engineering%20and%20Pre-processing/img/T_words_word_cloud.png" width="700"></p>


* **Modeling** – this involves selecting, training and deploying a model to make predictive insights. [Notebook](https://nbviewer.jupyter.org/github/DSJourney/MBTI/blob/master/notebooks/4.%20Modeling/Modeling_Results.ipynb)

<p align="center"><img src="https://github.com/DSJourney/MBTI/blob/master/notebooks/4.%20Modeling/img/Final_Models.png" width="700"></p>

* **Predicting** - this step involves taking unseen data and analysing it with our models created in the previous step. In this case I scraped some twitter profiles to find people who had their MBTI types in their bios and I extracted their tweets, which I then used to classify each person into a particular MBTI type. [Scraper](https://nbviewer.jupyter.org/github/DSJourney/MBTI/blob/master/notebooks/5.%20Predicting/Twitter_MBTI_Scraper.ipynb) and [Notebook](https://nbviewer.jupyter.org/github/DSJourney/MBTI/blob/master/notebooks/5.%20Predicting/Predicting.ipynb)

<p align="center"><img src="https://github.com/DSJourney/MBTI/blob/master/notebooks/5.%20Predicting/img/length_tweet_corpus_vs_correct_guesses.png" width="700"></p>


* **Documentation** – this involves documenting the work you’ve done and sharing your findings. [Presentation](https://github.com/DSJourney/MBTI/blob/master/reports/2.%20Final%20Report/MBTI_Final_Presentation.pdf)

<a href="https://github.com/DSJourney/MBTI/blob/master/reports/2.%20Final%20Report/MBTI_Final_Presentation.pdf"><p align="center"><img src="https://github.com/DSJourney/MBTI/blob/master/reports/2.%20Final%20Report/Cover_Image_for_README.png" width="700"></p></a>
