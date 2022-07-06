from cgi import test


test_set = {"apple", "banana", "cherry", "apple", True, 1, 13, 0, False, None, (0, 2, False, True)} 
test_set2 = set(("apple", "banana", "cherry", "kieszen"))
#0 i False traktowane tak samo, które napisane pierwsze to zostaje(tak samo z 1 i True)
#nie ma duplikatów
print(test_set) 
print(len(test_set))
print(type(test_set))
print(test_set2) 
print(len(test_set2))
print(type(test_set2))

print("apple" in test_set)
print("jablko" in test_set)
print(test_set - test_set2)
print(test_set | test_set2)
print(test_set & test_set2)
print(test_set ^ test_set2)

a = set("abracadabra")
b = set("abc")
c = {x for x in a if x not in b}
print("C:    ", c)



test_dictionary = {
    "abc": 17,
    "aaa": "A",
    "aaa": "A",
    28: "lalka"
}
#nie ma duplikatów
print(test_dictionary)
print(len(test_dictionary))
print(test_dictionary["abc"], test_dictionary[28])
del test_dictionary[28]
print(test_dictionary)
test_dictionary["abc"] = 27
test_dictionary["xyz"] = "last dance"
test_dictionary[1.2] = -34.73
print(test_dictionary)
print(list(test_dictionary)) #list keyi
del test_dictionary[1.2]
print(sorted(test_dictionary)) #sorted jak są same typy danych ktore mozna porownac (chodzi o keye), wypisuje wtedy je w posortowanej liscie
print(test_dictionary)
print("abc" in test_dictionary) #true
print(27 in test_dictionary) #false
dict1 = {x: x**2 for x in (2, 4, 6, 10)}
print(dict1)
dict1 = dict(whats = "whats", poppyn = 17, bro = 20)
print(dict1)
for key, value in dict1.items():
    print("key: ", key, " value: ", value)

A = ["tic", "tac", "toe"]
for i, v in enumerate(A):
    print(i, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))


T = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(T)
print(T[1:3])
print(T[:6])
print(T[2:])