
a="@"
print(ord(a)) #ord give unicode of variable a
 # → 65  (Unicode of A)
 #    # → "A" (Character from Unicode)
#indexing
# forward indexing = 0 1 2 3 4......
# reverse index=     ...... -2 -1
A ="college"
print(A[2],A[-5], A[5])    
# string slicing
# string[start : stop : step] — note that stop index is excluded.
a="waste"
print(a[1:4:1]) # to print ast
print(a[0:5:2]) # to print w s e 
print(a[0::2])
print(a[ : : ])
# type conversion