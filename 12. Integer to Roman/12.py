class Solution:
    def intToRoman(self, n: int) -> str:
        roman = str()
        if n // 1000:
            roman += ("M" * (n // 1000))
            n %= 1000
        if n // 900:
            roman += ("CM" * (n // 900))
            n %= 900
        if n // 500:
            roman += ("D" * (n // 500))
            n %= 500
        if n // 400:
            roman += ("CD" * (n // 400))
            n %= 400
        if n // 100:
            roman += ("C" * (n // 100))
            n %= 100
        if n // 90:
            roman += ("XC" * (n // 90))
            n %= 90
        if n // 50:
            roman += ("L" * (n // 50))
            n %= 50
        if n // 40:
            roman += ("XL" * (n // 40))
            n %= 40
        if n // 10:
            roman += ("X" * (n // 10))
            n %= 10
        if n // 9:
            roman += ("IX" * (n // 9))
            n %= 9
        if n // 5:
            roman += ("V" * (n // 5))
            n %= 5
        if n // 4:
            roman += ("IV" * (n // 4))
            n %= 4
        if n // 1:
            roman += ("I" * (n // 1))
        return roman

            
