class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        points = [(p, s) for p, s in zip(position, speed)]
        points.sort(reverse=True)

        scores = [(target - x[0]) / x[1] for x in points]
        fleets = 1
        head = scores[0]

        for i in range(1, len(scores)):
            if head < scores[i]:
                fleets += 1
                head = scores[i]

        return fleets





