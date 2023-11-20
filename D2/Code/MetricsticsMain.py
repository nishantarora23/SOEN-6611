import csv
from MetricsticsCalculator import *

class MetricsticsMain:
    """A class designed for computing statistical measures on a list of numbers, excluding the utilization of built-in functions."""

    def __init__(self, data):
        self.data = data

    def calculate_metricstics(self, selected_option):
        """Calculate selected statistical metric on the given data."""
        if not self.data:
            result = "Please enter valid data"
            return result

        if selected_option == "Minimum":
            result = f"Minimum: {MetricsticsCalculator.metricstics_min(self.data)}"
        elif selected_option == "Maximum":
            result = f"Maximum: {MetricsticsCalculator.metricstics_max(self.data)}"
        elif selected_option == "Mode":
            result = f"Mode: {MetricsticsCalculator.metricstics_mode(self.data)}"
        elif selected_option == "Median":
            result = f"Median: {MetricsticsCalculator.metricstics_median(self.data)}"
        elif selected_option == "Mean":
            result = f"Mean: {MetricsticsCalculator.metricstics_mean(self.data)}"
        elif selected_option == "Mean Absolute Deviation":
            result = f"Mean Absolute Deviation: {MetricsticsCalculator.metricstics_mean_absolute_deviation(self.data)}"
        elif selected_option == "Standard Deviation":
            result = f"Standard Deviation: {MetricsticsCalculator.metricstics_standard_deviation(self.data)}"

        return result

    @staticmethod
    def export_to_csv(data_dict):
        """Export data to a CSV file."""
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