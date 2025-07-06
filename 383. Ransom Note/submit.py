class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for note_letter in ransomNote:
            for mag_letter in magazine:
                if note_letter == mag_letter: