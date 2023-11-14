import csv

def calculate_statistics(data, selected_option):
    if not data:
        return "Please enter valid data"

    n = len(data)

    if selected_option == "Minimum":
        return f"Minimum: {min(data)}"
    elif selected_option == "Maximum":
        return f"Maximum: {max(data)}"
    elif selected_option == "Mode":
        frequency = {}
        for item in data:
            frequency[item] = frequency.get(item, 0) + 1
        mode = max(frequency, key=frequency.get)
        return f"Mode: {mode}"
    elif selected_option == "Median":
        sorted_data = sorted(data)
        if n % 2 == 1:
            median = sorted_data[n // 2]
        else:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        return f"Median: {median}"
    elif selected_option == "Mean":
        mean = sum(data) / n
        return f"Mean: {mean}"
    elif selected_option == "Mean Absolute Deviation":
        mean = sum(data) / n
        mad = sum(abs(x - mean) for x in data) / n
        return f"Mean Absolute Deviation: {mad}"
    elif selected_option == "Standard Deviation":
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = variance ** 0.5
        return f"Standard Deviation: {std_dev}"

def export_to_csv(data_dict):
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
