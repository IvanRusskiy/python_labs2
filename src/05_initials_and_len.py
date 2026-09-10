fio = input()
ini = ''
c = 0
fio = fio.split()
for i in fio:
    ini += i[0]
    c += len(i)
print(ini,c + 2)
