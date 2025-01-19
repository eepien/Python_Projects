#=====================================
# Program Emoji Converter: Outputs an emogy
#=====================================
message = input("Are you happy :) or Sad :(? > ")                  # > indicator for user to type a message
words = message.split(" ")            # splits the string by space. Usesspace as boundary to seperate strings
#print(words)                          # > Hello I am Epie --> ['Hello', 'I', 'am', 'Epie']
emojis = {
    ":)": "😊",                           # For Windows11 type: Windows_key + period
    ":(": "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "    # Takes a word from words and compares with emojis list. continue next line
print(output)                                 # Returns emoji if word is emoji or word if not emoji