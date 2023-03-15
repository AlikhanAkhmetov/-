import re

def virajenie_1 (nomer_glavi :int, nomer_stiha1 :int , nomer_stiha2 :int ,nomer_stiha3 : int, nomer_stiha4 : int ,
                 nomer_stiha5 : int, nomer_stiha6 :int, nomer_stiha7 :int) -> int :
    """Выражение  первого факта = номер главы + номер стиха первого + номер стиха второго и так до последнего стиха включительно"""
    nomer_glavi_str = str (nomer_glavi)
    nomer_stiha_1_str = str (nomer_stiha1)
    nomer_stiha_2_str = str (nomer_stiha2)
    nomer_stiha_3_str = str (nomer_stiha3)
    nomer_stiha_4_str = str (nomer_stiha4)
    nomer_stiha_5_str = str (nomer_stiha5)
    nomer_stiha_6_str = str (nomer_stiha6)
    nomer_stiha_7_str = str (nomer_stiha7)

   

    virajenie_1 = nomer_glavi_str + nomer_stiha_1_str + nomer_stiha_2_str + nomer_stiha_3_str + nomer_stiha_4_str + nomer_stiha_5_str+ nomer_stiha_6_str +nomer_stiha_7_str
    return  int(virajenie_1)
    
def fact_1 (nomer_glavi : int, nomer_stiha1 :int , nomer_stiha2 : int,nomer_stiha3 :int, nomer_stiha4 :int ,
            nomer_stiha5 : int, nomer_stiha6 : int, nomer_stiha7 : int) -> float :
    """Факт 1 = номер главы + номер стиха первого + номер стиха второго и так до последнего стиха включительно потом поделить на 19"""
    nomer_glavi_str = str (nomer_glavi)
    nomer_stiha_1_str = str (nomer_stiha1)
    nomer_stiha_2_str = str (nomer_stiha2)
    nomer_stiha_3_str = str (nomer_stiha3)
    nomer_stiha_4_str = str (nomer_stiha4)
    nomer_stiha_5_str = str (nomer_stiha5)
    nomer_stiha_6_str = str (nomer_stiha6)
    nomer_stiha_7_str = str (nomer_stiha7)

   

    virajenie_1 = nomer_glavi_str + nomer_stiha_1_str + nomer_stiha_2_str + nomer_stiha_3_str + nomer_stiha_4_str + nomer_stiha_5_str+ nomer_stiha_6_str +nomer_stiha_7_str
    
    virajenie_1_float = float (virajenie_1)

    fact1 = virajenie_1_float / 19

    
    return fact1

def kolvo_slov (stih) -> int :
    """Количество слов в стихе"""
    stih_list = stih.split ()
    kolvo_slov = len(stih_list)
    return kolvo_slov

def kolvo_slov_glavi (stih_1 : str, stih_2 :str , stih_3 :str , stih_4 :str, stih_5 :str, stih_6 :str, stih_7 :str ) -> int :
    """Количество слов в главе"""
    a1list = stih_1.split ()
    a2list = stih_2.split ()
    a3list = stih_3.split ()
    a4list = stih_4.split ()
    a5list = stih_5.split ()
    a6list = stih_6.split ()
    a7list = stih_7.split ()

    slova1 = len(a1list)
    slova2 = len(a2list)
    slova3 = len(a3list)
    slova4 = len(a4list)
    slova5 = len(a5list)
    slova6 = len(a6list)
    slova7 = len(a7list)

    kolvo_slov_glavi = slova1 + slova2 +slova3 + slova4 + slova5 + slova6 + slova7
    return kolvo_slov_glavi

def virajenie_2 (stih_1 : str, stih_2 :str , stih_3 :str , stih_4 :str, stih_5 :str, stih_6 :str, stih_7 :str , nomer_glavi : int , kolvo_stihov : int ) -> int :
    """Выражение номер 2 = номер главы + количество стихов в главе + количество слов в главе """
    nomer_glavi_str = str(nomer_glavi)
    kolichestvo_stihov_str = str(kolvo_stihov)
    """Количество слов в главе"""
    a1list = stih_1.split ()
    a2list = stih_2.split ()
    a3list = stih_3.split ()
    a4list = stih_4.split ()
    a5list = stih_5.split ()
    a6list = stih_6.split ()
    a7list = stih_7.split ()

    slova1 = len(a1list)
    slova2 = len(a2list)
    slova3 = len(a3list)
    slova4 = len(a4list)
    slova5 = len(a5list)
    slova6 = len(a6list)
    slova7 = len(a7list)

    kolvo_slov = slova1 + slova2 +slova3 + slova4 + slova5 + slova6 + slova7

    
    kolvo_slov_str = str (kolvo_slov)
    virajenie_2 = nomer_glavi_str + kolichestvo_stihov_str + kolvo_slov_str

    return  int (virajenie_2)

