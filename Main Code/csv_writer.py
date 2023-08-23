import csv

def write_to_csv(file_name, ear_and_mar_vals):
    with open(f"{file_name}-Data.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        column_headers = ['Time (s)', 'EAR', 'MAR', 'Blinked (Y/N)', 'Yawned (Y/N)']  # Replace with your actual column names
        writer.writerow(column_headers)
        writer.writerows(ear_and_mar_vals)