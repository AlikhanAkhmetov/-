import re

def miracle1 (nomer_glavi, nomer_stiha1 , nomer_stiha2 ,nomer_stiha3, nomer_stiha4 , nomer_stiha5, nomer_stiha6, nomer_stiha7) :
    """Алгоритм номер 1 = номер главы + номер стиха первого + номер стиха второго и так до последнего стиха включительно"""
    nomer_glavi_str = str (nomer_glavi)
    nomer_stiha_1_str = str (nomer_stiha1)
    nomer_stiha_2_str = str (nomer_stiha2)
    nomer_stiha_3_str = str (nomer_stiha3)
    nomer_stiha_4_str = str (nomer_stiha4)
    nomer_stiha_5_str = str (nomer_stiha5)
    nomer_stiha_6_str = str (nomer_stiha6)
    nomer_stiha_7_str = str (nomer_stiha7)

    print (nomer_stiha_1_str , type (nomer_stiha_1_str))

    virajenie1 = nomer_glavi_str + nomer_stiha_1_str + nomer_stiha_2_str + nomer_stiha_3_str + nomer_stiha_4_str + nomer_stiha_5_str+ nomer_stiha_6_str +nomer_stiha_7_str

    print ('Сложение строки из номеров стихов' ,virajenie1, type (virajenie1))

    virajenie_1_float = float (virajenie1)

    fact1 = virajenie_1_float / 19

    print ('Первый факт (номер главы + номера стиха 1 + номер стиха 2 + остальные номера стихов/19):',fact1, type (fact1))
    return fact1


def miracle2 (stih1 , stih2 , stih3 , stih4, stih5, stih6, stih7 , nomer_glavi , kolichestvo_stihov ) :
    """Алгоритм номер 2 = номер главы + количество стихов в главе + количество слов в главе / 19"""
    nomer_glavi_str = str(nomer_glavi)
    kolichestvo_stihov_str = str(kolichestvo_stihov)
    a1list = stih1.split ()
    a2list = stih2.split ()
    a3list = stih3.split ()
    a4list = stih4.split ()
    a5list = stih5.split ()
    a6list = stih6.split ()
    a7list = stih7.split ()

    print ('1 stih:' ,len(a1list))
    print ('2 stih:' ,len(a2list))
    print ('3 stih:' ,len(a3list))
    print ('4 stih:' ,len(a4list))
    print ('5 stih:' ,len(a5list))
    print ('6 stih:' ,len(a6list))
    print ('7 stih:' ,len(a7list))

    slova1 = len(a1list)
    slova2 = len(a2list)
    slova3 = len(a3list)
    slova4 = len(a4list)
    slova5 = len(a5list)
    slova6 = len(a6list)
    slova7 = len(a7list)

    obsheeslova = slova1 + slova2 +slova3 + slova4 + slova5 + slova6 + slova7

    print ('Количество слов в главе:',obsheeslova)
    obsheeslovastr = str (obsheeslova)

    virajenie2 = nomer_glavi_str + kolichestvo_stihov_str + obsheeslovastr

    virajenie_2_float = float (virajenie2)

    print ('Выражение Второго алгоритма Номер главы + количество стихов + количество слов в главе:' , virajenie2 )
    fact2 = virajenie_2_float / 19

    print ('Второй алгоритм(Номер главы + количество стихов + количество слов в главе)/19 :' , fact2)
    return fact2



