import os

directory = os.path.join(os.getcwd(), 'data')
days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


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
                        print(dateList)
                        if (dateList[month - 1] and int(dateList[month - 1]) == day):
                            operationList.append(operation)
                            break
    if (operationList):
        return operationList
    else:
        return 'В этот день никакие операции не выполнялись'


print(get_data(11, 17))
