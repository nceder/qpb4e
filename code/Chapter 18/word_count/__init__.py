#__init__.py
from word_count.exceptions import EmptyStringError
from word_count.cleaning import clean_line, get_words
from word_count.counter import count_words, word_stats
