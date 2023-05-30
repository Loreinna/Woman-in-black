#СДЕЛАТЬ ГРОМЧЕ ЗВУКИ МАРУСИ
# Определение персонажей игры.
define v = Character('Ваня', color='#f7e1e3', image='vanya',callback=name_callback, cb_name="vanya")
define p = Character('Петя', color='#d6d5ed', image='petya', callback=name_callback, cb_name="petya")
define mam = Character('Мама', color='#a6748b', image='mama', callback=name_callback, cb_name="mama")
define pap = Character('Папа' , color='#d6d5ed',image='papa', callback=name_callback, cb_name="papa")
define kit = Character('Маруся', color='#db81b3', image='kit')
define va = Character('Василиса', color='#9c1761', image='vasilisa', callback=name_callback, cb_name="vasilisa")
define da = Character('Данил', color='edb2d1',image ='danil')
define n = Character('Надя', color='#f0fdff', image ='nadya', callback=name_callback, cb_name="nadya")
define d = Character("Директор", color='#d7ddde', image='director',callback=name_callback, cb_name="director")
define m = Character("Марина Борисовна", color = "d9d2bf", image='marbar',callback=name_callback, cb_name="marbar")
define an = Character('Аня', color= '#edd5ec', image='anya',callback=name_callback, cb_name="anya")

##Подсветка персонажей###############################################
define a = Character(callback=name_callback, cb_name=None)
image anya rassta =At("anya rasst", sprite_highlight("anya"))
image anyaa=At("anya", sprite_highlight("anya"))
image directora=At("director", sprite_highlight("director"))
image director smilea=At("director smile", sprite_highlight("director"))
image mama angrya=At("mama angry", sprite_highlight("mama"))
image mama bykaa=At("mama byka", sprite_highlight("mama"))
image mama happya=At("mama happy", sprite_highlight("mama"))
image mama normala=At("mama normal", sprite_highlight("mama"))
image mama vostorga=At("mama vostorg", sprite_highlight("mama"))
image marbar normala=At("marbar normal", sprite_highlight("marbar"))
image marbar angrya=At("marbar angry", sprite_highlight("marbar"))
image papa angrya=At("papa angry", sprite_highlight("papa"))
image papa normala=At("papa normal", sprite_highlight("papa"))
image papa happya=At("papa happy", sprite_highlight("papa"))
image petya angrya=At("petya angry", sprite_highlight("petya"))
image petya fufa=At("petya fuf", sprite_highlight("petya"))
image petya gigaa=At("petya giga", sprite_highlight("petya"))
image petya happya=At("petya happy", sprite_highlight("petya"))
image petya v kur angrya=At("petya v kur angry", sprite_highlight("petya"))
image petya v kur happya=At("petya v kur happy", sprite_highlight("petya"))
image petya v kur rassta=At("petya v kur rasst", sprite_highlight("petya"))
image petya v kur rastera=At("petya v kur raster", sprite_highlight("petya"))
image vasilisa angrya=At("vasilisa angry", sprite_highlight("vasilisa"))
image vasilisa bykaa=At("vasilisa byka", sprite_highlight("vasilisa"))
image vasilisa happya=At("vasilisa happy", sprite_highlight("vasilisa"))
image vasilisa smysa=At("vasilisa smys", sprite_highlight("vasilisa"))
image vasilisa v kur angrya=At("vasilisa v kur angry", sprite_highlight("vasilisa"))
image vasilisa v kur happya=At("vasilisa v kur happy", sprite_highlight("vasilisa"))
image vasilisa v kur rassta=At("vasilisa v kur rasst", sprite_highlight("vasilisa"))
image vasilisa v kur rastera=At("vasilisa v kur raster", sprite_highlight("vasilisa"))
image vasilisa v kur smysa=At("vasilisa v kur smys", sprite_highlight("vasilisa"))
image vasilisa volna=At("vasilisa voln", sprite_highlight("vasilisa"))
image vasilisa closeda=At("vasilisa closed", sprite_highlight("vasilisa"))
image vasilisa v kur closeda=At("vasilisa v kur closed", sprite_highlight("vasilisa"))
image vasilisaa=At("vasilisa ", sprite_highlight("vasilisa"))
image vasilisa v kura=At("vasilisa v kur", sprite_highlight("vasilisa"))
image petya v kura=At("petya v kur", sprite_highlight("petya"))
image petya1a=At("petya1", sprite_highlight("petya"))
image petya closeda=At("petya closed", sprite_highlight("petya"))
image petya v kur closeda=At("petya v kur closed", sprite_highlight("petya"))

#ПОСЛЕ КОНЦА НОВЕЛЛЫ СДЕЛАТЬ ПОДСВЕТКУ
#Игровое###################################################

define prochel = False #Прочел ли Ваня смс от Пети или нет
define soglasilsya = False #Соглашается Ваня пойти после уроков к Пете
define otkazalcya = False #Ваня отказывается идти к Пете после уроков
define ne_prochel=False #Ваня игнорирует смс Василины
define ne_pobejal=False#Ваня не побежал за Hадей
define spisal_y_Ani=False
define spisal_y_Vasi=False
define spisal_y_Peti=False
#Анимация##################################################

image vasilisa blink:
    "vasilisaa"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "vasilisa closeda"
    pause 0.2
    repeat

image vasilisa blink1:
    "vasilisa v kura"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "vasilisa v kur closeda"
    pause 0.2
    repeat
    
image vasilisa blink2:

    "vasilisa v kur levo"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "vasilisa v kur closed"
    pause 0.2
    repeat

image petya blink:
    "petya1a"
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "petya closeda"
    pause 0.2
    repeat

image petya blink1:
    "petya v kura"   
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "petya v kur closeda"
    pause 0.2
    repeat
 
image petya blink2:
    "petya v kur pravo"   
    choice:
        pause 2
    choice:
        pause 4
    choice:
        pause 6
    "petya v kur closed"
    pause 0.2
    repeat
    
image sneg_idet:#Под вопросом

    "sneg"
    pause 0.55
    "sneg1"
    pause 0.55
    "sneg2"
    pause 0.55
    "sneg3"
    pause 0.55
    repeat

#Музыка и звуки############################################
define audio.mya = "sounds/mya.ogg"
define audio.mrr = "sounds/kitty-purr.ogg"
define audio.vstal = "sounds/vstal_s_krovati.mp3"
define audio.hmm = "sounds/hmm ot papi.mp3"
define audio.sms = "sounds/sms.ogg"
define audio.na_ulise = "audio/Betatrip compassion.mp3"
define audio.fon_scary = "audio/fon_scary.mp3"
define audio.na_nachalo="audio/Betatrip daydreams.mp3"
define audio.fon_s_nadya="audio/fon_s_Nadya.mp3"
define audio.hod_po_snegy="sounds/hod po snegy.mp3"
define audio.koridor="audio/koridor_v_shkole.mp3"
define audio.zvonok="sounds/schzvon.mp3"
define audio.beg_po_snegy="sounds/beg po snegy.mp3"
define audio.klass="audio/v_klasse.mp3"
define audio.beg_koridor="audio/beg_po_kor.mp3"
define audio.mus_v_kor="audio/music v koridore.mp3"
define audio.dver="sounds/dver.mp3"
define audio.shagi="sounds/shagi.mp3"
define audio.end="audio/end1.mp3"
#define dolgo = dissolve(10.0)
#Расположение############################################## 
init python:#ЭФФЕКТ МОРГАНИЯ
    onn = ImageDissolve("eye.jpg", 0.2, 4, reverse=False) 
    off = ImageDissolve("eye.jpg", 0.2, 4, reverse=True) 
    
