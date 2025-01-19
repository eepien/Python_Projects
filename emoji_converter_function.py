
#==============================
# Function Emoji converter
#============================
def emoji_conv(message):
    words = message.split(" ")
    # print(words)
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(" Are you Happy :) or Sad :(? > ") # Try this input: I am very happy today :). Was sad yesterday :(
results = emoji_conv(message)
print(results)