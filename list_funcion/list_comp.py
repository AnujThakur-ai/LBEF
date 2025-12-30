#list
l = ['Hello', 'world','lbef','collage']
l2 = [[i, len(i)] for i in l]
print(l2)


l4 = ['Australia', 'India', 'USA', 'UK', 'Newzealand', 'Germany', 'France', 'Italy']
vol = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
l5 = [i for i in l4 if i.startswith(tuple(vol))]
print('\nList of countries having vowels:\n', l5)



