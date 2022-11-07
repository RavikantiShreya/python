l= [8, 1, 7, 10, 5]
min, max = l[0], l[0]
for i in range(1, len(l)):
	if l[i] < min:
		min = l[i]
	if l[i] > max:
		max=l[i]
print('Minimum Element in the list', l, 'is', min)
print('Maximum Element in the list', l, 'is', max)
