import os
for index in range(1, 10):
    os.remove(str(index) + '.png')
os.remove('after.png')