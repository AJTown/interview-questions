# Given an enumerable of strings, attempt to parse each string and if
# it is an integer, add it to the returned enumerable.
#
# For example:
#
# extract_numbers(["123", "hello", "234"]);
#
# ; would return:
#
# [
#   123,
#   234
# ]
#
def extract_numbers(source):
    numericReturnList = []
    for item in source:
        item = str(item)
        if item.isnumeric():
            numericReturnList.append(item)
    return numericReturnList
    raise Exception('Not implemented')

# Given two enumerables of strings, find the longest common word.
#
# For example:
#
# longest_common_word(
#     [
#         "love",
#         "wandering",
#         "goofy",
#         "sweet",
#         "mean",
#         "show",
#         "fade",
#         "scissors",
#         "shoes",
#         "gainful",
#         "wind",
#         "warn"
#     ],
#     [
#         "wacky",
#         "fabulous",
#         "arm",
#         "rabbit",
#         "force",
#         "wandering",
#         "scissors",
#         "fair",
#         "homely",
#         "wiggly",
#         "thankful",
#         "ear"
#     ]
# );
#
# ; would return "wandering" as the longest common word.
def longest_common_word(first, second):
    longestCommonWord = ''
    lenLongestWord = 0
    for word in first:
        if lenLongestWord == 0:
            if word in second:
                longestCommonWord = word
                lenLongestWord = len(word)
            else: 
                continue
        else:
            if len(word) > lenLongestWord:
                if word in second:
                    longestCommonWord = word
                    lenLongestWord = len(word)
                else: 
                    continue
            else:
                continue
    return longestCommonWord
        
    raise Exception('Not implemented')

# Write a function that converts kilometers to miles, given that there are
# 1.6 kilometers per mile.
#
# For example:
#
# distance_in_miles(16);
#
# ; would return 10;
def distance_in_miles(kilometers):
    miles = kilometers/1.6
    return miles
    raise Exception('Not implemented')

# Write a function that converts miles to kilometers, give that there are
# 1.6 kilometers per mile.
#
# For example:
#
# distance_in_km(10);
#
# ; would return 16;
def distance_in_km(miles):
    kilometers = miles*1.6
    return kilometers
    raise Exception('Not implemented')

# Write a function that returns true if the word is a palindrome, false if
# it is not.
#
# For example:
#
# isPalindrome("bolton");
#
# ; would return False, and:
#
# isPalindrome("Anna");
#
# ; would return True.
#
# Also complete the related test case for this method.
def isPalindrome(word):
    word = str(word)
    word = word.lower()
    Result = ''
    if word[0] == word[-1]:
        if len(word) == 1:
            Result =  True
        elif len(word) == 2:
            Result =  True
        else:
            word = word[1:-1]
            Result = isPalindrome(word)
    else:
        Result =  False

    return Result
            
    raise Exception('Not implemented')
    
    