init:
    $left2 = Position(xalign=0.2, yalign=1.1)
    $right2 = Position(xalign=0.8, yalign=1.1)
    $right3 = Position(xalign=1.0, yalign=0.6)
    $right4 = Position(xalign=0.5, yalign=-0.3)
    $left3 = Position(xalign= 0.0, yalign=-0.3)
    $right5 = Position(xalign=0.8, yalign=-0.4)
    
# Игра начинается здесь:
label start:
    stop music fadeout 2
    #cцена cна  гг, появление Нади
    scene bg nachalo
    with fade
    
    n "Ваня....."
    
    n "Ваня!....."
    
    show nadya at center
    with dissolve
    
    n "Ваня!"
    
    n"......"
    
    n spina "Гд4е ты, {w=2}В@nя?.."
    
    n spina "......"
    
    n spina "В@Nyaa^a*a"
    
    n spina "......"
    
    n a "Отв..еть, В?аny0a?"
    with vpunch

    scene bg vanya na bed #done
    
    v "Надя!"
    
    a "Я перестал что либо чувсвовать, я больше не мог плакать, на меня опять навалилась бессонница..."
    
    play music na_nachalo
    
    scene bg main photo
    with fade
    
    v'''
    С самого детства у меня было три лучших друга. Надя, Петя и Василиса. Я их очень любил и люблю.
    
     Но однажды Надя просто пропала...
    
     А самое страшное это то, что никто не заметил ее пропажи.Никто ее не помнит, будто память о ней стерли у всех.
    
     Будто она испарилась.
     
     Все эти года я бежал вперед, хотел найти ее, сделать что-то непостижимое и, кажется в конце концов остался ни с чем.'''
    
    scene bg main ch room nig #начало сцены где гг делает выборы
    with fade
    
    v 'Эх...'
   
    "Ваня - школьник, учащийся в девятом классе, живет в среднестатестическом городе России, любит читать. Он очень ответственный человек, но достаточно неуверен в себе. Ходит в школу и проводит время со своими друзьями."
    "Комната Вани напоминала уголок, наполненный тоской и лишенный естественного света. Все здесь напоминало о подруге и ее неожиданном исчезновении, заставляя мальчика ощущать потерю и беспомощность."
    
    menu:
        v 'Мне так не хочется куда-то идти, вот бы еще поспать.'
        
        "Продолжить спать":
            jump son
        
        "Проверить телефон":
            jump telefon
        
        "Встать с кровати":
            jump vstat
    
    return     

label son: #Ваня продолжит спать

    "Ваня решает еще немного поспать в теплой кроватке."
    
    show mama angrya at right
    with vpunch
    
    mam "Ваня! Ты долго еще собираешься лежать в кровати! Ты так в школу опоздаешь! Иди давай завтракать!"
    
    hide mama
    
    jump na_kuhne #Перемещаемся на сцену на кухне
        
    return
    
label telefon:#Ваня решает проверить телефон

    "Ваня решает проверить социальные сети и сообщения от Пети."
    
    show sms na telefon #done
    with moveinbottom
    
    p "{i}Чувак, там две серии Наруто вышло! Погнали ко мне после школы смотреть!{/i}"
    
    $ prochel = True
    
    menu:
        "Что ответить Пете?"
        "Да, давай":
           jump sogl
        
        "Не, не хочу":
            jump otkaz
    return
    
label sogl: #Ваня соглашается пойти к Пете
    $soglasilsya = True

    show sms na telefon 2 
    with dissolve
    
    "Ваня соглашается пойти к Пете."
    
    v "{i}Ооо, крутяк,еще и сразу две! Конечно пошли,там сейчас самый экшен.{/i}"
    
    hide sms na telefon 2
    with moveoutbottom
    
    show mama normala at right
    with dissolve
    
    mam "Ваня, ну сколько можно спать, вставай давай и иди есть!"
    
    hide mama
    
    jump na_kuhne
    return

label otkaz: # Ваня отказывается пойти к Пете
    $otkazalcya = True
    
    show sms na telefon 2 
    with dissolve
    "Ваня решил не идти к Пете."
    
    v "{i}Нее, чувак, я не хочу, да и мама не разрешит. Может в другой раз...{/i}"
    
    hide sms na telefon 2
    with moveoutbottom
    
    show mama normala
    with dissolve
    
    mam "Ваня, ну сколько можно спать, вставай давай и иди есть!"
    
    hide mama
    
    jump na_kuhne
    
    return
    
label vstat: #Ваня встает
    # play sound vstal ПОКА НЕ ЗНАЮ ОСТАВИТЬ ИЛИ НЕТ
    "Ваня решает встать с кровати."
    
    show kit at right
    with dissolve
    
    play sound mya
    kit "Мяу!"
    
    v "Маруся,дак ты со мной сегодня спала"
    
    "Маруся больше всего любила Ваню в семье и всегда спала в его комнате"
    
    menu:
        "Погладить Марусю":
            jump pogladit
        
        "Уйти":
            jump yiti
            
    return
    
label pogladit: #Ваня встает: гладит Марусю

    show kit happy at right
    with dissolve
    
    play sound mrr
    kit "Мрррр...."
    
    v " Ты всегда поднимаешь настроение. Теперь я чувсвую себя лучше."
    
    $renpy.notify("Ваня себя чувствует лучше")
    
    hide kit

    show mama happya:
        xalign 0.8 yalign 1
    with dissolve
    
    mam "Ваня, в школу собираться пора, а ты с кошкой нянчишься, она итак от тебя не уходит, спускайся есть."
    
    hide mama
    
    jump na_kuhne

    return
    
label yiti:#Ваня встает: не гладит Марусю
    
    v "Прости,Мар,мне нужно собираться."
    
    hide kit
    
    show mama normala:
        xalign 0.8 yalign 1
    with dissolve
    
    mam "Ваня, завтрак приготовила, собирайся скорее давай и спускайся есть."
    
    hide mama
    
    jump na_kuhne

    return
    
