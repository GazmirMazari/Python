# Python3 program for a word frequency
# counter after crawling/scraping a web-page
import operator
from collections import Counter
import wikipedia
 


""" function to get user input for wikipedia name to fetch content from words and print top words
:param url: wikipedia url
:param number_of_top_words: number of top words to print
:return number_of_top_words: wikipedia """
def getUserInput():
    word_to_exlude = input("Enter the word to exclude: ")
    number_of_top_words = input("Enter the number of top words you would like to see(accepts_digits_only): ")
    if not number_of_top_words.isdigit():
        print("Invalid input, defaulting to 10, has to be number")
        number_of_top_words = 10
    return number_of_top_words, word_to_exlude

"""
Function to extract and convert.
:param wiki_content_json: content json to extract page content from
:return word_list: word_list with all required filters
"""

def extract_content_to_list(content, words_to_exclude):

     word_list = []
     try:
         # split the content into words
         word_list = content.split()

         # strip the spliced word for possible punctuations, discard the word > 4 char length and remove the words being passed
         word_list = [word for word in word_list if not word.isnumeric() and word not in words_to_exclude]
     except Exception as e:
         print("[ EXCEPTION : Generic Exception Occurred : {} ]".format(str(e)))
     finally:
         return word_list

def get_top_frequent_words(word_list, number_of_top_words):
    try:
        # convert the list to dictionary and count the frequency of each word
        word_frequency = Counter(word_list)
        # sort the dictionary in descending order
        sorted_word_frequency = sorted(word_frequency.items(), key=operator.itemgetter(1), reverse=True)
        print("Top {} words are: ".format(number_of_top_words))
        for word, frequency in sorted_word_frequency[:int(number_of_top_words)]:
            print(word, frequency)
    except Exception as e:
        print("[ EXCEPTION : Generic Exception Occurred : {} ]".format(str(e)))
  
 
# Driver code
if __name__ == '__main__':
    try:
        print("Welcome to Wikipedia Word Frequency Counter")
        print("==========================================")
        print("Printing Top 10 most used words in the Wikipedia page")
        # get user input
        number_of_words, words_to_exlude = getUserInput()
     
        #grab the content from History of the Page
        content = wikipedia.page("History of Microsoft").content

        #convert the content to list
        word_list = extract_content_to_list(content, words_to_exlude)
  
        # # get top frequent words based on user input
        words =get_top_frequent_words(word_list, number_of_words )
    except Exception as e:
        print("[ EXCEPTION : Generic Exception Occurred : {} ]".format(str(e)))
