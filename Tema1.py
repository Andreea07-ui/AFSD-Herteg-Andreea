s1='Rezultatele unui studiu clinic realizat în America de Nord arată că testul a fost capabil să identifice o gamă largă de tipuri de cancer, dintre care trei sferturi nu beneficiază de niciun program de screening.'
#Use string slicing to split the string into first and second half
s2=[len(s1)//2+len(s1)%2]
s3=[len(s1)//2+len(s2)%2]
print('First half',s2)
print('Second half',s3)
print('First half',(s1[:105]))
print('Second half',(s1[106:]))
first='Rezultatele unui studiu clinic realizat în America de Nord arată că testul a fost capabil să identifice o'
maj=first.upper()
print(maj)
first1=" ".join(maj.split())
print(first1)
second='gamă largă de tipuri de cancer, dintre care trei sferturi nu beneficiază de niciun program de screening.'
inverted=second[::-1]
print(inverted)
maj1=second.capitalize()
print(maj1)
second1=inverted.replace('.','')
print(second1)
final=first1+second1
print(final)