label na_kuhne:#Ваня завтракает с родителями,сцена на кухне #ПОМЕНЯТЬ ТЕЛЕФОН ЕСЛИ ПРОЧЕЛ СМС ОТ ПЕТИ
    
    show bg kuchna
    with fade
    
    show papa normala at left
    '''
    Папа Вани работал на угольном производстве, он никогда конкретно не рассказывал, чем занимается, но Ваня знал,что у него тяжелая и опасная работа.
    Дома он появлялся редко, а если и появлялся, то проводил время c женой.
    
    К Ване отец относился строго и требовательно, мальчику часто не хватало отцовского внимания и его любви.
    '''
    "Он попивал утренний кофе на своем месте, хмуро читая газету и говоря что-то себе под нос."
    
    play sound hmm
    pap angrya "Что-то ты долго сегодня встаешь."
    
    show mama normala at right2
    with dissolve
    
    a "Мама Вани была домохозяйкой. Она очень активна, организованна и энергична.Ей всегда удавалось создать уютную атмосферу дома."
    a "Ваня очень любит мать."
    
    mam happya "Так приятно когда мы все завтракаем вместе."
    
    mam vostorga "Дорогой представляешь, говорят,что поток туристов после 2014 года вырастет в три раза."
    
    pap happya "Ну, это и понятно. Сколько приедет только на олимпиаду поглазеть."
    
    mam bykaa "Нам нужно было тоже ехать на олимпиаду. Такое раз в жизни увидишь."
    
    stop music fadeout 7.0
    
    pap "Дорогая, мы же не могли бы все бросить и уехать."
    
    pap "Летом поедем куда захочешь."
    
    show mama vostorga at right2
    
    a "Ваня скучающе смотрел на тарелку, размазывая кашу по краям. Его не интересовали, ни олимпиада, ни поездки."#ДОПИСАТЬ
    
    hide mama
    
    hide papa
    
    show bg nachalo
    
    play music fon_scary
    
    a "Единственное,что его тревожило - сон с Надей."
    
    show nadya
    with Dissolve (5)
    
    v '''Как это могло произойти? 
    
    Где она сейчас? 
    
    Мог ли я что-то сделать, чтобы предотвратить это? 
    
    Как найти ее? 
    
    Как я могу связаться с людьми, которые могут знать, что случилось с ней?.
    
    Что она сделала,что пропала?
    
    Я был достаточно хорошим другом для нее?
    
    Как мне сохранить память о нашей дружбе?
    
    '''#еще не придумано
    
    hide nadya
    
    stop music
    
    play sound sms
    
    scene bg kuchna
    
    show papa crazy at left
    
    show mama crazy at right2
    
    v "?"
    
    show papa normal at left
    
    show mama vostorg
    if prochel:
        show sms na telefon vas no p
        with moveinbottom
    else:
        show sms na telefon vas
        with moveinbottom
    
    v "Василина?"
    v "Чего это она решила написать?"
    
    menu:
    
        "Прочитать сообщение Василины?"
        "Да":
        
            jump vasilina_i_vanya_idut_v_sh
            
        "Нет":
            $renpy.notify("Василина запомнит это")
            
            jump vanya_idet_s_petya
    
    return
    
label vasilina_i_vanya_idut_v_sh:#Петя читает смс от Василины

    show sms na telefon vas2
    
    va "{i}Привет, Ваня! Давай сегодня вместе в школу пойдем. Я буду ждать тебя у твоего дома^^/{/i}"
    $ne_prochel = True
    
    hide sms na telefon vas2
    with moveoutbottom
    
    v "Похоже у меня нет выбора, да и не хочу я отказывать Василине, неудобно получится, пора собираться в школу."
    
    "Ваня вышел из-за стола раньше обычного, решив не наслаждаться компанией родителей, хоть они и редко проводили утро всей семьей."
    jump ulisa
    return
    
label vanya_idet_s_petya: #Петя игнорирует сообщение от Василины

    v "Не хочу сейчас с кем-то разговаривать. Еще в школу собираться пора."
    
    hide sms na telefon vas
    with moveoutbottom
    
    "Ваня отложил телефон и продолжил слушать утренние разговоры родителей, порой вставляя свои слова в их диалог."
    "Редко выходило провести утро всей семьей, так что Ване удалось ненадолго забыть о своем тревожном сне и провести время с родителями."
    
    jump ulisa
    
    return
    
