import re

#третий факт суры Аль Фатиха
# состоит в  том что записывается в ряд сумма порядковых номеров аятов,
# количество слов в суре, количество букв в суре, и числовое значение суры\
# все значения переменных взяты из предыдущих расчетов

poryadkovisumma = str (28)
kolvoslov = str (29)
kolvobukv = str (139)
gemasuri1  = str (10143)

virajenie = poryadkovisumma + kolvoslov + kolvobukv + gemasuri1

print ('Выражение третьего факта:',virajenie)

virajeniefloat = float (virajenie)

fact3 = virajeniefloat / 19

print ('факт 3 :',fact3)
