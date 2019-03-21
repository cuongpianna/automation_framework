import csv


def get_csv_data(file_name):
    """
    read data from csv and return list
    :param file_name: some csv path string
    :return: list data
    """
    rows = []
    data_file = open(file_name, 'r', encoding='utf8')
    reader = csv.reader(data_file)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows