class MetricsticsHelper:

    @staticmethod
    def metricstics_sum(data):
        total = 0
        for item in data:
            total += item
        return total

    @staticmethod
    def metricstics_len(data):
        count = 0
        for item in data:
            count += 1
        return count

    @staticmethod
    def metricstics_sort(data):
        n = MetricsticsHelper.metricstics_len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

    @staticmethod
    def metricstics_abs(number):
        if number < 0:
            return -number
        else:
            return number