def fact_2 (stih_1 : str, stih_2 :str , stih_3 :str , stih_4 :str, stih_5 :str, stih_6 :str, stih_7 :str , nomer_glavi : int , kolvo_stihov : int ) -> float :
    """Факт номер 2 = (номер главы + количество стихов в главе + количество слов в главе) / 19"""
    nomer_glavi_str = str(nomer_glavi)
    kolichestvo_stihov_str = str(kolvo_stihov)
    """Количество слов в главе"""
    a1list = stih_1.split ()
    a2list = stih_2.split ()
    a3list = stih_3.split ()
    a4list = stih_4.split ()
    a5list = stih_5.split ()
    a6list = stih_6.split ()
    a7list = stih_7.split ()

    slova1 = len(a1list)
    slova2 = len(a2list)
    slova3 = len(a3list)
    slova4 = len(a4list)
    slova5 = len(a5list)
    slova6 = len(a6list)
    slova7 = len(a7list)

    kolvo_slov = slova1 + slova2 +slova3 + slova4 + slova5 + slova6 + slova7

    
    kolvo_slov_str = str (kolvo_slov)
    virajenie_2 = nomer_glavi_str + kolichestvo_stihov_str + kolvo_slov_str

    virajenie_2_float = float (virajenie_2)

    
    fact_2 = virajenie_2_float / 19

    return fact_2

def summa_poryadkovih_nomerov_stihov (nomer_stiha_1 : int, nomer_stiha_2 : int, nomer_stiha_3 : int,
                                      nomer_stiha_4 : int, nomer_stiha_5 : int, nomer_stiha_6 : int, nomer_stiha_7 : int) -> int :
    summa_poryadkovih_nomerov_stihov = nomer_stiha_1 + nomer_stiha_2 + nomer_stiha_3 + nomer_stiha_4 + nomer_stiha_5 + nomer_stiha_6 + nomer_stiha_7
    return summa_poryadkovih_nomerov_stihov

def kolvo_bukv (stih : str) -> int :
    """Считаем количество букв стиха"""
    stroka_bez_probela = re.sub (' ' ,'', stih)
    kolvo_bukv_stiha = len (stroka_bez_probela)
    return kolvo_bukv_stiha

def kolvo_bukv_glavi (stih_1 : str, stih_2 : str, stih_3 : str , stih_4 :str , stih_5 :str , stih_6 :str, stih_7 :str) -> int :
    """Считаем количество букв главы"""
    a1bez = re.sub (' ' ,'', stih_1)
    a2bez = re.sub (' ' ,'', stih_2)
    a3bez = re.sub (' ' ,'', stih_3)
    a4bez = re.sub (' ' ,'', stih_4)
    a5bez = re.sub (' ' ,'', stih_5)
    a6bez = re.sub (' ' ,'', stih_6)
    a7bez = re.sub (' ' ,'', stih_7)


    kolvo_bukv_glavi = len (a1bez) + len (a2bez) + len (a3bez) + len (a4bez) + len (a5bez) +len (a6bez) + len (a7bez)
    return kolvo_bukv_glavi

def spisok_bukv_stiha (stih : str) -> list :
    """Создаем список букв стиха"""
    spisok_bukv_stiha = re.findall (r'[^ ]' , stih)
    return spisok_bukv_stiha
def spisok_cifr_stiha (stih : str) -> list :
    """Создаем список цифр стиха"""
    spisok_bukv_stiha = re.findall (r'[^ ]' , stih)
    
    result_g1 = [elem.replace ('ا' , '1') for elem in spisok_bukv_stiha]
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
    spisok_cifr_stiha = [elem.replace ('آ' , '1') for elem in result_g1]

    return spisok_cifr_stiha

