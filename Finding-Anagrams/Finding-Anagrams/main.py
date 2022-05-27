# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    f = False
    if (len(word)==len(anagram)):
        if (set(word.lower()) == set(anagram.lower())):
            for i in range(len(word)-1):
                if word[i] !=anagram[i]:
                    f =True

    return f


print(find_anagram("hello", "check"))


    

