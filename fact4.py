import re

#четвертый факт состоит из номера суры, количества аятов, количеств слов в каждом аяте

numsura = str (1)
kolvoayatov = str (7)
ayat1 = str (4)
ayat2 = str (4)
ayat3 = str (2)
ayat4 = str (3)
ayat5 = str (4)
ayat6 = str (3)
ayat7 = str (9)

virajeniefact4 = numsura +kolvoayatov +ayat1 +ayat2 +ayat3 +ayat4 +ayat5 +ayat6 +ayat7
print ('Выражение факт 4 :',virajeniefact4)

virafact4float = float (virajeniefact4)

fact4 = virafact4float / 19

print ('Факт 4:',fact4)
