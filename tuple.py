nama = ('agus','risal','asri')

for i in nama:
	print(i)
	
nama = list(nama)
nama[1] = "aril"
print(nama)

nama.append('rudi')
print(nama)

nama.extend(['amri','robi'])
print(nama)

nama.insert(2,'udin')
print(nama)

del nama[2:5]
print(nama)

nama.remove('agus')
print(nama)