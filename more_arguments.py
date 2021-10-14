
#Default values of parameters
def appendItem(itemName, itemList=None): #default value
    if itemList == None:
          itemList = []
    itemList.append(itemName)
    return itemList
 
 
print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser')) 

# Type hints
def greeting(name: str) -> str:
    return 'Hello ' + name

# https://docs.python.org/3/library/typing.html
