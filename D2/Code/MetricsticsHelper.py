class MetricsticsHelper:

    @staticmethod
    def metricstics_sum(data):
        """ Calculate the sum of a list of numbers."""
        total = 0
        for item in data:
            total += item
        return total

    @staticmethod
    def metricstics_len(data):
        """ Get the length of a list."""
        count = 0
        for _ in data:
            count += 1
        return count

    @staticmethod
    def metricstics_sort(data):
        """ Sort a list in ascending order."""
        n = MetricsticsHelper.metricstics_len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

    @staticmethod
    def metricstics_abs(x):
        """ Calculate the absolute value of a number."""
        if x < 0:
            return -x
        else:
            return x