def cifrovoe_znachenie_stiha (stih : str) -> int :
    """Узнаем цифровое значение стиха"""
    spisok_bukv_stiha = re.findall (r'[^ ]' , stih)
    
    result_g1 = [elem.replace ('ا' , '1') for elem in spisok_bukv_stiha]
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
    spisok_cifr_stiha = [elem.replace ('آ' , '1') for elem in result_g1]
    
    spisok_cifr_stiha_int = [int  (x) for x  in spisok_cifr_stiha]
    cifrovoe_znachenie_stiha = sum(spisok_cifr_stiha_int)
    return cifrovoe_znachenie_stiha

def cifrovoe_znachenie_glavi (stih_1 : str, stih_2 : str , stih_3 : str , stih_4 :str, stih_5 :str, stih_6 :str, stih_7 :str) -> int :
    """Считаем числовое значение всей главы"""
    a1a2a3a4a5a6a7 = [stih_1 , stih_2 , stih_3 , stih_4, stih_5, stih_6, stih_7]
    cifrovoe_znachenie_glavi = 0
    for stih in a1a2a3a4a5a6a7 :
        spisok_bukv_stiha = re.findall (r'[^ ]' , stih)
        
        result_g1 = [elem.replace ('ا' , '1') for elem in spisok_bukv_stiha]
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
        spisok_cifr_stiha = [elem.replace ('آ' , '1') for elem in result_g1]
        
        spisok_cifr_stiha_float = [int  (x) for x  in spisok_cifr_stiha]
        cifrovoe_znachenie_stiha = sum(spisok_cifr_stiha_float)
        
        cifrovoe_znachenie_glavi += sum(spisok_cifr_stiha_float)
        
    return cifrovoe_znachenie_glavi

def virajenie_3 (nomer_stiha_1 : int, nomer_stiha_2 : int, nomer_stiha_3 : int, nomer_stiha_4 : int,
                 nomer_stiha_5 : int, nomer_stiha_6 : int, nomer_stiha_7 : int, stih_1 : str, stih_2 : str ,
                 stih_3 : str , stih_4 :str, stih_5 :str, stih_6 :str, stih_7 :str) -> int :
    """Выражение  номер 3: Сумма порядковых номеров стихов + количество слов в главе + количество букв в главе + числовое значение главы"""
    """Определяем сумму номеров стихов"""
    summa_poryadkovih_nomerov_stihov = nomer_stiha_1 + nomer_stiha_2 + nomer_stiha_3 + nomer_stiha_4 + nomer_stiha_5 + nomer_stiha_6 + nomer_stiha_7
    summa_poryadkovih_nomerov_stihov_str = str (summa_poryadkovih_nomerov_stihov)
    """Количество слов в главе"""
    a1list = stih_1.split ()
    a2list = stih_2.split ()
    a3list = stih_3.split ()
    a4list = stih_4.split ()
    a5list = stih_5.split ()
    a6list = stih_6.split ()
    a7list = stih_7.split ()

    slova1 = len(a1list)
    slova2 = len(a2list)
    slova3 = len(a3list)
    slova4 = len(a4list)
    slova5 = len(a5list)
    slova6 = len(a6list)
    slova7 = len(a7list)

    kolvo_slov = slova1 + slova2 +slova3 + slova4 + slova5 + slova6 + slova7

    
    kolvo_slov_str = str (kolvo_slov)

    """Считаем количество букв главы"""
    a1bez = re.sub (' ' ,'', stih_1)
    a2bez = re.sub (' ' ,'', stih_2)
    a3bez = re.sub (' ' ,'', stih_3)
    a4bez = re.sub (' ' ,'', stih_4)
    a5bez = re.sub (' ' ,'', stih_5)
    a6bez = re.sub (' ' ,'', stih_6)
    a7bez = re.sub (' ' ,'', stih_7)


    kolvo_bukv_glavi = len (a1bez) + len (a2bez) + len (a3bez) + len (a4bez) + len (a5bez) +len (a6bez) + len (a7bez)
    kolvo_bukv_glavi_str = str (kolvo_bukv_glavi)

    """Считаем числовое значение всей главы"""
    a1a2a3a4a5a6a7 = [stih_1 , stih_2 , stih_3 , stih_4, stih_5, stih_6, stih_7]
    cifrovoe_znachenie_glavi = 0
    for stih in a1a2a3a4a5a6a7 :
        spisok_bukv_stiha = re.findall (r'[^ ]' , stih)
        
        result_g1 = [elem.replace ('ا' , '1') for elem in spisok_bukv_stiha]
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
        spisok_cifr_stiha = [elem.replace ('آ' , '1') for elem in result_g1]
        
        spisok_cifr_stiha_float = [int  (x) for x  in spisok_cifr_stiha]
        cifrovoe_znachenie_stiha = sum(spisok_cifr_stiha_float)
        
        cifrovoe_znachenie_glavi += sum(spisok_cifr_stiha_float)
    virajenie_3 = summa_poryadkovih_nomerov_stihov_str + kolvo_slov_str + kolvo_bukv_glavi_str + str (cifrovoe_znachenie_glavi)
    return int (virajenie_3)

