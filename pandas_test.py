import pandas as pd
import os


# data = pd.read_csv('output_list.txt', header = None)
# print(data)


name = 'output_as'
filename = os.path.join(name + '.html')
# sys.stdout = open(filename, 'w', encoding='utf8')
data_columns = ["NAME", "SPEED", "ID", "IPV4", "IPV6"]
data = pd.read_csv('output_as.txt', delimiter="|", header=None, names=data_columns, encoding='utf8')
print(data)
#
# data.to_csv(filename)





