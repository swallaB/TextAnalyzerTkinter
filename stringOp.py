import os
from collections import Counter

class StringManager:
    def __init__(self):
        self.content = ""
        self.unique_words = set()
        self.word_count = {}

    def load_file(self, file_path):
        """ Loads the file content and processes the unique words. """
        try:
            with open(file_path, 'r') as file:
                self.content = file.read()
                words = self.content.split()
                self.unique_words = set(words)
                self.word_count = dict(Counter(words))
        except FileNotFoundError:
            return "Error: File not found!"
        except Exception as e:
            return f"Error: {e}"
        return "File loaded successfully."

    def count_lines(self):
        """ Counts the number of lines in the file. """
        return len(self.content.splitlines())

    def count_unique_words(self):
        """ Counts the number of unique words in the file. """
        return len(self.unique_words)

    def word_frequencies(self):
        """ Returns the frequency of each word in the file. """
        return self.word_count

    def capitalise_first_last_chars(self):
        """ Capitalises the first and last character of each line. """
        lines = self.content.splitlines()
        modified_lines = []
        for line in lines:
            if len(line) > 0:
                line = line[0].upper() + line[1:-1] + line[-1].upper()
            modified_lines.append(line)
        return "\n".join(modified_lines)

    def display_summary(self):
        """ Displays a summary of the file properties. """
        return (
            f"Total lines: {self.count_lines()}\n"
            f"Unique words: {self.count_unique_words()}\n"
            f"Word Frequencies: {self.word_frequencies()}"
        )
