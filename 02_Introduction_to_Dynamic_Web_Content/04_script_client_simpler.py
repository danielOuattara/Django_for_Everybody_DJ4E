import urllib.request

file_hand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')
for line in file_hand:
    print(line.decode().strip())
