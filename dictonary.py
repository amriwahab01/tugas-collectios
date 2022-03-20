#contoh membuat dictonary
identitas ={'nama' : 'amri','umur' : '20','tinggi' : '1.40'}


#menamoilkan key dan nilai dictonary
for i in identitas.items():
	print(i)

#mengganti nilai dictonary	
identitas['nama'] = 'zaky'
print(identitas)

#menghapus nilai dictonary
identitas.pop('umur')
print(identitas)

#menambah key dan nilai dictonary
identitas['alamat'] = 'pambusuang'
print(identitas)

