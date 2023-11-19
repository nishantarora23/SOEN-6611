class MetricsticsHelper:
    def __init__(self):
        self.data = None

    @staticmethod
    def metricstics_sum(self, data):
        """ Calculate the sum of a list of numbers."""
        self.data = data  # Store data in the instance variable
        total = 0
        for item in data:
            total += item
        return total

    @staticmethod
    def metricstics_len(self, data):
        """ Get the length of a list."""
        count = 0
        for _ in data:
            count += 1
        return count

    @staticmethod
    def metricstics_sort(self, data):
        """ Sort a list in ascending order."""
        self.data = data  # Store data in the instance variable
        n = self.metricstics_len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

    @staticmethod
    def metricstics_abs(number):
        """ Calculate the absolute value of a number."""
        if number < 0:
            return -number
        else:
            return number
