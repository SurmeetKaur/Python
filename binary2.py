from os import strerror

data = bytearray(20)

for i in range(len(data)):
    data[i] = 20 - i

try:
    bf = open('file2.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
try:
    bf = open('file2.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in range(len(data)):
        print(data[b], end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
