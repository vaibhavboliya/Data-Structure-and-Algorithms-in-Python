def createArray():
    list = []
    return list


def insertAtTheBeginning(list, value):
    # Time Complexity - O(N)
    list.insert(0, value)


def insertAtGivenIndex(list, value, index):
    # Time Complexity - O(N)
    list.insert(index, value)
    return list


def insertAtTheEnd(list, value):
    # Time Complexity = amortized O(1)
    # append single value at the end of the string
    list.append(value)
    return list


def insertMultipleAtTheEnd(list, vallist):
    # Time Complexity - O(N)
    # list in which values need to be added
    list.extend(vallist)
    return list


def removeFromBeginning(list):
    # Time Complexity - O(N)
    # Removes single item from the list
    list.pop(0)
    return list


def removeFromIndex(list, index):
    # Time Complexity - O(N)
    # Removes single item from the list
    del list[index]
    return list


def removeFromEnd(list):
    # Time Complexity - O(1)
    # Removes single item from the list
    list.pop()
    return list


def removeFromValue(list, value):
    # Time Complexity - O(N)
    # Removes single item from the list
    if value in list:
        list.remove(value)
    return list


def searchValue(list, value):
    # Time Complexity - O(N)
    if value in list:
        idx = list.index(value)
        return idx
    return None


def clearList(list):
    # Time Complexity - O(N)
    # removes all the items from the list
    list.clear()
    return list


#deleteList
    # Time Complexity - O(N)
#del(list)


