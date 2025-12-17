#1
str = input("Enter any sentence:")
print("a =",str.count('a'))
print("e =",str.count('e'))
print("i =",str.count('i'))
print("o =",str.count('o'))
print("u =",str.count('u'))

#2
a = [1,2,3]
b = [1,456,2]

new_lst = [a for a in a if a not in b] + [b for b in b if b not in a]
print(new_lst)

#3
sentence = input("Enter a random sentence:")
words = sentence.split() # .split() ek sentence ko words me convert krega.
result = {} #empty dictionary 
for word in words:
    result[word] = result.get(word,0) + 1  #.get() one by one word lega or wo kitni bar repeat ho rahe hai wo dekhega(default 0)
print(result)

#4
dict = {
    'a':1,
    'b':2
       }
new_dict = {}
for k in dict: 
    new_dict[dict[k]] = k #keys converted into values
    print(new_dict)

#5
numbers = [10,20,30,40,50]
for number in numbers:
    if number > 40:
        print("max number:" ,number)
    if number < 20:
        print("min number:", number)

numbers =[20,25,30,35,45]
min_num = numbers[0]
max_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print("min numbers:", min_num)
print("max numbers:", max_num)

#6
lst = [10,10,20,20,30,30,40,40,50,50]
remove_duplicate = []
for i in lst:
    if i not in remove_duplicate:
        remove_duplicate.append(i)
print(remove_duplicate)

#7
my_tuple = (10,20,30,40,50)
a,b,*_,last = my_tuple
print(a)
print(b)
print(last)

#8
dict1 = {'a':2 , 'b':3}
dict2 = {'a':5 , 'c':10}
merged_dict = {}
for k in dict1:
    merged_dict[k] = dict1[k]
for k in dict2:
    if k in merged_dict:
        merged_dict[k] += dict2[k]
    else:
        merged_dict[k] = dict2[k]
print(merged_dict)

#9
string = input("Enter any sentence:")
if string == string[::-1]:
    print('string is palindrome')
else:
    print('not palindrome')

#10
str1 = input("Enter first string:")
str2 = input("Enter second string:")
set1 = set(str1)
set2 = set(str2)
print(set1)
print(set2)
common_char = set1 &set2
print("common_char:", common_char)

















 














 

