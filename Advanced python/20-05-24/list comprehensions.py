## LIST COMPREHENSION

# remove float numbers from a list
l = [1.2, 0, 1, 23, 4.12, 56, 3.4, 9.0]

l1 = [i for i in l if type(i)==int]

print(l1)

# count the no. of spaces in a string
s = 'I am Sowmya Gowri Sri'
l1 = [i for i in s if i==' ']
print(len(l1))

# find the common elements in 2 lists
l1 = [1,5,3,2,7]
l2 = [65,3,2,9]

l = [i for i in l1 if i in l2]
print(l)

# consonants in a string
vowels = ['a', 'e', 'i', 'o', 'u']
l = [i for i in s.lower() if i not in vowels if i!=' ']
print(l)