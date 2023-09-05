class Solution:
    def candy(self, ratings) -> int:
        self.ratings = ratings
        left, right = self.managing_left(), self.managing_right()
        total_candies = 0
        for i in range(len(self.ratings)):
            total_candies += max(left[i], right[i])
        return total_candies

    def managing_left(self):
        left = [1] * len(self.ratings)
        for i in range(1, len(self.ratings)):
            if self.ratings[i] > self.ratings[i - 1]:
                left[i] += left[i - 1]

        return left
    
    def managing_right(self):
        right = [1] * len(self.ratings)
        for i in range(len(self.ratings) - 2, -1, -1):
            if self.ratings[i] > self.ratings[i + 1]:
                right[i] += right[i + 1]
        
        return right