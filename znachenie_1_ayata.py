import re

g1 = re.findall (r'[^ ]' , 'بسم الله الرحمن الرحيم')
print (g1)

 

result_g1 = [elem.replace ('ا' , '1') for elem in g1]
result_g1 = [elem.replace ('ب' , '2') for elem in result_g1]
result_g1 = [elem.replace ('ت' , '400') for elem in result_g1]
result_g1 = [elem.replace ('ث' , '500') for elem in result_g1]
result_g1 = [elem.replace ('ج' , '3') for elem in result_g1]
result_g1 = [elem.replace ('ح' , '8') for elem in result_g1]
result_g1 = [elem.replace ('د' , '4') for elem in result_g1]
result_g1 = [elem.replace ('ه' , '5') for elem in result_g1]
result_g1 = [elem.replace ('و' , '6') for elem in result_g1]
result_g1 = [elem.replace ('ز' , '7') for elem in result_g1]
result_g1 = [elem.replace ('ط' , '9') for elem in result_g1]
result_g1 = [elem.replace ('ي' , '10') for elem in result_g1]
result_g1 = [elem.replace ('ك' , '20') for elem in result_g1]
result_g1 = [elem.replace ('ل' , '30') for elem in result_g1]
result_g1 = [elem.replace ('م' , '40') for elem in result_g1]
result_g1 = [elem.replace ('ن' , '50') for elem in result_g1]
result_g1 = [elem.replace ('س' , '60') for elem in result_g1]
result_g1 = [elem.replace ('ع' , '70') for elem in result_g1]
result_g1 = [elem.replace ('ف' , '80') for elem in result_g1]
result_g1 = [elem.replace ('ص' , '90') for elem in result_g1]
result_g1 = [elem.replace ('ق' , '100') for elem in result_g1]
result_g1 = [elem.replace ('ر' , '200') for elem in result_g1]
result_g1 = [elem.replace ('ش' , '300') for elem in result_g1]
result_g1 = [elem.replace ('خ' , '600') for elem in result_g1]
result_g1 = [elem.replace ('ذ' , '700') for elem in result_g1]
result_g1 = [elem.replace ('ض' , '800') for elem in result_g1]
result_g1 = [elem.replace ('ظ' , '900') for elem in result_g1]
result_g1 = [elem.replace ('غ' , '1000') for elem in result_g1]
result_g1 = [elem.replace ('ح' , '8') for elem in result_g1]
result_g1 = [elem.replace ('ح' , '8') for elem in result_g1]
result_g1 = [elem.replace ('ح' , '8') for elem in result_g1]
print ('Список после превращения в буквы:',result_g1)

#Функция для замены нескольких значений
def multiple_replace (ayat1, replace_values) :
    #получаем заменяемое: подставляемое из словаря в цикле
    for i , j in replace_values.items () :
        ayat1 = 'بسم الله الرحمن الرحيم'
        replace_values = {"ا" : "1" , "ب" : "2" , "ج" : "3" , "د" : "4" , "ه" : "5" , "و" : "6" , "ز" : "7" , "ح" : "8" , "ط" : "9" ,
                  "ي" : "10" , "ك" : "20" , "ل" : "30" , "م" : "40" , "ن" : "50" , "س" : "60" , "ع" : "70" , "ف" : "80",
                  "ص" : "90" , "ق" : "100" , "ر" : "200" , "ش" : "300" , "ت" : "400" , "ث" : "500" , "خ" : "600" , "ذ" : "700" ,
                  "ض" : "800" , "ظ" : "900" , "غ" : "1000"}
        #меняем все target_str.replace (i, j)
        ayat2 = ayat1.replace (i ,j)
    return print (ayat2)
#создаем словарь со значениями и строку, которую будет изменять
replace_values = {"ا" : "1" , "ب" : "2" , "ج" : "3" , "د" : "4" , "ه" : "5" , "و" : "6" , "ز" : "7" , "ح" : "8" , "ط" : "9" ,
                  "ي" : "10" , "ك" : "20" , "ل" : "30" , "م" : "40" , "ن" : "50" , "س" : "60" , "ع" : "70" , "ف" : "80",
                  "ص" : "90" , "ق" : "100" , "ر" : "200" , "ش" : "300" , "ت" : "400" , "ث" : "500" , "خ" : "600" , "ذ" : "700" ,
                  "ض" : "800" , "ظ" : "900" , "غ" : "1000"}
ayat1 = 'بسم الله الرحمن الرحيم'
#Изменяем и печатаем строку
#print (multiple_replace (ayat1, replace_values))
def zamena (ayat , zameni) :
    for k, v in zameni.items :
        for i in ayat :
            if i == k:
                ayat = ayat.replace (i , v)

#zamena (ayat1 , replace_values)


float_result_g1 = [float  (x) for x  in result_g1]
print ('Сумма числового значения аята:',sum(float_result_g1))
