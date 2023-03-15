import re

a6 = 'اهدنا الصراط المستقيم'
a6bez = re.sub ('الصراط' , 'الصرط' , a6)
g6 = re.findall (r'[^ ]' , a6bez)

print (g6)

 

result_g6 = [elem.replace ('ا' , '1') for elem in g6]
result_g6 = [elem.replace ('ب' , '2') for elem in result_g6]
result_g6 = [elem.replace ('ت' , '400') for elem in result_g6]
result_g6 = [elem.replace ('ث' , '500') for elem in result_g6]
result_g6 = [elem.replace ('ج' , '3') for elem in result_g6]
result_g6 = [elem.replace ('ح' , '8') for elem in result_g6]
result_g6 = [elem.replace ('د' , '4') for elem in result_g6]
result_g6 = [elem.replace ('ه' , '5') for elem in result_g6]
result_g6 = [elem.replace ('و' , '6') for elem in result_g6]
result_g6 = [elem.replace ('ز' , '7') for elem in result_g6]
result_g6 = [elem.replace ('ط' , '9') for elem in result_g6]
result_g6 = [elem.replace ('ي' , '10') for elem in result_g6]
result_g6 = [elem.replace ('ك' , '20') for elem in result_g6]
result_g6 = [elem.replace ('ل' , '30') for elem in result_g6]
result_g6 = [elem.replace ('م' , '40') for elem in result_g6]
result_g6 = [elem.replace ('ن' , '50') for elem in result_g6]
result_g6 = [elem.replace ('س' , '60') for elem in result_g6]
result_g6 = [elem.replace ('ع' , '70') for elem in result_g6]
result_g6 = [elem.replace ('ف' , '80') for elem in result_g6]
result_g6 = [elem.replace ('ص' , '90') for elem in result_g6]
result_g6 = [elem.replace ('ق' , '100') for elem in result_g6]
result_g6 = [elem.replace ('ر' , '200') for elem in result_g6]
result_g6 = [elem.replace ('ش' , '300') for elem in result_g6]
result_g6 = [elem.replace ('خ' , '600') for elem in result_g6]
result_g6 = [elem.replace ('ذ' , '700') for elem in result_g6]
result_g6 = [elem.replace ('ض' , '800') for elem in result_g6]
result_g6 = [elem.replace ('ظ' , '900') for elem in result_g6]
result_g6 = [elem.replace ('غ' , '1000') for elem in result_g6]
result_g6 = [elem.replace ('إ' , '1') for elem in result_g6]


print ('Список после превращения в буквы:',result_g6)

float_result_g6 = [float  (x) for x  in result_g6]
result_g6_print =print ('Сумма числового значения аята 6:',sum(float_result_g6))
