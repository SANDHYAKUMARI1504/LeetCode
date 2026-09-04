import heapq

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_rating = {}
        self.food_cuisine = {}
        self.cuisine_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_rating[food] = rating
            self.food_cuisine[food] = cuisine

            if cuisine not in self.cuisine_heap:
                self.cuisine_heap[cuisine] = []

            # negative rating because heapq is a min-heap
            heapq.heappush(
                self.cuisine_heap[cuisine],
                (-rating, food)
            )

    def changeRating(self, food, newRating):
        cuisine = self.food_cuisine[food]

        self.food_rating[food] = newRating

        heapq.heappush(
            self.cuisine_heap[cuisine],
            (-newRating, food)
        )

    def highestRated(self, cuisine):
        heap = self.cuisine_heap[cuisine]

        while heap:
            rating, food = heap[0]

            # check whether this heap entry is still valid
            if -rating == self.food_rating[food]:
                return food

            # remove outdated rating
            heapq.heappop(heap)