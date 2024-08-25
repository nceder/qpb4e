# cleaning.py
from word_count.exceptions import EmptyStringError

punct = str.maketrans("",  "", "!.,:;-?")

def clean_line(line):
    """changes case and removes punctuation"""
    
    # raise exception if line is empty
    # uncomment to test EmptyStringError
    #if not line.strip():
    #    raise EmptyStringError()
    
    # make all one case
    cleaned_line = line.lower()
        
    # remove punctuation
    cleaned_line = cleaned_line.translate(punct)
    return cleaned_line


def get_words(line):
    """splits line into words, and rejoins with newlines"""
    words = line.split()
    return "\n".join(words) + "\n"
     
