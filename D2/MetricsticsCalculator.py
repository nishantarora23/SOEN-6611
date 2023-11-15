from MetricsticsHelper import *
class MetricsticsCalculator:

    @staticmethod
    def metricstics_min(data):
        if not data:
            return None
        minimum = data[0]
        for element in data[1:]:
            if element < minimum:
                minimum = element

        return minimum

    @staticmethod
    def metricstics_max(data):
        if not data:
            return None
        maximum = data[0]
        for element in data[1:]:
            if element > maximum:
                maximum = element

        return maximum

    @staticmethod
    def metricstics_mode(data):
        if not data:
            return None
        frequencies = []
        unique_items = []
        for item in data:
            if item in unique_items:
                index = unique_items.index(item)
                frequencies[index] += 1
            else:
                unique_items.append(item)
                frequencies.append(1)

        max_freq = metricstics_max(frequency.values())
        modes = []
        for item, freq in zip(unique_items, frequencies):
            if freq == max_freq:
                modes.append(item)

        if MetricsticsHelper.metricstics_len(modes) == 1:
            return modes[0]
        else:
            return modes

    @staticmethod
    def metricstics_median(data):
        if not data:
            return None
        MetricsticsHelper.metricstics_sort(data)
        n = MetricsticsHelper.metricstics_len(data)
        if n % 2 == 0:
            middle1 = data[n // 2 - 1]
            middle2 = data[n // 2]
            median = (middle1 + middle2) / 2
        else:
            median = data[n // 2]

        return median

    @staticmethod
    def metricstics_mean(data):
        if not data:
            return None
        total = MetricsticsHelper.metricstics_sum(data)
        mean = total / MetricsticsHelper.metricstics_len(data)

        return mean

    @staticmethod
    def metricstics_mean_absolute_deviation(data):
        if not data:
            return None
        mean = metricstics_mean(data)
        abs_diff_sum = 0
        for item in data:
            abs_diff_sum += MetricsticsHelper.metricstics_abs(item - mean)

        n = metricstics_len(data)
        mad = abs_diff_sum / n
        return mad

    @staticmethod
    def metricstics_standard_deviation(data):
        variance = metricstics_variance(data)
        if variance is None:
            return None
        standard_deviation = variance ** 0.5
        return standard_deviation

    @staticmethod
    def metricstics_variance(data):
        if not data:
            return None
        mean = metricstics_mean(data)
        squared_diff_sum = 0
        for item in data:
            squared_diff_sum += (item - mean) ** 2

        n = MetricsticsHelper.metricstics_len(data)
        variance = squared_diff_sum / n

        return variance