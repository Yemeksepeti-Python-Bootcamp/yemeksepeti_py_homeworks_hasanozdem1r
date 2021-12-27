# hex bin zfill
# ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız.
lectures_dict = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
lec_keys=list(lectures_dict.keys())
lec_keys=[key.replace(' ','') for key in lec_keys]
for new_key,old_key in zip(lec_keys,list(lectures_dict.keys())):
    lectures_dict[new_key] = lectures_dict[old_key]
    lectures_dict.pop(old_key)
print(lectures_dict)

# liste1=[1,2,3] liste2=[4,5,6,7,8] iki listeyi liste3 ile birleştiriniz?
l1=[1,2,3,]
l2=[4,5,6,7,8,]
l3=l1+l2
print(l3)

# liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?
l4=[1,2,3,4,5,6]
l4.pop(0)
print(l4)

# append
fruits=['apple','pear','strawberry']
fruits.append(3)
print(fruits)

# Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız
nums=[i for i in range(10)]
print(max(nums))

# "Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız.
text='D:/my_works/Kodluyoruz YS Python Web Development Bootcamp/task_3.py'
lower_letters=[]
upper_letters=[]
for i in text:
    if i.isupper():
        upper_letters.append(i)
    else:
        lower_letters.append(i)
print(upper_letters,lower_letters)

# kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız.
nums=[i for i in range(10)]
odd_num=0
even_num=0
for i in nums:
    if i%2==0:
        even_num+=1
    else:
        odd_num+=1
print(odd_num,even_num)
