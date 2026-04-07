class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # x <- x - learning_rate * derivative
        # init <- init - learning_rate * (2  * init)
        for _ in range(iterations):
            init = init - learning_rate * 2 * init
        return round(init, 5)