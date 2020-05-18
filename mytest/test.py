import tlsh

filename1 = "./1.txt"
filename2 = "./2.txt"

with open(filename1, 'rb') as file1:
    data1 = file1.read()
hv1 = tlsh.hash(data1)
print hv1
with open(filename2, 'rb') as file2:
    data2 = file2.read()
hv2 = tlsh.hash(data2)
print hv2
