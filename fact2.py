import re

a1 = 'بسم الله الرحمن الرحيم'
a2 = 'الحمد لله رب العلمين'
a3 = 'الرحمن الرحيم'
a4 = 'مالك يوم الدين'
a5 = 'إياك نعبد وإياك نستعين'
a6 = 'اهدنا الصراط المستقيم'
a7 = 'صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين'

a4bez = re.sub ('مالك' , 'ملك' , a4)
a6bez = re.sub ('الصراط' , 'الصرط' , a6)
a7bez = re.sub ('صراط' , 'صرط' , a7)

a1list = a1.split ()
a2list = a2.split ()
a3list = a3.split ()
a4list = a4.split ()
a5list = a5.split ()
a6list = a6.split ()
a7list = a7.split ()

print ('1 ayat:' ,len(a1list))
print ('2 ayat:' ,len(a2list))
print ('3 ayat:' ,len(a3list))
print ('4 ayat:' ,len(a4list))
print ('5 ayat:' ,len(a5list))
print ('6 ayat:' ,len(a6list))
print ('7 ayat:' ,len(a7list))

slova1 = len(a1list)
slova2 = len(a2list)
slova3 = len(a3list)
slova4 = len(a4list)
slova5 = len(a5list)
slova6 = len(a6list)
slova7 = len(a7list)

obsheeslova = slova1 + slova2 +slova3 + slova4 + slova5 + slova6 + slova7

print ('Количество слов в суре:',obsheeslova)
obsheeslovastr = str (obsheeslova)
numbersura = str (1)
kolichestvoayatov = str (7)
miracle2 = numbersura + kolichestvoayatov + obsheeslovastr


miracle2float = float (miracle2)

print ('Выражение Второго алгоритма Номер суры + количество аятов + количество слов в суре:' , miracle2 )
miracle2result = miracle2float / 19

print ('Второй алгоритм(Номер суры + количество аятов + количество слов в суре)/19 :' , miracle2result)




