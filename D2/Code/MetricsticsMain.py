import csv
from MetricsticsCalculator import *

class MetricsticsMain:
    """  A class designed for computing statistical measures on a list of numbers, excluding the utilization of built- in functions. """

    @staticmethod
    def calculate_metricstics(data, selected_option):
        if not data:
            return "Please enter valid data"

        if selected_option == "Minimum":
            return f"Minimum: {MetricsticsCalculator.metricstics_min(data)}"
        elif selected_option == "Maximum":
            return f"Maximum: {MetricsticsCalculator.metricstics_max(data)}"
        elif selected_option == "Mode":
            return f"Mode: {MetricsticsCalculator.metricstics_mode(data)}"
        elif selected_option == "Median":
            return f"Median: {MetricsticsCalculator.metricstics_median(data)}"
        elif selected_option == "Mean":
            return f"Mean: {MetricsticsCalculator.metricstics_mean(data)}"
        elif selected_option == "Mean Absolute Deviation":
            return f"Mean Absolute Deviation: {MetricsticsCalculator.metricstics_mean_absolute_deviation(data)}"
        elif selected_option == "Standard Deviation":
            return f"Standard Deviation: {MetricsticsCalculator.metricstics_standard_deviation(data)}"

    @staticmethod
    def export_to_csv(data_dict):
        """ Export data to a CSV file. """
        filename = "statistics_data.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            #writer.writerow(['Data'])
            for value in data_dict['Data']:
                writer.writerow([value])
            if 'Mean Absolute Deviation' in data_dict:
                writer.writerow(['MAD =', data_dict['Mean Absolute Deviation']])
            elif 'Standard Deviation' in data_dict:
                writer.writerow(['SD =', data_dict['Standard Deviation']])
        return f"Data exported to {filename}"
