# Straightforward/Bruteforce way is to just sort and compare - poor performance
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length is different, then no need for more logic
        if len(s) != len(t):
            return False

        char_count = [0] * 26  # Array for 26 lowercase English letters
        '''
        The ord() function converts a character into its ASCII (Unicode) value. For example:
                ord('a') = 97
                ord('b') = 98
                ord('z') = 122
        Subtracting ord('a') from ord(char) gives the zero-based index of the character in the alphabet:
                For 'a': ord('a') - ord('a') = 0
                For 'b': ord('b') - ord('a') = 1
                For 'z': ord('z') - ord('a') = 25
        This calculation maps each letter to its corresponding index in the char_count array.
        '''
        for char in s:
            char_count[ord(char) - ord('a')] += 1
            #This increments the count of the current character in the char_count array.

        for char in t:
            char_count[ord(char) - ord('a')] -= 1
            if char_count[ord(char) - ord('a')] < 0:
                return False
            #After decrementing, if the count of any character becomes negative, it means that t contains more occurrences of that character than s.
        return True