a = [1234,
     1243,
     1324,
     1342,
     1423,
     1432,
     2134,
     2143,
     2314,
     2341,
     2413,
     2431,
     3124,
     3142,
     3214,
     3241,
     3412,
     3421,
     4123,
     4132,
     4213,
     4231,
     4312,
     4321]
ast = []
for an in a:
    ast.append(str(an))

for an in ast:
    coms = []

    coms.append((an[:2][::-1] + an[2:], 2))
    coms.append((an[:1] + an[1:3][::-1] + an[3:], 2))
    coms.append((an[:2] + an[2:][::-1], 2))
    coms.append((an[:3][::-1] + an[3:], 3))
    coms.append((an[:1] + an[1:][::-1], 3))
    coms.append((an[::-1], 4))

    for c in coms:
        print(an, *c)
    print()