def miracle3 (nomer_stiha1, nomer_stiha2, nomer_stiha3, nomer_stiha4, nomer_stiha5, nomer_stiha6, nomer_stiha7,stih1, stih2, stih3 , stih4 , stih5 , stih6, stih7) :
    """Алгоритм  номер 3: Сумма порядковых номеров стихов + количество слов в главе + количество букв в главе + числовое значение главы"""
    """Определяем сумму номеров стихов"""
    stih1_float = float(nomer_stiha1)
    stih2_float = float(nomer_stiha2)
    stih3_float = float(nomer_stiha3)
    stih4_float = float(nomer_stiha4)
    stih5_float = float(nomer_stiha5)
    stih6_float = float(nomer_stiha6)
    stih7_float = float(nomer_stiha7)
    sum_nomerov_stihov = stih1_float + stih2_float + stih3_float  + stih4_float + stih5_float + stih6_float + stih7_float

    print ('Сумма номеров стихов главы 1:',sum_nomerov_stihov)
    sum_nomerov_stihov_str = str (int(sum_nomerov_stihov))

    """Считаем количество слов"""
    a1list = stih1.split ()
    a2list = stih2.split ()
    a3list = stih3.split ()
    a4list = stih4.split ()
    a5list = stih5.split ()
    a6list = stih6.split ()
    a7list = stih7.split ()

    print ('1 stih:' ,len(a1list))
    print ('2 stih:' ,len(a2list))
    print ('3 stih:' ,len(a3list))
    print ('4 stih:' ,len(a4list))
    print ('5 stih:' ,len(a5list))
    print ('6 stih:' ,len(a6list))
    print ('7 stih:' ,len(a7list))

    slova1 = len(a1list)
    slova2 = len(a2list)
    slova3 = len(a3list)
    slova4 = len(a4list)
    slova5 = len(a5list)
    slova6 = len(a6list)
    slova7 = len(a7list)

    obsheeslova = slova1 + slova2 +slova3 + slova4 + slova5 + slova6 + slova7

    print ('Количество слов в главе:',obsheeslova)
    obshee_slova_str = str (obsheeslova)

    """Считаем количество букв"""
    a1bez = re.sub (' ' ,'', stih1)
    print ('symbols a1bez')
    print (len (a1bez))

    a2bez = re.sub (' ' ,'', stih2)
    a3bez = re.sub (' ' ,'', stih3)
    a4bez = re.sub (' ' ,'', stih4)
    a5bez = re.sub (' ' ,'', stih5)
    a6bez = re.sub (' ' ,'', stih6)
    a7bez = re.sub (' ' ,'', stih7)


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

    obshee_bukvi = len (a1bez) + len (a2bez) + len (a3bez) + len (a4bez) + len (a5bez) +len (a6bez) + len (a7bez)
    print ('obshaya simboly')
    print ( obshee_bukvi )
    obshee_bukvi_str = str (obshee_bukvi)

    """Считаем числовое значение всей главы"""
    a1a2a3a4a5a6a7 = [stih1 , stih2 , stih3 , stih4, stih5, stih6, stih7]
    float_result_vse_znacheniya = 0
    for g1stroka in a1a2a3a4a5a6a7 :
        g1 = re.findall (r'[^ ]' , g1stroka)
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
        result_g1 = [elem.replace ('ؤ' , '6') for elem in result_g1]
        result_g1 = [elem.replace ('ئ' , '10') for elem in result_g1]
        result_g1 = [elem.replace ('ى' , '10') for elem in result_g1]
        """Хамза не имеет цифрового значения"""
        result_g1 = [elem.replace ('ء' , '0') for elem in result_g1]
        """Та марбута не имеет цифрового значения"""
        result_g1 = [elem.replace ('ة' , '0') for elem in result_g1]
        result_g1 = [elem.replace ('أ' , '1') for elem in result_g1]
        result_g1 = [elem.replace ('إ' , '1') for elem in result_g1]
        result_g1 = [elem.replace ('آ' , '1') for elem in result_g1]

        
        print ('Список после превращения в буквы:',result_g1)

        float_result_g1 = [float  (x) for x  in result_g1]
        print ('Сумма числового значения стиха:',sum(float_result_g1))
        
        float_result_vse_znacheniya += sum(float_result_g1)
        print ('Сумма числовых значений всей главы:', float_result_vse_znacheniya)
        str_result_vse_znacheniya = str(int(float_result_vse_znacheniya))
    
    virajenie = sum_nomerov_stihov_str + obshee_slova_str + obshee_bukvi_str + str_result_vse_znacheniya

    print ('Выражение третьего алгоритма (сумма номеров стихов + количество слов в главе + количество букв в главе + числовое значение всей главы',virajenie)

    virajeniefloat = float (virajenie)

    fact3 = virajeniefloat / 19

    print ('факт 3 (выражение третьего алгоритма /19) :',fact3)
    return print ('факт 3 (выражение третьего алгоритма /19) :',fact3)

def miracle4 (nomer_glavi,kolichestvo_stihov,stih1 ,stih2 ,stih3 , stih4, stih5, stih6 ,stih7) :
    """Номер главы + количество стихов + количество слов в первом стихе + количество слов во втором стихе и так далее до последнего стиха включительно"""
    nomer_glavi_str = str(nomer_glavi)
    kolichestvo_stihov_str = str (kolichestvo_stihov)
    
    """Считаем количество слов"""
    a1list = stih1.split ()
    a2list = stih2.split ()
    a3list = stih3.split ()
    a4list = stih4.split ()
    a5list = stih5.split ()
    a6list = stih6.split ()
    a7list = stih7.split ()

    print ('1 стих:' ,len(a1list))
    print ('2 стих:' ,len(a2list))
    print ('3 стих:' ,len(a3list))
    print ('4 стих:' ,len(a4list))
    print ('5 стих:' ,len(a5list))
    print ('6 стих:' ,len(a6list))
    print ('7 стих:' ,len(a7list))

    slova1 = str (len(a1list))
    slova2 = str (len(a2list))
    slova3 = str (len(a3list))
    slova4 = str (len(a4list))
    slova5 = str (len(a5list))
    slova6 = str (len(a6list))
    slova7 = str (len(a7list))

    """Делаем выражение"""
    virajeniefact4 = nomer_glavi_str + kolichestvo_stihov_str +slova1 +slova2 +slova3 + slova4 + slova5 +slova6 + slova7
    print ("Выражение  4 (Номер главы + количество стихов +количество слов"
           "в первом стихе + количество слов во втором стихе и так далее"
           "до последнего стиха включительно) :",virajeniefact4)

    virafact4float = float (virajeniefact4)

    fact4 = virafact4float / 19

    print ('Факт 4 (выражение 4 / 19):',fact4)
    return fact4