label ulisa: #Ваня уходит на улицу #CДЕЛАТЬ РЕАКЦИЮ ПЕТИ ЕСЛИ ВАНЯ ОТКАЗАЛСЯ СМ. НАРУТО НО ПРОИГНОРИЛ ВАСИЛИСУ
    scene bg ulisa #DONE
    with fade
    
    play music na_ulise
    
    "Ваня жил в спальном районе небольшого городка в центральной части России."
    "Все вокруг окутано свежим снегом, словно белоснежным покрывалом, на котором каждый шаг оставляет свой след. Голые деревья украшаются ледяными гирляндами, создавая прекрасный контраст с мягким снежным покровом." #РАСШИРИТЬ
    "Зимние улицы города погружены в мертвую тишину, обшарпанные здания тяжело вздыхают под тяжестью снега. Одинокие фонари гаснут на фоне затянутого серыми облаками неба, создавая ощущение заброшенности."
    
    if ne_prochel:#Ваня выходит к Василисе
    
        "Недалеко от подъезда Ваня увидел чей-то силуэт."
        
        show vasilisa v kur happy with dissolve
        
        "Это была Василина. Она стояла на тротуаре, обернутая в теплый пуховик и шарф, в ожидании своего друга. Снежинки медленно падали на ее волосы и плечи, которые она иногда пыталась отряхнуть."
        "Ее взгляд направлен вдаль, как будто она ожидала Ваню уже очень долго."
        
        show vasilisa blink1 with dissolve
        
        va"Привет,Ваня! Долго ты собирался, я уже успела замерзнуть."
        
        v"Прости, Василин, родители задержали."
        
        show vasilisa v kur happya
        
        va "Да ладно тебе, я как увидела тебя,сразу тепло стало."
        
        show vasilisa blink1 with dissolve
        
        a "Ваня почувствовал себя комфортно с подругой и мимолетно жизнь показалась ему счастливой, мальчик взглянул на темное и бесконечное небо, где-то еще видны были звезды."
        
        v"Пошли?"
        
        a "Он посмотрел на Василину, которая тоже подняла голову наверх, чтобы посмотреть на небо."
        
        va"Угу."
        scene bg vasilisa i vanya
        with fade
        pause 10
        
        jump vanya_i_vasilina_idut_v_sh
       
    else: #Ваня не прочел смс от Василины
        if prochel: #Ваня выходит к Пете и прочел смс его
            "Недалеко от подъезда Ваня увидел чей-то силуэт."
            "Это был Петя, он пинал снежные камни, держа руки в карманах, ходил туда сюда и мямлил что-то себе под нос. Парень явно был одет не по погоде, стоя в легкой куртке уже с румянцем от холода на щеках."
            "Когда Ваня вышел из подъезда, Петя радостно посмотрел на друга и подбежал к нему, мальчик явно ждал Ваню у подъезда."
            
            show petya blink1
            
            p "Йоу, Ваня, привет. Я уж думал ты не выйдешь. Захотел вместе в школу пойти, да написать не успел, хорошо, что ты прочел утреннее сообщение, сегодня же все в силе?"
            
            "Ваня улыбнулся Пете, в компании друга ему стало сразу веселее, он вспомнил о предстоящем вечере с другом и повеселел."
            
            v "Да, конечно, жду не дождусь. Только маму нужно будет предупредить. Купим сухариков после школы?"
            
            p "Ты еще спрашиваешь!"
            
            show petya v kur happya
            
            a "Мальчики рассмеялись и будто разбудили тишину, что стояла вокруг них."
            
            scene bg petya i vanya
            with fade
            pause 10
            
            jump vanya_i_petya_idut_v_sh
            
        else:#НАДО ПРОВЕРИТЬ НА СОГЛАШЕНИЕ ИЛИ НЕТ ПЕТИ.Ваня выходит к Пете,игнорируя его смс.
            "Недалеко от подъезда Ваня увидел чей-то силуэт" 
            "Это был Петя. Он стоял у подъезда с хмурым лицом, скрестив руки. Иногда пинал снежные камни, говоря себе что-то под нос."
            "Парень явно был одет не по погоде, стоя в легкой куртке уже с румянцем от холода на щеках."
            
            show petya v kur angrya with dissolve
            p"Привет, Ваня. Игнорщик ты. Я тебе еще вчера написал, а ты не читаешь."
            
            a "По лицу Пети казалось,что он злится, но на самом деле ему было просто обидно, Петя застал Ваню в расплох и ему стало стыдно."
            
            v"Извини, Петь, мама утром пришла будить, я даже собраться нормально не успел."#Может сделать выбор как извиниться перед Петей.
            
            show petya blink1 
            
            p "Да, лан тебе. Я так и понял. Я о чем писал то тебе, там сегодня целых ДВЕ серии вышло по Наруто, погнали ко мне после школы смотреть!"
            
            show petya v kur happya
            
            menu:
                v "Думаю, я..."
                "Да, пошли":
                    $soglasilsya = True
                    "Ваня заулыбается Пете, он сразу представил как они купят газировки и сухарики, а Петина мама угостит их чем-то вкусным."
                    
                    v"Думаю, я за. Отличная идея, целую неделю ждем серию, а тут их сразу две!"
                    
                    "Петя сразу расплылся в улыбке, казалось,что он светился ярче солнца."
                    
                    p"Отлично! Я не сомневался, что ты не откажешься."
                    
                    "Мальчики рассмеялись и будто разбудили тишину, что стояла вокруг них."
            
                    scene bg petya i vanya
                    with fade
                    pause 10
                    
                    jump vanya_i_petya_idut_v_sh
            
                    
                "Не, не хочу":
                    $otkazalcya = True
                    "Ване очень не хотелось сегодня даже вставать с кровати, что уж говорить о том,чтобы пойти куда-то после школы."
                    
                    v"Нее, я не хочу, давай завтра или на выходных?"
                    
                    #$ renpy.notify("Петя запомнит это.")
                    
                    show petya v kur rassta #Доделать
                    
                    p"Ну хорошо, я понимаю, тогда в другой раз."
                    
                    "Петя расстроенно посмотрел в пол, сминая куртку, он не любил, когда ему отказывают, особенно когда ему отказывал Ваня, но он всегда принимал его решение."
                    
                    v"Не переживай, мы обязательно посмотрим."
                    
                    scene bg petya i vanya
                    with fade
                    pause 10
                    
                    jump vanya_i_petya_idut_v_sh
                    
    return 
    
label vanya_i_vasilina_idut_v_sh: #ВАНЯ И ВАСИЛИСА ИДУТ В ШКОЛУ
    
    scene bg ulisa2
    with fade
    
    show sneg_idet
    show vasilisa blink1 at right2 with dissolve
    play sound hod_po_snegy
    
    a "Ребята пошли привычным маршрутом до школы. Тихая заснеженная улица ранним зимним утром словно окутана мерцанием лунного света.Под ногами хрустят свежие снежные хлопья."
    show vasilisa v kur smysa at right2 with dissolve 
    
    va  "Кстати, моя мама спрашивала о тебе."
    
    a "Ваня с удивлением посмотрел на Василину и робко спросил."
    
    v"Что, обо мне?"
    
    show  vasilisa v kur happya at right2 with dissolve
    
    va "Да, да, говорила почему это Ваня совсем в гости не приходит, сама хотела к твоей маме прийти."
    
    a "Ваня отвел взгляд в сторону, в последние годы они с Василисой стали не так близки. Мальчик судорожно думал о том, как сменить тему."
    
    show vasilisa blink1 at right2 with dissolve
    
    v "Аа... Ну, книга, книга которую я дал тебе, Морфий у Достоевского, ты ее уже прочла? Когда отдашь?"
    
    va v kur rastera "Ах, я про нее совсем забыла... "
    
    p "ВАНЯЯ, ВАСИЛИСА!!! Вот вы где!" with vpunch
    
    show vasilisa blink1 at right2 
    with vpunch
    
    a "Внезапно послышался крик, Ваня с Василисой вздрогнули из-за неожиданности, голос казался до боли знакомым..."
    a "Обернувшись, они увидели запыхающегося Петю, догоняющего их. Одет он был легко, явно не по погоде, ремянец выступил на кругом лице, то ли от холода, то ли от бега."
    
    show petya v kur happya at left2 with dissolve
    show vasilisa blink2
    
    p "Я ждал тебя у подъезда, Вань, и понял что ты уже ушел, а телефон разряжен. Иду, иду и вот вижу вас!"
    
    show petya blink1
    
    va "Привет, Петя."
    
    p blink2 "Привет, Вась."
    
    va v kur angrya "Не называй меня так, дурак."
    
    p v kur happya "Да ладно тебе."
    
    a "Появление Пети внесло краски в разговор ребят, он всегда умел развеселить кампанию и знал подход к каждому."
    
    if prochel==False:#ПЕТЯ СПРАШИВАЕТ У ВАНИ,ЕСЛИ ТОТ НЕ ПРОЧЕЛ УТРЕННЕЕ СООБЩЕНИЕ
    
        show petya v kur angrya at left2 with dissolve
        
        p"Ваня. Игнорщик ты. Я тебе еще вчера написал, а ты не читаешь."
            
        a "По лицу Пети казалось,что он злится, но на самом деле ему было просто обидно, Петя застал Ваню в расплох и ему стало стыдно."
            
        v"Извини, Петь, мама утром пришла будить, я даже собраться нормально не успел"#Может сделать выбор как извиниться перед Петей.
            
        show petya blink1 
            
        p"Да, лан тебе. Я так и понял. Я о чем писал то тебе, там сегодня целых ДВЕ серии вышло по Наруто, погнали ко мне после школы смотреть!"
            
        show petya v kur happya
            
        menu:
            v "Думаю, я..."
            "Да, пошли":
                $soglasilsya = True
                "Ваня заулыбается Пете, он сразу представил как они купят газировки и сухарики, а Петина мама угостит их чем-то вкусным"
                    
                v"Думаю, я за. Отличная идея, целую неделю ждем серию, а тут их сразу две!"
                    
                a "Петя сразу расплылся в улыбке, казалось,что он светился ярче солнца"
                    
                p"Отлично! Я не сомневался, что ты откажешься."
                   
            "Не, не хочу":
                $otkazalcya = True
                "Ване очень не хотелось сегодня даже вставать с кровати, что уж говорить о том,чтобы пойти куда-то после школы."
                    
                v"Нее, я не хочу, давай завтра или на выходных?"
                    
                #$ renpy.notify("Петя запомнит это.")
                    
                show petya v kur rassta #Доделать
                    
                p"Ну хорошо, я понимаю, тогда в другой раз."
                    
                "Петя расстроенно посмотрел в пол, сминая куртку, он не любил, когда ему отказывают, особенно когда ему отказывал Ваня, но он всегда принимал его решение."
                    
                v "Не переживай, мы обязательно посмотрим."
                   
    
    show petya blink2 at left2
    
    p " Вы готовились к контрольной по физике?"
    
    va blink2 "Конечно, правда до сих пор ничего не понимаю."
    
    show petya blink1 at left2
    show vasilisa blink1 at right2
    
    v "Я пытался понять, но потом забил и пошел играть в приставку."
    
    show petya v kur happy at left2
    show vasilisa v kur happy at right2
    
    a "Ваня любил когда они втроем шли в школу." #Дописать
    
    jump u_scholi
    
    return
    
