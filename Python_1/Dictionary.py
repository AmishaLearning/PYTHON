data={1:'Rose',2:'Mary',4:'Marlo'}
print(data)
print(data[4])
# print(data[3])
print(data.get(1))
print(data.get(3,'Not Found'))
print(data.get(1,'Not Found'))

#Merging two lists to a dictionary
keys=['Rose','Mary','Marlo']
values=['Python','java','js']
data1=dict(zip(keys,values))
print(data1)
print(data1['Mary'])

data1['Monika']='CS'
print(data1)
print(data1['Monika'])
del data1['Rose']
print(data1)

prog={'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prog)
print(prog['JS'])
print(prog['Java'])
print(prog['Python'][0])
print(prog['Java']['JEE'])