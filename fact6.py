import re
"""Номер суры + количество букв в 1 аяте + количество букв во 2 аяте +
количество букв в 3 аяте + количество букв в 4 аяте + количество букв в 5 аяте +
количество букв в 6 аяте + количество букв в 7 аяте"""

a1 = 'بسم الله الرحمن الرحيم'
a2 = 'الحمد لله رب العلمين'
a3 = 'الرحمن الرحيم'
a4 = 'مالك يوم الدين'
a5 = 'إياك نعبد وإياك نستعين'
a6 = 'اهدنا الصراط المستقيم'
a7 = 'صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين'
a1bez = re.sub (' ' ,'', a1)
a2bez = re.sub (' ' ,'', a2)
a3bez = re.sub (' ' ,'', a3)
a4bez = re.sub (' ' ,'', a4)
a5bez = re.sub (' ' ,'', a5)
a6bez = re.sub (' ' ,'', a6)
a7bez = re.sub (' ' ,'', a7)
a4bez = re.sub ('مالك' , 'ملك' , a4bez)
a6bez = re.sub ('الصراط' , 'الصرط' , a6bez)
a7bez = re.sub ('صراط' , 'صرط' , a7bez)
obsh = len (a1bez) + len (a2bez) + len (a3bez) + len (a4bez) + len (a5bez) +len (a6bez) + len (a7bez)
a1str = str (len (a1bez))
a2str = str (len (a2bez))
a3str = str (len (a3bez))
a4str = str (len (a4bez))
a5str = str (len (a5bez))
a6str = str (len (a6bez))
a7str = str (len (a7bez))
sura1 = str (1)
miracle2 = sura1 + a1str + a2str + a3str + a4str + a5str + a6str + a7str
miracle2after = float (miracle2) / 19

print ('Выражение второго факта:', miracle2)
print ('Результат второго факта:' , miracle2after)


