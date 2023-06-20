import os

directory = os.path.join(os.getcwd(), 'data')
temp_directory = os.path.join(os.getcwd(), 'temp')
days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
monthes = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
           7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}


def get_data(month, day):
    if (not isinstance(month, int) or not isinstance(day, int)):
        raise ValueError('Either day or month is not integer')
    if (not 0 < month < 13):
        raise ValueError('Such month does not exist')
    if (not 0 < day < days_in_month[month] + 1):
        raise ValueError('Such day does not exist')
    operationList = []
    for filename in os.listdir(directory):
        if (filename.endswith('.csv')):
            with open(os.path.join(directory, filename), encoding='utf-8') as f:
                operation = f.readline()
                operation = operation.replace('\n', '')
                f.readline()
                for line in f:
                    if (line):
                        line = line.replace('\n', '')
                        dateList = line.split(';')
                        if (dateList[month - 1].isnumeric() and int(dateList[month - 1]) == day):
                            operationList.append(operation)
                            break
    if (operationList):
        return operationList
    else:
        return 'В этот день никакие операции не выполнялись'


def clean_temp_directory(directory):
    if (directory[-4:] != 'temp'):
        raise ValueError("Wrong directory!")
    for filename in os.listdir(directory):
        os.remove(os.path.join(directory, filename))


def get_date(month, day):
    if (not isinstance(month, int) or not isinstance(day, int)):
        raise ValueError('Either day or month is not integer')
    if (not 0 < month < 13):
        raise ValueError('Such month does not exist')
    if (not 0 < day < days_in_month[month] + 1):
        raise ValueError('Such day does not exist')
    return f'{day} {monthes[month]}'


def write_data(data, date):
    if (not data):
        raise ValueError("No data to write in the file!")
    clean_temp_directory(temp_directory)
    filename = 'data.txt'
    with open(os.path.join(temp_directory, filename), 'w', encoding='utf-8') as f:
        if (isinstance(data, list)):
            f.write(f'Операции, выполненные {date}\n\n')
            for operation in data:
                f.write(operation + '\n')
        elif (isinstance(data, str)):
            f.write(date + '. ' + data + '\n')
        else:
            raise ValueError("Wrong data format!")


def get_new_data_file(month, day):
    date = get_date(month, day)
    data = get_data(month, day)
    write_data(data, date)


get_new_data_file(11, 17)
