import re

sura1 = 1

ayat1 = 1

ayat2 = 2
ayat3 = 3
ayat4 = 4
ayat5 = 5
ayat6 = 6
ayat7 = 7

print ( ayat1 , type (ayat1))

sura1str = str (sura1)
ayat1str = str (ayat1)

ayat2str = str (ayat2)
ayat3str = str (ayat3)
ayat4str = str (ayat4)
ayat5str = str (ayat5)
ayat6str = str (ayat6)
ayat7str = str (ayat7)

print (ayat2str , type (ayat2str))

miracle1 = sura1str + ayat1str + ayat2str + ayat3str + ayat4str + ayat5str+ ayat6str +ayat7str

print ('Сложение строки из номеров аятов' ,miracle1, type (miracle1))

miracle1float = float (miracle1)

fact1 = miracle1float / 19

print ('Первое чудо:',fact1, type (fact1))


ayat1_float = float(ayat1)
ayat2_float = float(ayat2)
ayat3_float = float(ayat3)
ayat4_float = float(ayat4)
ayat5_float = float(ayat5)
ayat6_float = float(ayat6)
ayat7_float = float(ayat7)

print ('Проверка для сложения',ayat7_float , type (ayat7_float))
sum_nomerov_ayatov = ayat1_float + ayat2_float + ayat3_float  + ayat4_float + ayat5_float + ayat6_float + ayat7_float

print ('Сумма номеров аятов суры 1:',sum_nomerov_ayatov)

