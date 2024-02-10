import csv
import json


def read_csv_to_dict(csv_file):
    result = {}
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row
        names = [cell.strip() for cell in header[1:] if cell.strip()]  # Extract names

        for row in reader:
            question_number = int(row[0].strip())  # Extract the question number
            for i, name in enumerate(names):
                if i + 1 < len(row) and row[i + 1].strip():
                    result.setdefault(name, {})[question_number] = row[i + 1].strip()

    return result


# Example usage
csv_file = "/Users/zman/Downloads/Superbowl-Prop-Submissions.csv"  # Replace with your CSV file path
data = read_csv_to_dict(csv_file)
print(json.dumps(data))