label vanya_i_petya_idut_v_sh: #ВАНЯ И ПЕТЯ ИДУТ В ШКОЛУ

    scene bg ulisa2
    with fade
    
    show sneg_idet
    show petya blink1 at left2 with dissolve
    play sound hod_po_snegy
    
    a "Ребята пошли привычным маршрутом до школы. Тихая заснеженная улица ранним зимним утром словно окутана мерцанием лунного света.Под ногами хрустят свежие снежные хлопья."
    
    p "Я сегодня тааак не выспался."
    
    a "Растянуто сказал Петя, протяжно зевая."
    
    v "А почему ты без шапки? Уже достаточно холодно чтобы ходить без нее."
    
    p v kur rastera "Пффф... В ней я выгляжу как яйцо, да и не холодно мне вовсе."
    
    p v kur happya "А без нее я выгляжу очень привлекательно."
    
    a "Внезапно впереди мальчики заметили очень знакомую фигуру, это была Василиса, шагающая одна по сугробам в школу."
    
    p"ВАСЯЯ!!" with vpunch
    
    a "Петя громко закричал и замахал руками, они был очень громкоголосым парнем,так что девушка сразу услышала."
    a "Обернувшись Василина сразу поймала взглядом Ваню и недовольно посмотрела на него."
    
    show vasilisa v kur angrya at right2 with moveinright
    
    p blink2"Привет,Василиса."
    
    va "Ваня, ты дурак, я тебе писала, а ты игнорщик."
    
    v"Прости меня, я хотел пойти вообще один в школу."
    
    a "Смущенно затараторил Ваня."
    
    va v kura "Ну ладно, все равно не смогу злиться на тебя долго."
    
    p v kur happya "Ребята, давайте жить дружно."
    
    show petya blink2 at left2
    
    p " Вы готовились к контрольной по физике?"
    
    va blink2 "Конечно, правда до сих пор ничего не понимаю."
    
    show petya blink1 at left2
    show vasilisa blink1 at right2
    
    v "Я пытался понять, но потом забил и пошел играть в приставку."
    
    show petya v kur happya at left2
    show vasilisa v kur happya at right2
    
    a "Ваня любил когда они втроем шли в школу." #Дописать
    
    jump u_scholi
    return  
    
label u_scholi:#Ребята подошли к школе,Появление Нади

    #stop hod_po_snegy
    scene bg u scholi with fade
    
    v "Школа была скучным местом, где ученики проводили большую часть дня, слушая однообразные лекции и выполняя задания."
    
    show petya blink1 at right2 with dissolve
    show vasilisa blink1 at left2 with dissolve
    
    p "Ладно,хватит об учебе. Я слышал слухи, что к нам хотят перевести кого-то."
    
    stop music fadeout 7.0
    
    v"Да,ладно?! А кого именно ты не знаешь?"
    
    p"Вроде каких-то двух ребят, надо спросить в классе."
    
    p v kur rastera "Знаю только то, что это парень и девчонка."
    
    a "Так как ребята жили в небольшом городке, перевод кого-то в их школу казался чем-то необычным."
    
    hide petya
    hide vasilisa
    
    "Ваня?" with vpunch
    
    play music fon_s_nadya
    
    scene bg vanya v shoke with fade
    
    "Внезапно Ваня услышал кроткий голос, донельзя знакомый и незнакомый одновременно, сначала парень подумал, что ему показалось."
    "Он сразу начал оглядываться, бегая глазами по лицам прохожих, сердце начало учащенно биться, а дыхание сбилось."#
    
    scene bg nadya with fade
    
    "Девушка с черными волосами казалась потерянной в толпе, словно ее душа была где-то далеко от здесь и сейчас. Как ей было не холодно?"
    "Она была одета в темное платье. В ее глазах не было света, лишь тоска и безысходность."#Описание Нади
    
    scene black with off
    
    scene bg no nadya with onn
    
    v "Надя!?"
    
    show vasilisa v kur rassta with dissolve
    
    va "Ваня?? Все хорошо?"
    
    a "На лице Василины читалось волнение и смятение."
    
    a "Мальчик вышел из оцепенения."
    
    menu:
        v "Что же мне делать?"
      
        "Побежать за девушкой":
        
            v "Подожди Василиса."
            
            jump pobejal
            
        "Не бежать за девушкой":
        
            jump ne_pobejal        
    
    return
    
label pobejal: #Ваня побежал за Надей
    play sound beg_po_snegy
    
    scene bg vanya bezit with vpunch
    
    '''Мальчик тут же сорвался с места и побежал, прорываясь сквозь толпу школьников и их родителей.
    "Я должно быть в бреду?" - думал Ваня, он не понимал зачем вообще побежал за девочкой, но ноги сами его понесли.
    
    Позади были слышны окрики друзей, они побежали за парнем.'''
    
    scene bg vanya i nadya with fade
    
    "Девушка была так близка, но в то же время так далка, он почти дотянулся, однако она быстро скрылась из виду, будто ей и вовсе нельзя было показываться."
    
    scene bg vanya i friends with fade
    
    "Внезапно мальчик почувсвтовал чью-то руку на плече и сразу же остановился. Он столкнулся с Петей и Ваней, который догнали мальчика."
    
    scene bg u scholi with fade#поменять на что-то другое 
    
    show petya v kur rassta at right2
    show vasilisa v kur rassta at left2
    
    p "Ваня, блин, ты куда понесся!?"
    
    va "Что с тобой?!"
    
    a "Они смотрели ошарашенно на мальчика."
    
    a "Ваня смотрел в глаза друзей и не мог проронить ни слова, он и не знал что говорить."
    
    v "Я не знаю, показалось, что я увидел знакомую и..."
    
    p v kur angrya "И решил удрать от нас?"
    
    stop music fadeout 4.0
    
    v "Я обознался..."
    
    jump v_koridore
    
    return
    
