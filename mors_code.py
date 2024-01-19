morse_words = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-",
    ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.", "$": "...-..-",
    "@": ".--.-.", " ": "/"
}

morse_to_words = {v: k for k, v in morse_words.items()}
print("[1] Morse to Word")
print("[2] Word to Morse")
choice = input("Enter a choice: ")

if choice == "1":
    user = input("Enter Morse code: ")
    code_words = user.split("/")
    for code_word in code_words:
        letters = code_word.split()
        word = ""
        for letter in letters:
            if letter in morse_to_words:
                character = morse_to_words[letter]
                word += character
        print(word, end=" ")
    print()

elif choice == "2":
    user = input("Enter a word: ").upper()
    for letter in user:
        code = morse_words.get(letter, "")
        print(code, end=" ")
    print()

else:
    exit()
