import re

a7 = 'صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين'
a7bez = re.sub ('صراط' , 'صرط' , a7)
g7 = re.findall (r'[^ ]' , a7bez)

print (g7)

 

result_g7 = [elem.replace ('ا' , '1') for elem in g7]
result_g7 = [elem.replace ('ب' , '2') for elem in result_g7]
result_g7 = [elem.replace ('ت' , '400') for elem in result_g7]
result_g7 = [elem.replace ('ث' , '500') for elem in result_g7]
result_g7 = [elem.replace ('ج' , '3') for elem in result_g7]
result_g7 = [elem.replace ('ح' , '8') for elem in result_g7]
result_g7 = [elem.replace ('د' , '4') for elem in result_g7]
result_g7 = [elem.replace ('ه' , '5') for elem in result_g7]
result_g7 = [elem.replace ('و' , '6') for elem in result_g7]
result_g7 = [elem.replace ('ز' , '7') for elem in result_g7]
result_g7 = [elem.replace ('ط' , '9') for elem in result_g7]
result_g7 = [elem.replace ('ي' , '10') for elem in result_g7]
result_g7 = [elem.replace ('ك' , '20') for elem in result_g7]
result_g7 = [elem.replace ('ل' , '30') for elem in result_g7]
result_g7 = [elem.replace ('م' , '40') for elem in result_g7]
result_g7 = [elem.replace ('ن' , '50') for elem in result_g7]
result_g7 = [elem.replace ('س' , '60') for elem in result_g7]
result_g7 = [elem.replace ('ع' , '70') for elem in result_g7]
result_g7 = [elem.replace ('ف' , '80') for elem in result_g7]
result_g7 = [elem.replace ('ص' , '90') for elem in result_g7]
result_g7 = [elem.replace ('ق' , '100') for elem in result_g7]
result_g7 = [elem.replace ('ر' , '200') for elem in result_g7]
result_g7 = [elem.replace ('ش' , '300') for elem in result_g7]
result_g7 = [elem.replace ('خ' , '600') for elem in result_g7]
result_g7 = [elem.replace ('ذ' , '700') for elem in result_g7]
result_g7 = [elem.replace ('ض' , '800') for elem in result_g7]
result_g7 = [elem.replace ('ظ' , '900') for elem in result_g7]
result_g7 = [elem.replace ('غ' , '1000') for elem in result_g7]
result_g7 = [elem.replace ('إ' , '1') for elem in result_g7]
result_g7 = [elem.replace ('أ' , '1') for elem in result_g7]
result_g7 = [elem.replace ('ح' , '8') for elem in result_g7]

print ('Список после превращения в буквы:',result_g7)

float_result_g7 = [float  (x) for x  in result_g7]
result_g7_print =print ('Сумма числового значения аята 7:',sum(float_result_g7))