label ne_pobejal:#Ваня НЕ! побежал за Надей
    
    $ne_pobejal = True
    
    stop music fadeout 5.0

    v "Да, Василин, все нормально, не проснулся видимо еще."
    
    "В голове у Вани все смешалось в кашу, сердце по-прежнему сильно билось и звенело в ушах."
    
    hide vasilina v kur rasst
    
    scene bg u scholi with fade
    
    show petya blink1 at right2 with dissolve
    show vasilisa blink1 at left2 with dissolve
    
    p "Это потому что ложиться надо нормально, а не в три ночи, как ты любишь."
    
    v "Не могу я спать, заснуть не получается."
    
    p v kur rastera "Мда, чувак, это плохо."
    
    va "Может тебе таблетки пить какие-нибудь?"
    
    va v kur rastera"И давайте пойдем уже, пять минут осталось, а нам переодеться еще надо."
    #Может как-то дополнить
    
    jump v_koridore
    
    return
    
label v_koridore:#Момент в коридоре перед уроком

    if ne_pobejal:
    
        scene bg koridor with fade
        
        play music koridor
        
        "Коридор в школе был обшарпанным и потрепанным. Стены были покрыты царапинами  а на полу можно было увидеть участки обломанной плитки. Несмотря на это, воздух был свежим и здесь слышался звонкий смех детей."
    
        show vasilisa blink at left2 with dissolve 
        
        show petya blink at right2 with dissolve
        
        p "А что у нас сейчас?"
        
        va "Русский язык! Боже, Петя мы учимся по этому расписанию уже полгода, а ты еще не запомнил."
        
        p  happya "Да ладно тебе, Вась."
        
        va @ bykaa "Ты начинаешь меня бесить, придурок."
        
        a "Ваня внезапно ткнул Петю локтем, кивая вперед, давая знак, чтобы он вел себя потише."
        
        a "Впереди ребята заметили стройную фигуру в черном пиджаке и увесистыми плечами."
        a "В коридоре тут же стало тихо, будто все разом замолчали."
        
        stop music fadeout 4.0
        play music mus_v_kor fadeout 4.0
        
        a "Это был директор их школы."
        a "У него всегда был строгий и устрашающий вид, ученики отвели взгляд в пол и чувствовали себя скованно."
        
        hide vasilisa 
        hide petya
        
        show directora at right3 with dissolve
        show vasilisaa at left3 with dissolve
        show petya1 at right4 with dissolve
        
        d "Доброе утро ребята."
        
        a "Здравствуйте,Петр Николаевич!"
        
        a "Хором сказали ребята, вытянувшись в струнку."
        
        a "Мужчина прошел мимо них, цепляя взглядом Ваню, на его лице было невозможно прочитать эмоции."
        
        hide directora
        hide vasilisaa 
        hide petya1
        
        show vasilisa blink at left2 with dissolve 
        
        show petya blink at right2  with dissolve
        
        '''
        "Cамое интересное это то, что он отец Нади." - пронеслось в голове Вани, - "он точно должен что-то знать."
        "Эта мысль у меня уже давно, как родитель может отрицать существование своего ребенка?" - подумал Ваня.
        '''
        $renpy.notify("Поговорить с директором")
        
        p fufa "Фуууф, у меня сердце чуть не вывалилось, почему он страшный такой."
        
        va bykaa "Не неси чепухи, у него просто строгий вид, каким еще должен быть директор?"
        
        p gigaa "Молодой и красивой женщиной!"
        
        va angrya "Ты у меня сейчас получишь, болван."
        
        #Вася побьет Петю картинкаМБ
        
        a "Василиса и Петя всегда легко находили общий язык и вели себя максимально открыто. Ване это нравилось."
        
        v "Вы сейчас поубиваете друг друга."
        
        'Смеясь сказал Ваня, наблюдая за друзьями."Ах, мне с ними так хорошо."- подумал Ваня. "Вот бы это продолжалось вечность."'
        
        play sound zvonok #Cделать погромче
        
        jump v_klasse
        
    else: #Побежал
        scene bg koridor no ppl with fade
        
        "Коридор был пустым, звонок уже прозвенел и в школе было максимально тихо, бесшумную идиллию разбивали быстрые шаги ребят, опаздывающих на урок."
        
        play sound beg_koridor
        
        show vasilisa volna at left2 with dissolve
        
        show petya blink at right2 with dissolve
        
        va volna "Если Марина Борисовна уже в классе, то нам конец."
        
        p @ gigaa "Ты останешься жива, она тебя любит."
        
        va bykaa "Тебя послушай, ты вообще не волнуешься, если нам дадут тест делать, я тебе не дам списывать."
       
        d "Господа и дама, почему бегаем по коридору после звонка?"
        
        hide vasilisa
        hide petya
        
        stop music
        
        a "Ребята резко остановились и врезались друг в друга, первым был Ваня, он и поймал на себе осуждаюзий взгляд человека, стоящего перед ними."
        
        show director at right3 with dissolve
        show vasilisa at left3 with dissolve
        show petya1 at right4 with dissolve
        
        a "Единственный, кого они не хотели бы встретить, нашел их сам. Это был директор их школы."
        a "У него всегда был строгий и устрашающий вид, ученики отвели взгляд в пол и чувствовали себя скованно."
        a "Ваня сделал шаг вперед, выпрямил грудь вперед и уверенно сказал."
        
        v "Здравствуйте,Петр Николаевич! Не рассчитали время случайно. Идем на урок."
        
        d smilea "Тогда поторопитесь, на русский язык опаздывать плохо."
        
        hide director with dissolve
        hide vasilisa 
        hide petya1
        
        a "Мужчина улыбнулся и пошел дальше по коридору, провожая взглядом Ваню."
        
        show vasilisa blink at left2 with dissolve 
        
        show petya blink at right2  with dissolve
        
        p fufa "Фуф, ушел. Откуда он знает, что у нас сейчас русский?"
        
        v "Действительно..."
        '''
        "Cамое интересное это то, что он отец Нади." - пронеслось в голове Вани, - "он точно должен что-то знать."
        "Эта мысль у меня уже давно, как родитель может отрицать существование своего ребенка?" - подумал Ваня.
        '''
        $renpy.notify("Поговорить с директором")
        
        va "Пойдемте!"
        
        scene bg anya v kor with fade
        
        "У входа в класс они заметили кого-то. Это была Аня, одноклассница ребят. Она достаточно хорошо сдружилась с мальчиками, так как тоже любила смотреть аниме."
        "Девочка услышала чьи-то шаги и обернулась,взглянув на ребят то ли радостно, то ли расстерянно."
        
        scene bg u classa
        
        show vasilisa blink at right with moveinleft
        show petya blink with moveinleft
        show anya rassta at left with moveinleft
        
        v "Аня?"
        
        an "Ребятааа. Вы тоже опаздываете? Я боюсь туда одна заходить, Марина Борисовна съест меня живьём."
        
        a "Петя с гордым видом и выпрямленной спиной подошел к Ане и сказал."
        
        p gigaa "Не волнуйся, Аня."
        
        jump v_klasse
        
    return
    
