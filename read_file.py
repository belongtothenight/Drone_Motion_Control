import csv


def read_csv(program):
    """
    Description:
        Read data from input file.
    Parameter:
        Input:
            program: (str) File directory and file name of target csv file.
        Output:
            return: (str/arr) Array of read data. (If the file include header, it will be included)
    Link:
        https://stackoverflow.com/questions/56870272/how-to-execute-another-python-file-and-then-close-the-existing-one/56871072#56871072
        https://realpython.com/python-return-statement/
    """
    file = open(program)
    print('read_file.py: csv file opened')
    csvreader = csv.reader(file)
    print('read_file.py: csv file read')
    rows = []
    for row in csvreader:
        rows.append(row)
    print('read_file.py: coordinate data appended')
    #print(rows)
    file.close()
    return rows