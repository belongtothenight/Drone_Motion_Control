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


def print_csv_data_single_row(array, row_number):
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
            pass


def get_csv_data_single_row_adj_element(array, row_number, start_element_number, end_element_number):
    """
    Description:
        Print and return desire elements of single row from the target 2 order array.
    parameter:
        Input:
            array: (str/2nd.arr) Target array name.
            row_number: (int) Target row number.
            start_element_number: (int) First required element index.
            end_element_number: (int) Last required element index.
        Output:
            coordinate_array: (str/arr) Array storing required elements.
            total_row_count: (int) Total number of row in target csv file.
            total_column_count: (int) Total number of column in target csv file.
    Link:
        https://stackoverflow.com/questions/16548668/iterating-over-a-2-dimensional-python-list
        https://stackabuse.com/python-get-number-of-elements-in-a-list/
        https://www.codingem.com/python-how-to-return-multiple-values/
    """
    coordinate_array = []
    total_row_count = len(range(len(array)))
    total_column_count = 12
    # print('read_file.py-> Total row count:' + str(total_row_count))
    # print('read_file.py-> Total column count:' + str(total_column_count))
    i = start_element_number
    if start_element_number >= 0 and end_element_number < total_column_count:
        while start_element_number <= i <= end_element_number:
            '''
            try:
                print('read_file.py-> Printing read data: ' + array[row_number][i])
            except IndexError:
                # print('main.py-> Finished reading data.')
                pass
            '''
            coordinate_array.append(array[row_number][i])
            i += 1
    else:
        print('read_file.py-> Parameter Error!!!')
    return coordinate_array, total_row_count, total_column_count


def read_txt(program, line_number):
    """
    Description:

    parameter:
        Input:
            program: (str) The directory and file name of target file.
            line_number: The line you want to read.
        Output:
            line: (str) The last line read by this function.
    Link:
        https://www.pythontutorial.net/python-basics/python-read-text-file/
    """
    with open(program) as f:
        for i in range(line_number):
            line = f.readline()
            # print('read_file.py-> Line' + str(i) + ': ' + line)
            i += 1
        print('read_file.py-> finished reading txt')
    return line


def line_split(line, index):
    """
    Description:

    parameter:
        Input:

        Output:

    Link:

    """
    txt = line.split()
    #print('read_file.py-> ' + str(txt))
    return txt[index]
