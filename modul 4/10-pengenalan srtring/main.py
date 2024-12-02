# string adalah kumpulan dari karakter

data = "ini adalahh string"
print(data)
print("panjang karakter :",len (data))
print("tipe data :", type (data))

#1.cara membuat string
'''
    1.menggunakan single quote '...'
    2.menggunakan double quote "..."

'''
data ='menggunakan single quote'
print(data)

data ="menggukan double quote"
print(data)

print('"hay,apa kabar "')
print('"hay,apa kabar"')
print('"ini adalah hari jumat"')

#2. mengukan tanda \

#membuat tanda' menjadi string
print('mari solat jum\'at')
print('g\'day,isn\'t it ')

# double backslash
print('c:\\user\\ali')

#tab
print('ali\tkumarudin,lagi sedih')

#backspace
print('ali \bkumar,lagi sad')

#newline
print('baris pertama.\nbaris kedua.')#lf ->line feed ->dipakai unix,macos,linuk
print('baris pertama.\rbaris kedua.')#carriage return ->di pakai commodore,acorn,lisp
print('baris pertama. \r\nbaris kedua.')#crlf -> line feed carriage return -> di pakai windows

#3.string literal atau raw

#hati-hati
print('c:\new folder')


#menggunakan literal string
print("""
Nama : Ali
Kelas: 12 MA"""
)

#multiline literal string dan raw
print(r"""
Nama : Ali 
Kelas : 12 MA \new normal""")

#multiline literal string dan raw
print(r"""
Nama: ali
Kelas: 12 MA \new normal
website: www.ali.com/newID""")













# newline (enter)
print("baris satu.\nbaris dua.")#Lf ->line feed = macos
print("baris saru.\n\nbaris dua.") # CRLF -> WINDOWS

#new strinng
print(r"c \user\adan")