def miracle5 (nomer_glavi,kolichestvo_stihov, stih1, stih2,
              stih3, stih4 ,stih5 ,stih6, stih7) :
    """Выражение факта 5 = номер главы + количество стихов +
    количество букв в главе + числовое значение главы"""
    nomer_glavi_str = str(nomer_glavi)
    kolichestvo_stihov_str = str (kolichestvo_stihov)
    """Считаем количество букв"""
    a1bez = re.sub (' ' ,'', stih1)
    print ('symbols a1bez')
    print (len (a1bez))

    a2bez = re.sub (' ' ,'', stih2)
    a3bez = re.sub (' ' ,'', stih3)
    a4bez = re.sub (' ' ,'', stih4)
    a5bez = re.sub (' ' ,'', stih5)
    a6bez = re.sub (' ' ,'', stih6)
    a7bez = re.sub (' ' ,'', stih7)


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

    obshee_bukvi = len (a1bez) + len (a2bez) + len (a3bez) + len (a4bez) + len (a5bez) +len (a6bez) + len (a7bez)
    print ('obshaya simboly')
    print ( obshee_bukvi )
    obshee_bukvi_str = str (obshee_bukvi)

    """Считаем числовое значение всей главы"""
    a1a2a3a4a5a6a7 = [stih1 , stih2 , stih3 , stih4, stih5, stih6, stih7]
    float_result_vse_znacheniya = 0
    for g1stroka in a1a2a3a4a5a6a7 :
        g1 = re.findall (r'[^ ]' , g1stroka)
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
        result_g1 = [elem.replace ('ؤ' , '6') for elem in result_g1]
        result_g1 = [elem.replace ('ئ' , '10') for elem in result_g1]
        result_g1 = [elem.replace ('ى' , '10') for elem in result_g1]
        """Хамза не имеет цифрового значения"""
        result_g1 = [elem.replace ('ء' , '0') for elem in result_g1]
        """Та марбута не имеет цифрового значения"""
        result_g1 = [elem.replace ('ة' , '0') for elem in result_g1]
        result_g1 = [elem.replace ('أ' , '1') for elem in result_g1]
        result_g1 = [elem.replace ('إ' , '1') for elem in result_g1]
        result_g1 = [elem.replace ('آ' , '1') for elem in result_g1]

        
        print ('Список после превращения в буквы:',result_g1)

        float_result_g1 = [float  (x) for x  in result_g1]
        print ('Сумма числового значения стиха:',sum(float_result_g1))
        
        float_result_vse_znacheniya += sum(float_result_g1)
    print ('Сумма числовых значений всей главы:', float_result_vse_znacheniya)
    str_result_vse_znacheniya = str(int(float_result_vse_znacheniya))

    virajenie5 = nomer_glavi_str + kolichestvo_stihov_str + obshee_bukvi_str + str_result_vse_znacheniya
    print ('Выражение факта 5 = номер главы + количество стихов + количество букв в главе + числовое значение главы:' , virajenie5)

    virajenie5_float = float (virajenie5)
    fact5 = virajenie5_float / 19

    print ('Факт 5 (выражение факта5 / 19):' , fact5)

    return fact5

def miracle6 (nomer_glavi , stih1, stih2, stih3 , stih4, stih5, stih6, stih7) :
    """Выражение 6 факта = номер главы + количество букв в 1 стихе + количество букв во 2 стихе и так до последнего стиха включительно"""
    nomer_glavi_str = str(nomer_glavi)
    """Считаем количество букв"""
    a1bez = re.sub (' ' ,'', stih1)
    print ('symbols a1bez')
    print (len (a1bez))

    a2bez = re.sub (' ' ,'', stih2)
    a3bez = re.sub (' ' ,'', stih3)
    a4bez = re.sub (' ' ,'', stih4)
    a5bez = re.sub (' ' ,'', stih5)
    a6bez = re.sub (' ' ,'', stih6)
    a7bez = re.sub (' ' ,'', stih7)

    bukvi1_str = str(len(a1bez))
    bukvi2_str = str(len(a2bez))
    bukvi3_str = str(len(a3bez))
    bukvi4_str = str(len(a4bez))
    bukvi5_str = str(len(a5bez))
    bukvi6_str = str(len(a6bez))
    bukvi7_str = str(len(a7bez))
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

    virajenie6 = nomer_glavi_str + bukvi1_str + bukvi2_str + bukvi3_str + bukvi4_str + bukvi5_str + bukvi6_str + bukvi7_str
    print ("Выражение 6 факта: номер главы + количество букв в 1 стихе + количество букв во втором стихе + и так далее до последнего стиха" , virajenie6)

    virajenie6_float = float (virajenie6)
    fact6 = virajenie6_float / 19
    print ("Факт 6: выражение 6 / 19", fact6)
    return fact6
