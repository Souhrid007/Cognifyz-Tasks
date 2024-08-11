import string

def count_words_in_file(filename):
    word_counts = {}

    try:
        with open(filename, 'r') as file:
            content = file.read()

            content = content.translate(str.maketrans('', '', string.punctuation)).lower()

            words = content.split()

            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

        sorted_word_counts = dict(sorted(word_counts.items()))

        for word, count in sorted_word_counts.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = input("Enter the filename (with extension): ")
count_words_in_file(filename)
