import csv

def load_csv(file_name):
    f = open(file_name)
    lines = csv.reader(f)
    dataset = list(lines)
    dataset = list(line[0] for line in dataset)
    f.close()
    return dataset