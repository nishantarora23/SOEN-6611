import csv
from MetricsticsCalculator import *

class MetricsticsMain:
    """  A class designed for computing statistical measures on a list of numbers, excluding the utilization of built- in functions. """
    def __init__(self):
        self.data = None
        self.result = None

    @staticmethod
    def calculate_metricstics(self, data, selected_option):
        if not data:
            self.result = "Please enter valid data"
            return self.result

        if selected_option == "Minimum":
            self.result = f"Minimum: {self.metricstics_min(data)}"
        elif selected_option == "Maximum":
            self.result = f"Maximum: {self.metricstics_max(data)}"
        elif selected_option == "Mode":
            self.result = f"Mode: {self.metricstics_mode(data)}"
        elif selected_option == "Median":
            self.result = f"Median: {self.metricstics_median(data)}"
        elif selected_option == "Mean":
            self.result = f"Mean: {self.metricstics_mean(data)}"
        elif selected_option == "Mean Absolute Deviation":
            self.result = f"Mean Absolute Deviation: {self.metricstics_mean_absolute_deviation(data)}"
        elif selected_option == "Standard Deviation":
            self.result = f"Standard Deviation: {self.metricstics_standard_deviation(data)}"

        self.data = data
        return self.result

    @staticmethod
    def export_to_csv(data_dict):
        """ Export data to a CSV file. """
        filename = "statistics_data.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Data'])
            for value in data_dict['Data']:
                writer.writerow([value])
            if 'Mean Absolute Deviation' in data_dict:
                writer.writerow(['MAD =', data_dict['Mean Absolute Deviation']])
            elif 'Standard Deviation' in data_dict:
                writer.writerow(['SD =', data_dict['Standard Deviation']])
        return f"Data exported to {filename}"
