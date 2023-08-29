class Solution:
    def isPalindrome(self, s: str) -> bool:
        lP = 0
        rP = len(s)-1
        
        while(lP < rP):
            print("Left Pointer Index: " + str(lP) + " Value: " + s[lP])
            print("Right Pointer Index: " + str(rP) + " Value: " + s[rP])
            while lP < rP and not s[lP].isalnum():
                lP += 1
            while rP > lP and not s[rP].isalnum():
                rP -= 1
            if s[lP].lower() != s[rP].lower():
                return False
            lP += 1
            rP -= 1
        return True