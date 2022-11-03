# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    # Converting the strings to lower cases

    word = word.lower()
    anagram = anagram.lower()

    # Sorting the strings to check for anagrams

    if(sorted(word)==sorted(anagram)):
      return True
    else:
      return False