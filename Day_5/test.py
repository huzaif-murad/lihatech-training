# f=open('a.txt')

# data=f.read()
# print(data)

#readline() - read only one line

f=open('a.txt')

# for i in range(3):
#     print(f.readline())

# readlinea() - read all Lines from the file as a [str]

# data=f.readlines()
# print(data)
# image_path="./img.png"

# f=open(image_path,'r+b')
# data=f.read()
# print(data)

# path2="a.png"
# j=open(path2,'w+b')
# f.write(data)
# Assignment - create a new image file by using above binary data

with open('new_3.txt','w') as f:
    f.write('sample data')
    print("Inside check",f.closed)
print('Outside check:',f.closed)