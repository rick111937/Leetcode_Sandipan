class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        try:
            val = float(s)
        except:
            return False
        if s.lower() in ["inf", "+inf", "-inf", "infinity", "+infinity", "-infinity", "nan"]:
            return False
        return True