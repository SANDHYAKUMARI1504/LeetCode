class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = []

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    placed.append(fruits[i])
                    baskets.pop(j)
                    break

        n = len(fruits) - len(placed)
        return n