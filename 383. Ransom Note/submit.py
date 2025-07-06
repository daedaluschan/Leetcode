class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        used_letters = []
        for note_letter in ransomNote:
            found = False
            for idx, mag_letter in enumerate(magazine):
                if note_letter == mag_letter and (idx not in used_letters):
                    found = True
                    used_letters.append(idx)
                    break

            if not found:
                return False

        return True