label v_klasse:#Ребята пришли в класс
    if ne_pobejal:

        scene bg classroom with fade
    
        play music klass
        
        "Учительницы еще не было, поэтому в классе было достаточно шумно, заходя в кабинет, ребята сразу наткнулись на знакомыне лица."
        
        show anyaa with moveinbottom
        
        an "Ваня, Петя, привет!"
        
        show anyaa at left 
        with move
        
        show petya gigaa with moveinright
        
        show vasilisa bykaa at right with moveinright
        
        p "Привет, привет, Аня."
        
        a "В классе ребят встретила Аня, их одноклассница, красивая, маленькая, светлая и веселая девочка, часто проводила время с друзьями, однако Василиса не очень любила кампанию Ани."
        
        an "Вы уже видели новые серии Наруто!?"
        
        "Она, как и парни, увлекалась аниме и очень любила брать образы из любимых произведений."
        
        stop music fadeout 3.0
        
        play sound shagi
        
        if soglasilsya:
        
            v "Мы как раз собираемся посмотреть сегодня."
        else:
            v "Может в ближайшее время посмотрим."
            
        #добавить диалог  
        hide vasilisa byka
        hide petya giga
        hide anya
        
        show marbar normala with dissolve
        
        m "..."
    
        m angrya "Девятый Б! У нас звонок не только для учителя прозвенел! Вас на другом этаже слышно!" with vpunch 
        
        m "Анна, опять оделась невесть что, ты таким внешним видом пришла знания получать или внимание мальчиков привлекать?"
        
        hide marbar
        
        a "Аня продолжила улыбаться мальчикам, не обращая внимания на слова учительницы."
        a "Все сели за свои места и начался очередной скучный урок русского языка. Мальчики сидели на третьей парте, а перед ними сидели Аня с Василисой."
        
        scene bg za partoi
        
        m "Итак, вы все знаете, что с этого года для выпускников девятых классов вводится основной государственный экзамен, вы как раз попадаете под первое его проводение. Исключений не будет, вам придется его сдавать."
        
        a "По классу раздались охи и разочарованные вздохи, пошел шум обсуждения услышанного."
        
        
        p angry "Да что это за капец, как теперь из школы выпускаться. Нам надо устраивать бунт, я не хочу писать эту херню."
        
        "Яростно шептал Петя Ване."      
        
        m "...Поэтому, русский язык вы будете сдавать поголовно, так что предлагаю устроить проверочную работу, чтобы я проверила как хорошо вы меня слушали за этот год."

        scene bg test v klasse with fade
        
        "Ваня пытался решить всеми силами, но некоторые задания давались с трудом и ничего лучше, чем попросить списать у кого-нибудь он не придумал."
        
        menu: #Списывание
            v "Черт, и что мне теперь делать?"
      
            "{image=images/icons/anya.png}Списать у Ани":#АНЯ
            
                show bg nachalo 
                show anya with fade
                
                $spisal_y_Ani=True
                
                v "Аня. Она достаточно умна, чтобы решить это, тем более у нас один вариант, но она не гуманитарий, надеюсь, она сможет мне помочь..."
                
                scene bg test v klasse
                
                "Ваня тыкнул ручкой в спину Аню, девочка в то же время повернулась и улыбнулась."
                
                an "Что такое?"
                
                v "Можешь помочь?"
                
                an "Конечно."
                
                "Парень передал подруге маленький листочек, где написал с какими заданиями у него проблемы, девочка повернулась и начала усердно что-то писать, Ваня делал умный вид что думает над заданиями, параллельно поглядывая на учительницу."
                
                show bg tetrad with fade
                
                show rukaani with moveintop
                
                an "Держи."
                
                an "Вроде бы все написала."
                
                $renpy.notify("Аня не забудет этого.")
                
                hide rukaani with dissolve
                
                "Надо было быстро переписать задания."
        
            "{image=images/icons/vas.png}Списать у Василисы":#ВАСИЛИСА
            
                show bg nachalo 
                show vasilisa with fade
                
                $spisal_y_Vasi=True
                
                v "Вася. Она точно знает ответы, она самая умная в классе. Надеюсь она сможет помочь."
                
                scene bg test v klasse
                
                "Ваня тыкнул ручкой в спину Василисы, девочка повернулась полубоком и вопросительно посмотрела на парня, Ваня прошептал."
                
                v "Можешь помочь?"
                
                "Василиса с улыбкой посмотрела на Ваню."
                
                va "Дурачина ты Ваня, что у тебя не получается?"
               
                "Парень передал подруге маленький листочек, где написал с какими заданиями у него проблемы, девочка повернулась и начала что-то писать, Ваня делал умный вид что думает над заданиями, параллельно поглядывая на учительницу."
                
                show bg bumaga with fade
                
                "Девочка быстро обернулась и кинула в Ваню скомканную бумажку."
                
                $renpy.notify("Василина не забудет этого.")
                
                show bg list
                
                "На листке были ровным почерком выведены ответы. Мальчик принялся переписывать ответы."
                
                v "На всякий случай нужно сделать пару ошибок, а то она не поверит, что я все сделал идеально."
                
            "{image=images/icons/petya.png}Списать у Пети":#ПЕТЯ
            
                show bg nachalo 
                show petya1 with fade
                
                $spisal_y_Peti=True
                
                v "Петя. Кажется он сейчас по уши в этом д...тесте. Это будет как-то эгоистично. Вряд-ли он мне как-то поможет, но раз в год и палка стрельнет."
                
                scene bg test v klasse
                
                "Мальчик ткнул локтем соседа. Обреченный Петя повернулся к Ване."
                
                v "Как успехи?"
                
                p mini "Ужасно... Может хоть тебя сможем вытянуть из этого болота."
                
                v "Поможешь?"
                
                p "Ага."
                
                "Петя всегда думал о других больше чем о себе, и это часто выходило ему боком, но Ваня не собирался осаваться у друга в долгу."
                
                v "Я тебе физику дам списать."
                
                "Парни, перешептываясь, начали делать задания."
                
                #show bg parni with fade
                
                m "Мальчики, чего списываем друг у друга, вам оценку тоже на двоих делить? Сдавайте свои работы." with vpunch
                
                
        if spisal_y_Vasi or spisal_y_Ani:
        
            m "Так, ребята, сколько вы собираетесь писать, я же говорила, это задание на пятнадцать минут, сдавайте листочки." with vpunch          
    

    else: #Побежал
        scene bg classroom with fade#добавить к бг марбару
        
        m ' Итак, вы все знаете, что с этого года для выпускников девятых классов вводится основной государственный экзамен, вы как раз попадаете под первое его проводение. Исключений не будет, вам придется его сдавать.'
        
        "По классу раздались охи и разочарованные вздохи, пошел шум обсуждения услышанного."
        
        m 'Записываем тему урока "Знаки препинания в сложноподчиненном предложении", нам дано на нее не так много времени, поэтому будем проходить быстро, а если что-то непонятно, то говорите.'
        
        #мб добавить звук скрипучей двери
        play sound dver
        
        "Дверь со скрипом открылась, выдавая с потрахами опаздавших, учительница тут же замолкла и, опустив очки, грозно посмотрела на ребят."
        
        show marbar angrya with dissolve
        
        m "Кондратьев, Ильин, Коносова, почему учитель никогда не опаздывает на ваши уроки, а вы постоянно заставляете меня ждать вас. Я уже отметила в журнале, что вас нет."
        
        m @ normala "Aх, Василинушка, почему ты обременяешь себя этими ребятами, умная ведь девочка."
        
        p "Да мы не специально опаздали, Марина Борисовна."
        
        m "Да, Кондратьев, я тоже не специально дам вам тест по прошлой теме. Доставайте двойные листочки, сейчас найду что вам дать."
        
        "За спиной у преподавательницы слышались мерзкие смешки, никто не любил дополнительных заданий на оценку, но все любили, когда их дают другим."
        
        scene bg test v klasse with fade
        
        "Ваня пытался решать всеми силами, но в голове у него только мелькало утро, он не мог сосредоточиться на дурацких заданиях, лучше чем попросить списать у кого-нибудь он не придумал."
        
        menu: #Списывание
            v "Черт, и что мне теперь делать?"
      
            "{image=images/icons/anya.png}Списать у Ани":#АНЯ
            
                show bg nachalo 
                show anya with fade
                
                $spisal_y_Ani=True
                
                v "Аня. Она достаточно умна, чтобы решить это, тем более у нас один вариант, но она не гуманитарий, надеюсь, она сможет мне помочь..."
                
                scene bg test v klasse
                
                "Ваня тыкнул ручкой в спину Аню, девочка в то же время повернулась и улыбнулась."
                
                an "Что такое?"
                
                v "Можешь помочь?"
                
                an "Конечно."
                
                "Парень передал подруге маленький листочек, где написал с какими заданиями у него проблемы, девочка повернулась и начала усердно что-то писать, Ваня делал умный вид что думает над заданиями, параллельно поглядывая на учительницу."
                
                show bg tetrad with fade
                
                show rukaani with moveintop
                
                an "Держи."
                
                an "Вроде бы все написала."
                
                $renpy.notify("Аня не забудет этого.")
                
                hide rukaani with dissolve
                
                "Надо было быстро переписать задания."
        
            "{image=images/icons/vas.png}Списать у Василисы":#ВАСИЛИСА
            
                show bg nachalo 
                show vasilisa with fade
                
                $spisal_y_Vasi=True
                
                v "Вася. Она точно знает ответы, она самая умная в классе. Надеюсь она сможет помочь."
                
                scene bg test v klasse
                
                "Ваня тыкнул ручкой в спину Василисы, девочка повернулась полубоком и вопросительно посмотрела на парня, Ваня прошептал."
                
                v "Можешь помочь?"
                
                "Василиса с улыбкой посмотрела на Ваню."
                
                va "Дурачина ты Ваня, что у тебя не получается?"
               
                "Парень передал подруге маленький листочек, где написал с какими заданиями у него проблемы, девочка повернулась и начала что-то писать, Ваня делал умный вид что думает над заданиями, параллельно поглядывая на учительницу."
                
                show bg bumaga with fade
                
                "Девочка быстро обернулась и кинула в Ваню скомканную бумажку."
                
                $renpy.notify("Василина не забудет этого.")
                
                show bg list
                
                "На листке были ровным почерком выведены ответы. Мальчик принялся переписывать ответы."
                
                v "На всякий случай нужно сделать пару ошибок, а то она не поверит, что я все сделал идеально."
                
            "{image=images/icons/petya.png}Списать у Пети":#ПЕТЯ
            
                show bg nachalo 
                show petya1 with fade
                
                $spisal_y_Peti=True
                
                v "Петя. Кажется он сейчас по уши в этом д...тесте. Это будет как-то эгоистично. Вряд-ли он мне как-то поможет, но раз в год и палка стрельнет."
                
                scene bg test v klasse
                
                "Мальчик ткнул локтем соседа. Обреченный Петя повернулся к Ване."
                
                v "Как успехи?"
                
                p mini "Ужасно... Может хоть тебя сможем вытянуть из этого болота."
                
                v "Поможешь?"
                
                p "Ага."
                
                "Петя всегда думал о других больше чем о себе, и это часто выходило ему боком, но Ваня не собирался осаваться у друга в долгу."
                
                v "Я тебе физику дам списать."
                
                "Парни, перешептываясь, начали делать задания."
                
                #show bg parni with fade
                
                m "Мальчики, чего списываем друг у друга, вам оценку тоже на двоих делить? Сдавайте свои работы." with vpunch
                
                
        if spisal_y_Vasi or spisal_y_Ani:
        
            m "Так, опаздавшие, сколько вы собираетесь писать, я же говорила, это задание на десять минут, сдавайте листочки." with vpunch
     
    show bg u doski with fade
    
    show marbar normala at right5 with dissolve
    
    a "Оставшаяся часть урока прошла повседневно скучно. Марина Борисовна читала учебник, не обращая внимание на уровень понимания учеников."
    a "Весь урок состоял из заучивания правил грамматики и списывания слов из учебника в тетрадь. Учительница говорила монотонным голосом, без эмоций."
    a "Внезапно в конце урока постучались в дверь, звук будто вывел весь класс из транса нудной лекции, Петя даже проснулся."
    a "В дверном проеме показался чей-то высокий темный силуэт. Черные отпылерованные до блеску ботинки зашагали по классу."
    a "'Что он тут забыл?'- пронеслось в голове у Вани."
    
    show director smilea at left2 with moveinleft
    
    d "Доброе утро, Марина Борисовна, извините что потревожу вас! Я тут показывал школу нашей новенькой, которая попала в 9Б. К сожалению, из-за этого она пропустила ваш прекрасный урок."
    
    m "Петр Николаевич! Доброе, доброе утро! Я слышала от вас, что девочка прилежная, наверное знает программу наперед. Это парни у меня в классе оболтусы."
    
    play music end1 fadein 7.0
    
    d "Тогда представьте нашу новенькую классу, пожалуйста, а я вынужден удалиться."
    
    hide marbar with dissolve
    
    hide director with dissolve
    
    "В классе раздался звук каблуков, медленно шагая, высокая фигура с холодным лицом зашла в класс."
    
    show bg end1 with fade
    
    "Длинные черные волосы достигали поясницы, выделяя еще больше без того бледное лицо. Входя в кабинет, она оставила впечатление элегантности. Ее присутствие привлекло внимание других, многие обратили взгляд на нее."
    
    "По классу волной пошел шепот."
    
    "Ваня не мог поверить своим глазам. Он не мог произнести ни слова, единственное что вырвалось у него изо рта."
    
    v "Надя?"
    
    show bg end2 
    
    "Конец первого акта."
    
    pause 60.
    
    return