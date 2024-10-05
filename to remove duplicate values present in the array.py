#The function removes duplicate values present in the array
ArrayWithDuplicateValues=eval(input("enter an array :"))
def RemoveDuplicateValuesInArray(ArrayWithDuplicateValues):
    ArrayWithoutDuplicateValues=list(set(ArrayWithDuplicateValues))
    return ArrayWithoutDuplicateValues
print(RemoveDuplicateValuesInArray(ArrayWithDuplicateValues))
