from flask import Flask, render_template, request, redirect, escape
from miracles import virajenie_1 , fact_1 , kolvo_slov , kolvo_slov_glavi , virajenie_2, fact_2 , summa_poryadkovih_nomerov_stihov
from miracles import kolvo_bukv , kolvo_bukv_glavi , spisok_bukv_stiha, spisok_cifr_stiha, cifrovoe_znachenie_stiha, cifrovoe_znachenie_glavi
from miracles import virajenie_3 , fact_3

app = Flask (__name__)

@app.route ('/')
@app.route ('/entry')
def entry_page () -> 'html' :
    return render_template ('entry.html' ,
                            the_title = 'Попытка увидеть пока не стало поздно')

@app.route ('/googled7833cc9ffb86fa9.html')
def google_autentification () -> 'html' :
    return render_template ('googled7833cc9ffb86fa9.html')


@app.route ('/results' , methods = ['POST'])
def results () -> 'html' :
    stih_1_fatiha = 'بسم الله الرحمن الرحيم'
    stih_2_fatiha = 'الحمد لله رب العلمين'
    stih_3_fatiha = 'الرحمن الرحيم'
    stih_4_fatiha = 'ملك يوم الدين'
    stih_5_fatiha = 'إياك نعبد وإياك نستعين'
    stih_6_fatiha = 'اهدنا الصرط المستقيم'
    stih_7_fatiha = 'صرط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين'
    nomer_glavi_fatiha = 1
    number_stih_1_fatiha = 1
    number_stih_2_fatiha = 2
    number_stih_3_fatiha = 3
    number_stih_4_fatiha = 4
    number_stih_5_fatiha = 5
    number_stih_6_fatiha = 6
    number_stih_7_fatiha = 7
    kolvo_stihov_glavi_fatiha_backend = 7
    kolvo_stihov_glavi_user = 7
    nomer_glavi = request.form ['nomer_glavi']
    stih1 = str (request.form ['stih_1'])
    stih2 = str (request.form ['stih_2'])
    stih3 = str (request.form ['stih_3'])
    stih4 = str (request.form ['stih_4'])
    stih5 = str (request.form ['stih_5'])
    stih6 = str (request.form ['stih_6'])
    stih7 = str (request.form ['stih_7'])
    number_stih_1 = request.form ['number_stih_1']
    number_stih_2 = request.form ['number_stih_2']
    number_stih_3 = request.form ['number_stih_3']
    number_stih_4 = request.form ['number_stih_4']
    number_stih_5 = request.form ['number_stih_5']
    number_stih_6 = request.form ['number_stih_6']
    number_stih_7 = request.form ['number_stih_7']
    virajenie_1_fatiha = virajenie_1 (nomer_glavi_fatiha , number_stih_1_fatiha, number_stih_2_fatiha, number_stih_3_fatiha, number_stih_4_fatiha,
                                      number_stih_5_fatiha, number_stih_6_fatiha, number_stih_7_fatiha)
    
    fact_1_fatiha = fact_1 (nomer_glavi_fatiha , number_stih_1_fatiha, number_stih_2_fatiha, number_stih_3_fatiha, number_stih_4_fatiha,
                            number_stih_5_fatiha, number_stih_6_fatiha, number_stih_7_fatiha)
    
    virajenie_1_user = virajenie_1 ( nomer_glavi, number_stih_1 , number_stih_2, number_stih_3 , number_stih_4 , number_stih_5 ,
                                     number_stih_6 , number_stih_7)
    
    fact_1_user = fact_1 (nomer_glavi, number_stih_1 , number_stih_2, number_stih_3 , number_stih_4 , number_stih_5 ,
                          number_stih_6 , number_stih_7)
    kolvo_slov_1_fatiha_backend = kolvo_slov (stih_1_fatiha)
    kolvo_slov_2_fatiha_backend = kolvo_slov (stih_2_fatiha)
    kolvo_slov_3_fatiha_backend = kolvo_slov (stih_3_fatiha)
    kolvo_slov_4_fatiha_backend = kolvo_slov (stih_4_fatiha)
    kolvo_slov_5_fatiha_backend = kolvo_slov (stih_5_fatiha)
    kolvo_slov_6_fatiha_backend = kolvo_slov (stih_6_fatiha)
    kolvo_slov_7_fatiha_backend = kolvo_slov (stih_7_fatiha)

    virajenie_2_fatiha_backend = virajenie_2 (stih_1_fatiha, stih_2_fatiha, stih_3_fatiha, stih_4_fatiha, stih_5_fatiha, stih_6_fatiha,
                                              stih_7_fatiha, nomer_glavi_fatiha, kolvo_stihov_glavi_fatiha_backend)
    
    fact_2_fatiha_backend = fact_2 (stih_1_fatiha, stih_2_fatiha, stih_3_fatiha, stih_4_fatiha, stih_5_fatiha, stih_6_fatiha,
                                    stih_7_fatiha, nomer_glavi_fatiha, kolvo_stihov_glavi_fatiha_backend)
    kolvo_slov_glavi_fatiha_backend = kolvo_slov_glavi (stih_1_fatiha, stih_2_fatiha, stih_3_fatiha, stih_4_fatiha, stih_5_fatiha, stih_6_fatiha, stih_7_fatiha)


    kolvo_slov_1_user = kolvo_slov (stih1)
    kolvo_slov_2_user = kolvo_slov (stih2)
    kolvo_slov_3_user = kolvo_slov (stih3)
    kolvo_slov_4_user = kolvo_slov (stih4)
    kolvo_slov_5_user = kolvo_slov (stih5)
    kolvo_slov_6_user = kolvo_slov (stih6)
    kolvo_slov_7_user = kolvo_slov (stih7)

    kolvo_slov_glavi_user = kolvo_slov_glavi (stih1, stih2, stih3, stih4, stih5, stih6, stih7)

    virajenie_2_user = virajenie_2 (stih1, stih2, stih3, stih4, stih5, stih6, stih7,nomer_glavi, kolvo_stihov_glavi_user)
    fact_2_user = fact_2 (stih1, stih2, stih3, stih4, stih5, stih6, stih7,nomer_glavi, kolvo_stihov_glavi_user)

    sum_poryadkovih_nomerov_fatiha_backend = summa_poryadkovih_nomerov_stihov (number_stih_1_fatiha, number_stih_2_fatiha, number_stih_3_fatiha, number_stih_4_fatiha,
                                                                               number_stih_5_fatiha, number_stih_6_fatiha, number_stih_7_fatiha)

    kolvo_bukv_1_fatiha_backend = kolvo_bukv (stih_1_fatiha)
    kolvo_bukv_2_fatiha_backend = kolvo_bukv (stih_2_fatiha)
    kolvo_bukv_3_fatiha_backend = kolvo_bukv (stih_3_fatiha)
    kolvo_bukv_4_fatiha_backend = kolvo_bukv (stih_4_fatiha)
    kolvo_bukv_5_fatiha_backend = kolvo_bukv (stih_5_fatiha)
    kolvo_bukv_6_fatiha_backend = kolvo_bukv (stih_6_fatiha)
    kolvo_bukv_7_fatiha_backend = kolvo_bukv (stih_7_fatiha)
    kolvo_bukv_glavi_fatiha_backend = kolvo_bukv_glavi (stih_1_fatiha, stih_2_fatiha, stih_3_fatiha, stih_4_fatiha, stih_5_fatiha, stih_6_fatiha, stih_7_fatiha)


    spisok_bukv_1_fatiha_backend = spisok_bukv_stiha (stih_1_fatiha)
    spisok_bukv_2_fatiha_backend = spisok_bukv_stiha (stih_2_fatiha)
    spisok_bukv_3_fatiha_backend = spisok_bukv_stiha (stih_3_fatiha)
    spisok_bukv_4_fatiha_backend = spisok_bukv_stiha (stih_4_fatiha)
    spisok_bukv_5_fatiha_backend = spisok_bukv_stiha (stih_5_fatiha)
    spisok_bukv_6_fatiha_backend = spisok_bukv_stiha (stih_6_fatiha)
    spisok_bukv_7_fatiha_backend = spisok_bukv_stiha (stih_7_fatiha)

    spisok_bukv_cifr_1_fatiha_backend = spisok_cifr_stiha (stih_1_fatiha)
    spisok_bukv_cifr_2_fatiha_backend = spisok_cifr_stiha (stih_2_fatiha)
    spisok_bukv_cifr_3_fatiha_backend = spisok_cifr_stiha (stih_3_fatiha)
    spisok_bukv_cifr_4_fatiha_backend = spisok_cifr_stiha (stih_4_fatiha)
    spisok_bukv_cifr_5_fatiha_backend = spisok_cifr_stiha (stih_5_fatiha)
    spisok_bukv_cifr_6_fatiha_backend = spisok_cifr_stiha (stih_6_fatiha)
    spisok_bukv_cifr_7_fatiha_backend = spisok_cifr_stiha (stih_7_fatiha)

    сifr_znach_1_fatiha_backend = cifrovoe_znachenie_stiha (stih_1_fatiha)
    сifr_znach_2_fatiha_backend = cifrovoe_znachenie_stiha (stih_2_fatiha)
    сifr_znach_3_fatiha_backend = cifrovoe_znachenie_stiha (stih_3_fatiha)
    сifr_znach_4_fatiha_backend = cifrovoe_znachenie_stiha (stih_4_fatiha)
    сifr_znach_5_fatiha_backend = cifrovoe_znachenie_stiha (stih_5_fatiha)
    сifr_znach_6_fatiha_backend = cifrovoe_znachenie_stiha (stih_6_fatiha)
    сifr_znach_7_fatiha_backend = cifrovoe_znachenie_stiha (stih_7_fatiha)

    cifr_znach_glavi_fatiha_backend = cifrovoe_znachenie_glavi (stih_1_fatiha, stih_2_fatiha, stih_3_fatiha, stih_4_fatiha,
                                                                stih_5_fatiha, stih_6_fatiha, stih_7_fatiha)


    the_virajenie_3_fatiha_backend = virajenie_3 (number_stih_1_fatiha, number_stih_2_fatiha, number_stih_3_fatiha, number_stih_4_fatiha,
                                                  number_stih_5_fatiha, number_stih_6_fatiha, number_stih_7_fatiha, stih_1_fatiha,
                                                  stih_2_fatiha, stih_3_fatiha, stih_4_fatiha, stih_5_fatiha, stih_6_fatiha, stih_7_fatiha)

    
    the_results_3_fatiha_backend = fact_3 (number_stih_1_fatiha, number_stih_2_fatiha, number_stih_3_fatiha, number_stih_4_fatiha,
                                           number_stih_5_fatiha, number_stih_6_fatiha, number_stih_7_fatiha, stih_1_fatiha,
                                           stih_2_fatiha, stih_3_fatiha, stih_4_fatiha, stih_5_fatiha, stih_6_fatiha, stih_7_fatiha)

    
    sum_poryadkovih_nomerov_backend = summa_poryadkovih_nomerov_stihov (int (number_stih_1), int (number_stih_2), int (number_stih_3), int (number_stih_4),
                                                                        int (number_stih_5), int (number_stih_6), int (number_stih_7))

    kolvo_bukv_1_user = kolvo_bukv (stih1)
    kolvo_bukv_2_user = kolvo_bukv (stih2)
    kolvo_bukv_3_user = kolvo_bukv (stih3)
    kolvo_bukv_4_user = kolvo_bukv (stih4)
    kolvo_bukv_5_user = kolvo_bukv (stih5)
    kolvo_bukv_6_user = kolvo_bukv (stih6)
    kolvo_bukv_7_user = kolvo_bukv (stih7)

    kolvo_bukv_glavi_user = kolvo_bukv_glavi (stih1, stih2, stih3, stih4, stih5, stih6, stih7)

    spisok_bukv_1_user = spisok_bukv_stiha (stih1)
    spisok_bukv_2_user = spisok_bukv_stiha (stih2)
    spisok_bukv_3_user = spisok_bukv_stiha (stih3)
    spisok_bukv_4_user = spisok_bukv_stiha (stih4)
    spisok_bukv_5_user = spisok_bukv_stiha (stih5)
    spisok_bukv_6_user = spisok_bukv_stiha (stih6)
    spisok_bukv_7_user = spisok_bukv_stiha (stih7)

    spisok_bukv_cifr_1_user = spisok_cifr_stiha (stih1)
    spisok_bukv_cifr_2_user = spisok_cifr_stiha (stih2)
    spisok_bukv_cifr_3_user = spisok_cifr_stiha (stih3)
    spisok_bukv_cifr_4_user = spisok_cifr_stiha (stih4)
    spisok_bukv_cifr_5_user = spisok_cifr_stiha (stih5)
    spisok_bukv_cifr_6_user = spisok_cifr_stiha (stih6)
    spisok_bukv_cifr_7_user = spisok_cifr_stiha (stih7)

    сifr_znach_1_user = cifrovoe_znachenie_stiha (stih1)
    сifr_znach_2_user = cifrovoe_znachenie_stiha (stih2)
    сifr_znach_3_user = cifrovoe_znachenie_stiha (stih3)
    сifr_znach_4_user = cifrovoe_znachenie_stiha (stih4)
    сifr_znach_5_user = cifrovoe_znachenie_stiha (stih5)
    сifr_znach_6_user = cifrovoe_znachenie_stiha (stih6)
    сifr_znach_7_user = cifrovoe_znachenie_stiha (stih7)

    cifr_znach_glavi_user = cifrovoe_znachenie_glavi (stih1, stih2, stih3, stih4, stih5, stih6, stih7)

    the_virajenie_3_user = virajenie_3 (int (number_stih_1), int (number_stih_2), int (number_stih_3), int (number_stih_4),
                                        int (number_stih_5), int (number_stih_6), int (number_stih_7), stih1, stih2, stih3,
                                        stih4, stih5, stih6, stih7)

    the_results_3_user = fact_3 (int (number_stih_1), int (number_stih_2), int (number_stih_3), int (number_stih_4),
                                 int (number_stih_5), int (number_stih_6), int (number_stih_7), stih1, stih2, stih3,
                                 stih4, stih5, stih6, stih7)



    
    return render_template ('results.html' ,
                            the_title = 'Ваши результаты',
                            the_nomer_glavi_fatiha = nomer_glavi_fatiha,
                            the_number_stih_1_fatiha = number_stih_1_fatiha,
                            the_number_stih_2_fatiha = number_stih_2_fatiha,
                            the_number_stih_3_fatiha = number_stih_3_fatiha,
                            the_number_stih_4_fatiha = number_stih_4_fatiha,
                            the_number_stih_5_fatiha = number_stih_5_fatiha,
                            the_number_stih_6_fatiha = number_stih_6_fatiha,
                            the_number_stih_7_fatiha = number_stih_7_fatiha,
                            the_virajenie_1_fatiha = virajenie_1_fatiha,
                            the_results_1_fatiha = fact_1_fatiha,
                            the_virajenie_1 = virajenie_1_user,
                            the_results_1 = fact_1_user,
                            kolvo_slov_1_fatiha = kolvo_slov_1_fatiha_backend,
                            kolvo_slov_2_fatiha = kolvo_slov_2_fatiha_backend,
                            kolvo_slov_3_fatiha = kolvo_slov_3_fatiha_backend,
                            kolvo_slov_4_fatiha = kolvo_slov_4_fatiha_backend,
                            kolvo_slov_5_fatiha = kolvo_slov_5_fatiha_backend,
                            kolvo_slov_6_fatiha = kolvo_slov_6_fatiha_backend,
                            kolvo_slov_7_fatiha = kolvo_slov_7_fatiha_backend,

                            kolvo_slov_glavi_fatiha = kolvo_slov_glavi_fatiha_backend,
                            kolvo_stihov_glavi_fatiha = kolvo_stihov_glavi_fatiha_backend,

                            the_virajenie_2_fatiha = virajenie_2_fatiha_backend,
                            the_results_2_fatiha = fact_2_fatiha_backend,

                            kolvo_slov_1 = kolvo_slov_1_user,
                            kolvo_slov_2 = kolvo_slov_2_user,
                            kolvo_slov_3 = kolvo_slov_3_user,
                            kolvo_slov_4 = kolvo_slov_4_user,
                            kolvo_slov_5 = kolvo_slov_5_user,
                            kolvo_slov_6 = kolvo_slov_6_user,
                            kolvo_slov_7 = kolvo_slov_7_user,
                            the_kolvo_slov_glavi = kolvo_slov_glavi_user,
                            the_kolvo_stihov_glavi = kolvo_stihov_glavi_user,

                            the_virajenie_2 = virajenie_2_user,
                            the_results_2 = fact_2_user,

                            sum_poryadkovih_nomerov_fatiha = sum_poryadkovih_nomerov_fatiha_backend,

                            kolvo_bukv_1_fatiha = kolvo_bukv_1_fatiha_backend,
                            kolvo_bukv_2_fatiha = kolvo_bukv_2_fatiha_backend,
                            kolvo_bukv_3_fatiha = kolvo_bukv_3_fatiha_backend,
                            kolvo_bukv_4_fatiha = kolvo_bukv_4_fatiha_backend,
                            kolvo_bukv_5_fatiha = kolvo_bukv_5_fatiha_backend,
                            kolvo_bukv_6_fatiha = kolvo_bukv_6_fatiha_backend,
                            kolvo_bukv_7_fatiha = kolvo_bukv_7_fatiha_backend,
                            kolvo_bukv_glavi_fatiha = kolvo_bukv_glavi_fatiha_backend,


                            spisok_bukv_1_fatiha = spisok_bukv_1_fatiha_backend,
                            spisok_bukv_2_fatiha = spisok_bukv_2_fatiha_backend,
                            spisok_bukv_3_fatiha = spisok_bukv_3_fatiha_backend,
                            spisok_bukv_4_fatiha = spisok_bukv_4_fatiha_backend,
                            spisok_bukv_5_fatiha = spisok_bukv_5_fatiha_backend,
                            spisok_bukv_6_fatiha = spisok_bukv_6_fatiha_backend,
                            spisok_bukv_7_fatiha = spisok_bukv_7_fatiha_backend,

                            spisok_bukv_cifr_1_fatiha = spisok_bukv_cifr_1_fatiha_backend,
                            spisok_bukv_cifr_2_fatiha = spisok_bukv_cifr_2_fatiha_backend,
                            spisok_bukv_cifr_3_fatiha = spisok_bukv_cifr_3_fatiha_backend,
                            spisok_bukv_cifr_4_fatiha = spisok_bukv_cifr_4_fatiha_backend,
                            spisok_bukv_cifr_5_fatiha = spisok_bukv_cifr_5_fatiha_backend,
                            spisok_bukv_cifr_6_fatiha = spisok_bukv_cifr_6_fatiha_backend,
                            spisok_bukv_cifr_7_fatiha = spisok_bukv_cifr_7_fatiha_backend,

                            сifr_znach_1_fatiha = сifr_znach_1_fatiha_backend,
                            сifr_znach_2_fatiha = сifr_znach_2_fatiha_backend,
                            сifr_znach_3_fatiha = сifr_znach_3_fatiha_backend,
                            сifr_znach_4_fatiha = сifr_znach_4_fatiha_backend,
                            сifr_znach_5_fatiha = сifr_znach_5_fatiha_backend,
                            сifr_znach_6_fatiha = сifr_znach_6_fatiha_backend,
                            сifr_znach_7_fatiha = сifr_znach_7_fatiha_backend,

                            cifr_znach_glavi_fatiha = cifr_znach_glavi_fatiha_backend,
                            
                            the_virajenie_3_fatiha = the_virajenie_3_fatiha_backend,
                            the_results_3_fatiha = the_results_3_fatiha_backend,

                            sum_poryadkovih_nomerov = sum_poryadkovih_nomerov_backend,

                            kolvo_bukv_1 = kolvo_bukv_1_user,
                            kolvo_bukv_2 = kolvo_bukv_2_user,
                            kolvo_bukv_3 = kolvo_bukv_3_user,
                            kolvo_bukv_4 = kolvo_bukv_4_user,
                            kolvo_bukv_5 = kolvo_bukv_5_user,
                            kolvo_bukv_6 = kolvo_bukv_6_user,
                            kolvo_bukv_7 = kolvo_bukv_7_user,

                            kolvo_bukv_glavi = kolvo_bukv_glavi_user,

                            spisok_bukv_1 = spisok_bukv_1_user,
                            spisok_bukv_2 = spisok_bukv_2_user,
                            spisok_bukv_3 = spisok_bukv_3_user,
                            spisok_bukv_4 = spisok_bukv_4_user,
                            spisok_bukv_5 = spisok_bukv_5_user,
                            spisok_bukv_6 = spisok_bukv_6_user,
                            spisok_bukv_7 = spisok_bukv_7_user,

                            spisok_bukv_cifr_1 = spisok_bukv_cifr_1_user,
                            spisok_bukv_cifr_2 = spisok_bukv_cifr_2_user,
                            spisok_bukv_cifr_3 = spisok_bukv_cifr_3_user,
                            spisok_bukv_cifr_4 = spisok_bukv_cifr_4_user,
                            spisok_bukv_cifr_5 = spisok_bukv_cifr_5_user,
                            spisok_bukv_cifr_6 = spisok_bukv_cifr_6_user,
                            spisok_bukv_cifr_7 = spisok_bukv_cifr_7_user,

                            сifr_znach_1 = сifr_znach_1_user,
                            сifr_znach_2 = сifr_znach_2_user,
                            сifr_znach_3 = сifr_znach_3_user,
                            сifr_znach_4 = сifr_znach_4_user,
                            сifr_znach_5 = сifr_znach_5_user,
                            сifr_znach_6 = сifr_znach_6_user,
                            сifr_znach_7 = сifr_znach_7_user,

                            cifr_znach_glavi = cifr_znach_glavi_user,

                            the_virajenie_3 = the_virajenie_3_user,
                            the_results_3 = the_results_3_user,
                            
                            



                            
                            the_nomer_glavi = nomer_glavi,
                            the_stih_1 = stih1,
                            the_stih_2 = stih2,
                            the_stih_3 = stih3,
                            the_stih_4 = stih4,
                            the_stih_5 = stih5,
                            the_stih_6 = stih6,
                            the_stih_7 = stih7,
                            the_number_stih_1 = number_stih_1,
                            the_number_stih_2 = number_stih_2,
                            the_number_stih_3 = number_stih_3,
                            the_number_stih_4 = number_stih_4,
                            the_number_stih_5 = number_stih_5,
                            the_number_stih_6 = number_stih_6,
                            the_number_stih_7 = number_stih_7,
                            the_results = results,)

if __name__  == '__main__' :
        app.run(debug=True)
