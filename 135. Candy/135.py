class Solution:
    def candy(self, ratings) -> int:
        if len(ratings) == 1: return 1
        if len(ratings) == 2: 
            ratings.sort()
            if ratings[0] == ratings[1]: return 2
            if ratings[0] < ratings[1]: return 3
        i = 1
        neighbour = 1
        candies = 0
        while i < len(ratings) - 1:
            # Estimated Neighbours_________________
            if ratings[i] > ratings[i - 1]:
                neighbour += 1
            elif ratings[i] == ratings[i - 1]:
                neighbour = 1
            # _____________________________________
            if ratings[i + 1] < ratings[i]:
                count = 1
                while i < len (ratings) - 1 and ratings[i + 1] < ratings[i]:
                    i += 1
                    candies += count
                    count += 1
                candies += max(count, neighbour)
                i += 1
                neighbour = 1
                continue
            candies += neighbour
            i += 1
        if ratings[-1] > ratings[-2]: 
            candies += neighbour + 1
        if ratings[-1] == ratings[-2]:
            candies += 1

        if ratings[0] < ratings[1]:
            candies += 1
        else:
            i = 0
            while i < len(ratings) - 1 and ratings[i + 1] < ratings[i]:
                i += 1
            candies += i + 1


        return candies
            