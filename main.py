import tkinter as tk
from tkinter import filedialog, messagebox
from stringOp import StringManager


class StringManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("String Manager")
        self.root.geometry("500x600")
        self.root.config(bg="black")

        self.sm = StringManager()  # Creating an instance of StringManager

        self.create_widgets()

    def create_widgets(self):
        """Creates the GUI components"""

        # Load file button
        self.load_button = tk.Button(self.root, text="Load File", width=20, height=2, font=("Consolas", 10),bg="#E2725B",
                                     command=self.load_file)
        self.load_button.pack(pady=10,expand=True)

        # Text area to display file content or results
        self.text_area = tk.Text(self.root, width=50, height=15, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(pady=10,expand=True)

        # Count lines button
        self.count_lines_button = tk.Button(self.root, text="Count Lines", width=20, height=2, bg="#F8BBD0", font=("Consolas", 10),
                                            command=self.count_lines)
        self.count_lines_button.pack(pady=5,expand=True)

        # Count unique words button
        self.count_unique_words_button = tk.Button(self.root, text="Count Unique Words", width=20, height=2, bg="#D6AEDD", font=("Consolas", 10),
                                                   command=self.count_unique_words)
        self.count_unique_words_button.pack(pady=5,expand=True)

        # Word frequencies button
        self.word_freq_button = tk.Button(self.root, text="Word Frequencies", width=20, height=2, bg="#A8E6CF", font=("Consolas", 10),
                                          command=self.word_frequencies)
        self.word_freq_button.pack(pady=5,expand=True)

        # Capitalise first & last characters button
        self.capitalize_button = tk.Button(self.root, text="Capitalize First & Last Char", width=20, height=2, font=("Consolas", 10),
                                           bg="#4B9E9E", command=self.capitalize_first_last_chars)
        self.capitalize_button.pack(pady=5,expand=True)

        # Display summary button
        self.display_summary_button = tk.Button(self.root, text="Display Summary", width=20, height=2, bg="#D6CFC7", font=("Consolas", 10),
                                                command=self.display_summary)
        self.display_summary_button.pack(pady=5,expand=True)

    def load_file(self):
        """ Opens file dialog to load a file and then processes it. """
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            result = self.sm.load_file(file_path)
            if "Error" in result:
                messagebox.showerror("Error", result)
            else:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, "File loaded successfully!\n\n" + self.sm.content)

    def count_lines(self):
        """ Displays the count of lines in the file. """
        lines = self.sm.count_lines()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Total lines: {lines}\n")

    def count_unique_words(self):
        """ Displays the count of unique words. """
        unique_words = self.sm.count_unique_words()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Total unique words: {unique_words}\n")

    def word_frequencies(self):
        """ Displays the word frequencies in the file. """
        word_freq = self.sm.word_frequencies()
        self.text_area.delete(1.0, tk.END)
        for word, freq in word_freq.items():
            self.text_area.insert(tk.END, f"{word}: {freq}\n")

    def capitalize_first_last_chars(self):
        """ Displays the file with first and last characters capitalized. """
        modified_text = self.sm.capitalise_first_last_chars()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, modified_text)

    def display_summary(self):
        """ Displays the summary of the file. """
        summary = self.sm.display_summary()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, summary)


if __name__ == "__main__":
    root = tk.Tk()
    app = StringManagerApp(root)
    root.mainloop()
