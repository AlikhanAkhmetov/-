import re

g2 = re.findall (r'[^ ]' , 'الحمد لله رب العلمين')
print (g2)

 

result_g2 = [elem.replace ('ا' , '1') for elem in g2]
result_g2 = [elem.replace ('ب' , '2') for elem in result_g2]
result_g2 = [elem.replace ('ت' , '400') for elem in result_g2]
result_g2 = [elem.replace ('ث' , '500') for elem in result_g2]
result_g2 = [elem.replace ('ج' , '3') for elem in result_g2]
result_g2 = [elem.replace ('ح' , '8') for elem in result_g2]
result_g2 = [elem.replace ('د' , '4') for elem in result_g2]
result_g2 = [elem.replace ('ه' , '5') for elem in result_g2]
result_g2 = [elem.replace ('و' , '6') for elem in result_g2]
result_g2 = [elem.replace ('ز' , '7') for elem in result_g2]
result_g2 = [elem.replace ('ط' , '9') for elem in result_g2]
result_g2 = [elem.replace ('ي' , '10') for elem in result_g2]
result_g2 = [elem.replace ('ك' , '20') for elem in result_g2]
result_g2 = [elem.replace ('ل' , '30') for elem in result_g2]
result_g2 = [elem.replace ('م' , '40') for elem in result_g2]
result_g2 = [elem.replace ('ن' , '50') for elem in result_g2]
result_g2 = [elem.replace ('س' , '60') for elem in result_g2]
result_g2 = [elem.replace ('ع' , '70') for elem in result_g2]
result_g2 = [elem.replace ('ف' , '80') for elem in result_g2]
result_g2 = [elem.replace ('ص' , '90') for elem in result_g2]
result_g2 = [elem.replace ('ق' , '100') for elem in result_g2]
result_g2 = [elem.replace ('ر' , '200') for elem in result_g2]
result_g2 = [elem.replace ('ش' , '300') for elem in result_g2]
result_g2 = [elem.replace ('خ' , '600') for elem in result_g2]
result_g2 = [elem.replace ('ذ' , '700') for elem in result_g2]
result_g2 = [elem.replace ('ض' , '800') for elem in result_g2]
result_g2 = [elem.replace ('ظ' , '900') for elem in result_g2]
result_g2 = [elem.replace ('غ' , '1000') for elem in result_g2]
print ('Список после превращения в буквы:',result_g2)

float_result_g2 = [float  (x) for x  in result_g2]
result_g2_print =print ('Сумма числового значения аята 2:',sum(float_result_g2))
