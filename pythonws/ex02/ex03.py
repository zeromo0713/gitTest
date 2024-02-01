a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
b = dict(a)
print(a)
print(b)
print("a  : {}, b  {}".format(id(a),id(b)))
a['alice'].append(30)
print("==============================")
print(a)
print(b)
print("a  : {}, b  {}".format(id(a),id(b)))


name = ['bob','tony','suzy']
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
print(a)
a.update({name[0]:a[name[0]]-5, 'tony':a['tony']-5, 'suzy': a['suzy']-5})
print(a)
