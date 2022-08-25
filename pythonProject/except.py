def myfile():
    try:
        c=open('python.txt','r')
        print(c.read())
    except(FileNotFoundError):
        return('not exists')
emp=myfile()
print(emp)