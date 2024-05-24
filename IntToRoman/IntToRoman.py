import sys

class Solution(object):
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman = []
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman.append(symbols[i])
        return ''.join(roman)

def main():
    solution = Solution()

    num = int(input("Enter an integer: "))
    if num > 0:
        roman = solution.intToRoman(num)
        print(f"The Roman numeral for {num} is {roman}")
    else:
        print("Invalid input! Please enter a positive integer.")

if __name__ == "__main__":
    main()