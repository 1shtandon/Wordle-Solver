import re
import requests
print("----------------------------------------------------")
print("          Welcome to the Word Game!")
print("----------------------------------------------------")

print("fetching all 5 letters words........")

# getting html code from the website
data_response = requests.get("https://meaningpedia.com/5-letter-words?show=all")

# compiling regex
regex = re.compile(r'<span itemprop="name">(\w+)</span>')
# write to file
word_list = regex.findall(data_response.text)
with open("words.txt", "w") as f:
    for word in word_list:
        f.write(word + "\n")

#  removing duplicates
word_list = list(set(word_list))

# sorting words by alphabetical order
with open("words.txt", "r") as f:
    words = f.readlines()
    words.sort()
    with open("words.txt", "w") as f:
        for word in words:
            f.write(word)

print("Words fetched!")


def updateByLetters(list):
    # update the file with words having letters in the list
    with open("words.txt", "r") as f:
        words = f.readlines()
        with open("words.txt", "w") as f:
            for word in words:
                if all(letter in word for letter in list):
                    f.write(word)


def updateByPosition(searchLetter, index):
    # update the file with words having letters and their position known in the list
    with open("words.txt", "r") as f:
        words = f.readlines()
        with open("words.txt", "w") as f:
            for word in words:
                if word[index] == searchLetter:
                    f.write(word)


def removeByLetters(list):
    # update the file with words not having these individual letters in the list
    with open("words.txt", "r") as f:
        words = f.readlines()
        with open("words.txt", "w") as f:
            for word in words:
                if not any(letter in word for letter in list):
                    f.write(word)


print("choose among the following options")
while (True):
    print("1. update by letters")
    print("2. update by index")
    print("3. remove by letters")
    print("4. exit")
    choice = int(input())
    if choice == 1:
        print("enter the letters present in the word")
        letters = input().split()
        updateByLetters(letters)
    elif choice == 2:
        print("enter the letter and index")
        search_letter = input()
        position = int(input())
        updateByPosition(search_letter, position)
    elif choice == 3:
        print("enter the letters not present in the word")
        letters = input().split()
        removeByLetters(letters)
    elif choice == 4:
        print("Hope you got the word!")
        break
    else:
        continue
