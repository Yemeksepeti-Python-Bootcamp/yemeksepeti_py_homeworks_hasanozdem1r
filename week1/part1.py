# 1.Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız
get_text_len = lambda text : len(text)
print(get_text_len('Mustafa Kemal Atatürk'))
# 2.Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız
get_char_of_text= lambda text : print(f'İlk iki karakter : {text[:2]} ve son iki karakter : {text[-1,-3,-1]}')
print("Mustafa Kemal Atatürk")

# 3.Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız
change_letter = lambda text,old,new : print(text.replace(old,new))
change_letter("Mustafa Kemal Atatürk",'ü','u')

# 4.Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız.
def is_palindrom(text:str):
    for i in range(len(text)//2):
        if text[i]!=text[-i-1]:
            print('It is not palindrome')
            break
    else:
        print('It is a palindrome')
is_palindrom('ADAA')

# 5.Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. * aritmetik operatöründen faydalanabilirsiniz.
multiple_letters= lambda text : print(f'{text}{text[-1:-3:-1]*4}')
multiple_letters('hasan')

# 6. 5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız.
numbers=[i for i in range(5)]
numbers[1]=100
print(numbers)

# 7. İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız liste1 = [1,2,3] liste2 = [4,5,6] liste3 = ????? """
numbers=[i for i in range(5)]
numbers2=[i for i in range(10)]
# append usage
def merge_append(num1,num2):
    for i in num1:
        num2.append(i)
    print(num2)
merge_append(numbers,numbers2)
# extend usage
numbers.extend(numbers2)
print(numbers)
# plus usage
print(numbers+numbers2)

#  8. Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız
nums={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# get the last
last_item=list(nums.keys())[-1]
last_value=nums[last_item]
nums.pop(last_item)
print(f'({last_value}:{last_item})')

# 9. Sözlüğe eleman ekleme
nums[7]=70

# 10. Sözlük oluştur {key:key*10}
dict_10x={i:i*10 for i in range(10)}

# 11 Setdefault
dict_10x.setdefault(11,110)
