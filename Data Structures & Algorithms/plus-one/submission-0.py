class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ten = pow(10,len(digits)-1)
        total = 0
        for char in digits:
            total += int(char) * ten
            ten /= 10
        return list(str(int(total+1)))