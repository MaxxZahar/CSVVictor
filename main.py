import os

directory = os.path.join(os.getcwd(), 'data')
for filename in os.listdir(directory):
    if (filename.endswith('.csv')):
        with open(os.path.join(directory, filename), encoding='utf-8') as f:
            operation = f.readline()
            f.readline()
            for line in f:
                line = f.readline()
                if (line):
                    line = line.replace('\n', '')
                    dateList = line.split(';')
                    print(dateList)
