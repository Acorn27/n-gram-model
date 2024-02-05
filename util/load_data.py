import csv

def load_csv(file_name):

    try:
        f = open(file_name)
    except FileNotFoundError as err:
        print("Failed to open '{file_name}'")
        return None

    lines = csv.reader(f)
    dataset = list(lines)
    f.close()
    return dataset