def fact_3 (nomer_stiha_1 : int, nomer_stiha_2 : int, nomer_stiha_3 : int, nomer_stiha_4 : int,
                 nomer_stiha_5 : int, nomer_stiha_6 : int, nomer_stiha_7 : int, stih_1 : str, stih_2 : str ,
                 stih_3 : str , stih_4 :str, stih_5 :str, stih_6 :str, stih_7 :str) -> float :
    """ِФакт  номер 3: (Сумма порядковых номеров стихов + количество слов в главе + количество букв в главе + числовое значение главы) / 19"""
    """Определяем сумму номеров стихов"""
    summa_poryadkovih_nomerov_stihov = nomer_stiha_1 + nomer_stiha_2 + nomer_stiha_3 + nomer_stiha_4 + nomer_stiha_5 + nomer_stiha_6 + nomer_stiha_7
    summa_poryadkovih_nomerov_stihov_str = str (summa_poryadkovih_nomerov_stihov)
    """Количество слов в главе"""
    a1list = stih_1.split ()
    a2list = stih_2.split ()
    a3list = stih_3.split ()
    a4list = stih_4.split ()
    a5list = stih_5.split ()
    a6list = stih_6.split ()
    a7list = stih_7.split ()

    slova1 = len(a1list)
    slova2 = len(a2list)
    slova3 = len(a3list)
    slova4 = len(a4list)
    slova5 = len(a5list)
    slova6 = len(a6list)
    slova7 = len(a7list)

    kolvo_slov = slova1 + slova2 +slova3 + slova4 + slova5 + slova6 + slova7

    
    kolvo_slov_str = str (kolvo_slov)

    """Считаем количество букв главы"""
    a1bez = re.sub (' ' ,'', stih_1)
    a2bez = re.sub (' ' ,'', stih_2)
    a3bez = re.sub (' ' ,'', stih_3)
    a4bez = re.sub (' ' ,'', stih_4)
    a5bez = re.sub (' ' ,'', stih_5)
    a6bez = re.sub (' ' ,'', stih_6)
    a7bez = re.sub (' ' ,'', stih_7)


    kolvo_bukv_glavi = len (a1bez) + len (a2bez) + len (a3bez) + len (a4bez) + len (a5bez) +len (a6bez) + len (a7bez)
    kolvo_bukv_glavi_str = str (kolvo_bukv_glavi)

    """Считаем числовое значение всей главы"""
    a1a2a3a4a5a6a7 = [stih_1 , stih_2 , stih_3 , stih_4, stih_5, stih_6, stih_7]
    cifrovoe_znachenie_glavi = 0
    for stih in a1a2a3a4a5a6a7 :
        spisok_bukv_stiha = re.findall (r'[^ ]' , stih)
        
        result_g1 = [elem.replace ('ا' , '1') for elem in spisok_bukv_stiha]
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
        spisok_cifr_stiha = [elem.replace ('آ' , '1') for elem in result_g1]
        
        spisok_cifr_stiha_float = [int  (x) for x  in spisok_cifr_stiha]
        cifrovoe_znachenie_stiha = sum(spisok_cifr_stiha_float)
        
        cifrovoe_znachenie_glavi += sum(spisok_cifr_stiha_float)
    virajenie_3 = summa_poryadkovih_nomerov_stihov_str + kolvo_slov_str + kolvo_bukv_glavi_str + str (cifrovoe_znachenie_glavi)
    fact_3 = float (virajenie_3) / 19
    return fact_3



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

        
        print ('Список после превращения в цифры:',result_g1)

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
    print ("Выражение 6 факта: номер главы + количество букв в 1 стихе + количество букв во втором стихе + и так далее до последнего стиха" ,
           virajenie6)
    virajenie6_float = float (virajenie6)
    fact6 = virajenie6_float / 19
    print ("Факт 6: выражение 6 / 19", fact6)
    return print ("Факт 6: выражение 6 / 19", fact6)
