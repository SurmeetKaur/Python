

# Your code that reads bytes from the stream should go here.
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in range(len(data)):
        print(data[b], end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
