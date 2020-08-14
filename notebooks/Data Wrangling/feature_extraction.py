import numpy as np
import string


class Feature_Extraction:
    """A simple class to extract data from the MBTI Dataset"""
    
    def __init__(self, df, target='type', posts='posts'):
        self.df = df
        self.target = target
        self.posts = posts

    def dummies_types(self, column='type', drop_first=True):
        """Extracts the individual attributes as dummy variables from the type column
            - column: takes the column name you want to analyze (default is 'type')
            - drop_first: If False will return all the dummy variables, if True (default) it will erase Extraversion, Sensing, Feeling, Perceiving since they are the opposite extremes of I N T J
        returns the dataframe
        """
        df_dummies = self.df[column].str.get_dummies('')
        if drop_first == True:
            df_dummies = df_dummies.drop(['E','S','F','P'], axis=1)
        self.df = self.df.join(df_dummies)
        return self.df
    
    @staticmethod # I made this one to practice with a staticmethod
    def posts_len(df, column='posts', new_col_name='posts_len'):
        """Will create a new column with the length of all the posts gathered.
        It is a static method so it takes:
            - the dataframe since it is a staticmethod
            - the column we want to count the lenght of (by default is the "posts" column)
            - the name of the new column (by defaul "posts_len")
        """
        df[new_col_name] = df[column].str.len()

    def split_posts(self, column='posts', separator='|||', new_col_name='posts_separated', count_posts=True):
        """Will generate a new column with the posts separated.
            - column: is the column we want to separate (by defaul 'posts')
            - separator: is the condition we want to separate on  (by default '|||')
            - new_col_name: is the name of the new column we will generate (by defaul 'posts_spearated')
            - count_posts: default True it tells us how many different posts there have been"""
        self.df[new_col_name] = self.df[column].apply(lambda x: x.split(separator))
        if count_posts == True:
            self.df['count_posts'] = self.df[new_col_name].str.len()
        return self.df.head()

    def avg_num_char(self, column='posts_separated', new_col_name='avg_num_char_x_post'):
        """Will create a column with the average number of characters per post
        It takes two arguments:
            - column: the column with the posts you what to count the characters for (by default 'posts_separated' but if you have not done split_posts, this column will not exists)
            - new_col_name: how you want to name the new column (by default avg_num_char_x_post)"""
        self.df[new_col_name] = [np.mean([len(i) for i in x]) for x in self.df[column]]

    def num_links(self, column='posts_separated', new_col_name='num_of_links'):
        """Will create a column with the number of hyperlinks a person has used
        It takes two arguments:
            - column: the column with the posts you what to count the number of links for
            - new_col_name: how you want to name the new column"""
        self.df[new_col_name] = [sum([url.count('http') for url in x]) for x in self.df[column]]

    def keisey_temp(self, column, keirsey, col_index=-1):
        """Will take the "type" column and extracts the keirsey temperaments
        It takes three arguments:
            - column: the "type" column
            - keirsey: the keirsey temperaments you want to extract (NT, NF, SP, SJ)
            - col_index: the index where you want to put the new column"""
        keirsey_result = self.df[column].str.contains(keirsey, regex=True)
        keirsey_result = keirsey_result*1
        self.df.insert(col_index, keirsey.replace('.',''), keirsey_result)

    def get_emoticons(self, column, list_emoticons, total=False, average=False):
        """Searches for the emoticons specified to see how many times a person has used them
        It takes 4 arguments:
            - column: the column in which the posts are
            - list_emoticons: the list of the different emoticons we want to search for
            - total: default False, it will take all the columns and add them to generate a total
            - average: will divide the total column by the number of posts a person created, it is recommended since it will give a corrected total"""
        for emoji in list_emoticons:
            self.df[emoji + '_count'] = [sum([x.count(emoji) for x in post]) for post in self.df[column]]
        if total == True:
            num = len(list_emoticons)
            self.df['total_emoticons'] = self.df.iloc[:,-num:].sum(axis=1)
        if average == True:
            self.df['avg_emoticons_per_post'] = self.df['total_emoticons'] / self.df['count_posts']

    def get_mentions(self, column, list_of_types, total=False, average=False):
        """This method will generate a list of the mentions a type has done to other types. E.g How many times have the INTJs mentioned the ENFJs?
        It takes four arguments:
            - column: the column where the posts are.
            - list_of_types: a list of the types you want the program to extract the data of
            - total_mentions: if True (default is False), it will generate a column with the total mentions
            - average: will divide the total column by the number of posts a person created, it is recommended since it will give a corrected total"""
        for mbti_type in list_of_types:
            self.df[mbti_type + '_mentions'] = [sum([x.casefold().count(mbti_type.casefold()) for x in post]) for post in self.df[column]]
        if total == True:
            mention_cols = [col for col in self.df.columns if 'mentions' in col]
            self.df['total_mentions'] = self.df.filter(mention_cols).sum(axis=1)
        if average == True:
            self.df['avg_mentions_per_post'] = self.df['total_mentions'] / self.df['count_posts']

    def extract_words(self, word_list, total=False, total_col_name=None, average=False, avg_col_name=None):
        """This method will search the amount of times a person has used a certain word. It will then create a column with that number.
        It takes five arguments:
            - word_list: a list of the words you want to search for. It is recommended to leave a space before and after the words you want to look for e.g. " potato " instead of "potato"
            - total: if True (default is False), it will generate a column with the sum of the words you have specified in the list
            - total_col_name: allows you to specify the name of the total column
            - average: will divide the total column by the amount of posts the person has made
            - avg_col_name: allows you to specify the name of teh average column"""
        table = str.maketrans({key: ' ' for key in string.punctuation}) # this cleans the text of these signs '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' which is good since we are only trying to detect words
        cleaned_posts = [[x.translate(table) for x in post] for post in self.df['posts_separated']]
        for word in word_list:
            self.df[word.replace(' ','')+'_count'] = [sum([x.casefold().count(word.casefold()) for x in post]) for post in cleaned_posts]
        if total == True:
            num = len(word_list)
            self.df[total_col_name] = self.df.iloc[:,-num:].sum(axis=1)
        if average == True:
            self.df[avg_col_name] = self.df[total_col_name] / self.df['count_posts']
    
    def fit(self):
        """Will execute the following methods all at once: 
        
        - dummies_types() which creates dummies for the "type" column
        - posts_len() which will generate a column with the length of the "posts" column
        - split_posts() which will separate the "posts" column into individual posts
        - avg_num_char() which will provide the average number of characters per post
        - num_links() which will return the number of hyperlinks a user made

        """
        self.dummies_types()
        self.posts_len(self.df)
        self.split_posts()
        self.avg_num_char()
        self.num_links()
        return self.df
        
    def __repr__(self):
        """The goal of __repr__ is to make our instance be unambiguous"""
        return repr(self.df)
    
    @staticmethod
    def get_df_name(dataframe):
        name =[x for x in globals() if globals()[x] is dataframe][0]
        return name
    
    def __str__(self):
        """The goal of __str__ is to make our instance be readable"""
        globals()['df'] = self.df 
        return "'The object created is the dataframe: '{}', the target column: '{}', and the text input column:'{}'".format(self.get_df_name(self.df), self.target, self.posts)
    
    