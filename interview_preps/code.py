""" 1. Anagram Test: Decide if two strings are anagrams or not """
def anagram_test_one(str1, str2):
  return sorted(str1) == sorted(str2)

def anagram_test_two(str1, str2):
  if len(str1) != len(str2):
    return False
  for c in str1:
    if c in str2:
      continue
    return False
  return True

""" 2. Determine if a string has all unique characters """
def unique_one(string):
  # Performance: O(1). We exit as soon as first duplicate is found
  unique_chars = set()
  for char in string:
    if char in unique_chars:
      return False
    unique_chars.add(char)
  return True

def unique_two(string):
  # Performance: O(n) since we would have to process all chars in the string
  return len(set(string)) == len(string)
