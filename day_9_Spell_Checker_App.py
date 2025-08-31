# importing the spell checker library
from spellchecker import SpellChecker

# creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()   # Split sentence into words
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)  # Suggested correction
            if corrected_word and corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)  # Keep word as is if correct

        # Return corrected sentence
        return " ".join(corrected_words)


# ---------------------------
# Example usage
# ---------------------------
if __name__ == "__main__":
    app = SpellCheckerApp()

    text = input("Enter a sentence: ")
    corrected = app.correct_text(text)
    print("\nCorrected Sentence:", corrected)
