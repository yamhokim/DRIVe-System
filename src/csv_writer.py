import csv

def write_to_csv(file_name, ear_and_mar_vals, counter):
    with open(f"{file_name}-Data.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        if counter == 0:    # Since the headers should only be written once, add a counter
            column_headers = ['Time (s)', 'EAR', 'MAR', 'Blinked (Y/N)', 'Yawned (Y/N)']  # Replace with your actual column names
            writer.writerow(column_headers)
            counter = 1
        writer.writerows(ear_and_mar_vals)


def write_to_csv_perclos(file_name, perclos_vals):
    with open(f"{file_name}-PERCLOS-Data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        column_headers = ["Interval #", "PERCLOS Value"]
        writer.writerow(column_headers)
        writer.writerows(perclos_vals)