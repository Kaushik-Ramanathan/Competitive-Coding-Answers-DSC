#This program inputs a string and the function returns the string sorted in ascending order of the length of the words
string=input("enter a sentence:")
def ArrangeWordsInAscendingOrderByLength(string):
    SortedList=string.split()
    SortedStringInAscOrder= " "
    SortedListByLength=sorted(SortedList, key=len)
    for Word in SortedListByLength:
        SortedStringInAscOrder+=  Word + '  '

    SortedStringInAscOrder= SortedStringInAscOrder.strip()
    return SortedStringInAscOrder

print(ArrangeWordsInAscendingOrderByLength(string))




    
