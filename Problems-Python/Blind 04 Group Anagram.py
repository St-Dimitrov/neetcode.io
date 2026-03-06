from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a hashmap to store groups of anagrams
        anagrams = defaultdict(list)

        for word in strs:
            char_count = [0] * 26  # Assuming only lowercase English letters
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            anagrams[tuple(char_count)].append(word) # update the defaultdict key frequency count : value word
            #print(anagrams) #testing

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values()) # return only values from hashmap as a array
''' testing
solution = Solution()
result = solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
print(result)
'''
