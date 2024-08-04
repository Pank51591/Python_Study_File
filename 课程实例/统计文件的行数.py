file_name = 'datal.txt'
try:
    with open(file_name) as f:
        data = f.readlines()
except FileNotFoundError:
    print(file_name + 'does not exist')
lens = len(data)
print('datal.txt'+' has'+str(lens)+' lines')
