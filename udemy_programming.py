filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for file in filenames:
    file_x = open(file, 'w')
    file_x.write('Hello')
    file_x.close()