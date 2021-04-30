'''
Create a function called phrase_word_split() which takes in a string phrase 
and a set list_of_words. 
The function will then determine if it is possible to split the string in a way 
in which words can be made from the list of words. 
You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
'''
def phrase_word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []
    
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)

            # recursively call the fn on the remaining portion of the phrase
            return phrase_word_split(phrase[len(word):], list_of_words, output)

    return output

print(phrase_word_split('themanran', ['the','ran','man']))
print(phrase_word_split('ilovedogsJohn', ['i','am','a','dogs','lover','love','John']))
print(phrase_word_split('themanran', ['clown','ran','man']))