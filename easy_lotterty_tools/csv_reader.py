import csv


def get_result_map(filename):
    with open(filename, 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        idx = 0
        result = {}
        for row in reader:
            if idx > 0:
                result[row[0]] = row[2]
            idx += 1

        return result
