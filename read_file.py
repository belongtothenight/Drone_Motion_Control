import csv


def read_csv(program):
    """
    Description:
        Read data from input file.
    Parameter:
        Input:
            program: (str) File directory and file name of target csv file.
        Output:
            return: (str/2nd.arr) Array of read data. (If the file include header, it will be included)
    Link:
        https://stackoverflow.com/questions/56870272/how-to-execute-another-python-file-and-then-close-the-existing-one/56871072#56871072
        https://realpython.com/python-return-statement/
    """
    file = open(program)
    print('read_file.py-> csv file opened')
    csvreader = csv.reader(file)
    print('read_file.py-> csv file read')
    rows = []
    for row in csvreader:
        rows.append(row)
    print('read_file.py-> coordinate data appended')
    # print(rows)
    file.close()
    return rows


def print_csv_data(array, row_number):
    """
    Description:
        Print out all the elements of single row from the target 2 order array.
    parameter:
        Input:
            array: (str/2nd.arr) Target array name.
            row_number: (int) Target row number.
        Output:
            None
    Link:
        https://stackoverflow.com/questions/16548668/iterating-over-a-2-dimensional-python-list
    """
    for i in range(len(array)):
        try:
            print('read_file.py-> Printing read data: ' + array[row_number][i])
        except IndexError:
            # print('main.py-> Finished reading data.')
            break
