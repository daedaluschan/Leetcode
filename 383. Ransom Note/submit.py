class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for note_letter in ransomNote:
            found = False
            for idx, mag_letter in enumerate(magazine):
                if note_letter == mag_letter:
                    found = True
                    mag_letter[idx] = None

            if not found:
                return False

        return True