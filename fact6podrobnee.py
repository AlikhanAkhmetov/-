import re

a1 = 'بسم الله الرحمن الرحيم'
a2 = 'الحمد لله رب العلمين'
a3 = 'الرحمن الرحيم'
a4 = 'مالك يوم الدين'
a5 = 'إياك نعبد وإياك نستعين'
a6 = 'اهدنا الصراط المستقيم'
a7 = 'صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين'

#print ('symbols a1')
#print (len(a1))

a1bez = re.sub (' ' ,'', a1)
print ('symbols a1bez')
print (len (a1bez))

a2bez = re.sub (' ' ,'', a2)
a3bez = re.sub (' ' ,'', a3)
a4bez = re.sub (' ' ,'', a4)
a5bez = re.sub (' ' ,'', a5)
a6bez = re.sub (' ' ,'', a6)
a7bez = re.sub (' ' ,'', a7)

a4bez = re.sub ('مالك' , 'ملك' , a4bez)
a6bez = re.sub ('الصراط' , 'الصرط' , a6bez)
a7bez = re.sub ('صراط' , 'صرط' , a7bez)
print ('symbols a2bez')
print (len (a2bez))

print ('symbols a3bez')
print (len (a3bez))

print ('symbols a4bez')
print (len (a4bez))

print ('symbols a5bez')
print (len (a5bez))

print ('symbols a6bez')
print (len (a6bez))

print ('symbols a7bez')
print (len (a7bez))

obsh = len (a1bez) + len (a2bez) + len (a3bez) + len (a4bez) + len (a5bez) +len (a6bez) + len (a7bez)
print ('obshaya simboly')
print ( obsh )


a1str = str (len (a1bez))
a2str = str (len (a2bez))
a3str = str (len (a3bez))
a4str = str (len (a4bez))
a5str = str (len (a5bez))
a6str = str (len (a6bez))
a7str = str (len (a7bez))

sura1 = str (1)

print (sura1, type (sura1))

miracle6 = sura1 + a1str + a2str + a3str + a4str + a5str + a6str + a7str
miracle6after = float (miracle6) / 19
print ('sura1 +count words in 1 ayat + in 2 ayat + in 3 ayat + in 4 ayat + in 5 ayat + in 6 ayat + + in 7 ayat')
print (miracle6)
print ('Miracle 6:')
print (miracle6after)



