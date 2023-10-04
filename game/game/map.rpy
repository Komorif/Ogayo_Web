# Карта
screen map:
    modal True
    zorder 100

    fixed:
        xsize 1920 ysize 1080
        add "images/map/friend_solo_plan.png" align (.5,.5)

    fixed:
        xsize 1920 ysize 1080

        # Транспортная система
        button:
            xpos 890 ypos 701
            xsize 64 ysize 66
            idle_background "images/map/idle_search.png"
            hover_foreground "images/map/hover_search.png"
            tooltip "Упрощённая транспортная система королевства Френдсоло"
            action Hide("map"), Jump("transportSystem")

        # Центральная зона
        button:
            xpos 800 ypos 375
            xsize 64 ysize 66
            idle_background "images/map/idle_search.png"
            hover_foreground "images/map/hover_search.png"
            tooltip "Центральная зона королевства Френдсоло"
            action Hide("map"), Jump("centralZone")

        # Башня
        button:
            xpos 1375 ypos 265
            xsize 64 ysize 66
            idle_background "images/map/idle_search.png"
            hover_foreground "images/map/hover_search.png"
            tooltip "Одна из сторожевых башен королевства Френдсоло"
            action Hide("map"), Jump("tower")

        # Лавка NeerwoX
        button:
            xpos 670 ypos 620
            xsize 64 ysize 66
            idle_background "images/map/idle_search.png"
            hover_foreground "images/map/hover_search.png"
            tooltip "Самое популярное место королевства Френдсоло - это лавка Нирвокса"
            action Hide("map"), Jump("shopNeerwox")

        # Выбырите
        button:
            xpos 59 ypos 55
            xsize 282 ysize 154
            idle_background "images/map/idle_next.png"
            hover_foreground "images/map/hover_next.png"
            tooltip "Чтобы выбрать куда пойти нажмите на кнопки поиска"
            action NullAction()


    $ tooltip = GetTooltip()

    if tooltip:
        fixed:
            xpos 30 ypos 656
            xsize 331 ysize 419
            add "images/map/book.png"
            text "[tooltip]" xsize 200 ysize 138 align (.5,.5)


# Переход к Транспортной системе
label transportSystem:
    play music forest
    scene transport_system with dissolve
    "Некоторые из нас научились использовать диких лошадей и теперь могут передвигаться с их помощью по городу."
    "Доставки карет и напитков делаються быстро и без проблем на дорогах."
    "Правда Нирвокс иногда жалуется на то, что дорога к его дому довольно трудная."
    "И ещё, если получится, то я хотел бы с течением времени увеличить количество мест, которые можно посетить."


    show screen map

# Переход к Центральной зоне
label centralZone:
    play music forest
    scene friend_solo with dissolve
    malaysia two bed "Я в центральной зоне королевства Френдсоло."
    malaysia two bed "Напрявлюсь в башню на юге, к капитану."
    scene forest2 with dissolve
    ""
    show screen map

# Переход к Башне
label tower:
    play music forest
    scene tower_inside with dissolve
    s3 three bed "Я в башне королевства Френдсоло."

    show subaru_five_animation with dissolve:
        xalign 0.01
    
    show subaru_six_animation with dissolve:
        xalign 1.02

    "~ В башнях находятся Субару. ~"
    "~ Их способности можно обозначить, как сенсорные, или ориентированные на обнаружение различного рода чужеземных объектов. ~"
    "~ Возле башен находятся лагеря капитанов, которые сразу получали информацию и начинали оперативно действовать. ~"

    show screen map

# Лавка NeerwoX
label shopNeerwox:
    play music forest
    scene shop_neerwox with dissolve

    "Поскольку самый быстрый путь к цели - прямой."
    "Скорее всего я добрался до внутренних западных ворот немного быстрее, чем напарники к краевым башням."
    show neerwox_animation with dissolve
    show subaru_five_animation with dissolve:
        xalign 0.01

    show subaru_four_animation with dissolve:
        xalign 1.00

    neerwox "Вот ваша порция эдитов."
    neerwox "Такие стоят 10000 гривен."
    s5 five "Это грабёж!"
    neerwox "Вы взяли самые дорогие, так что всё честно."
    s5 five "Ладно, но можешь сделать скидку?"
    s5 five "У моей дочери скоро день рождения и она очень любит твои, так называемые, эдиты."
    s5 five "Ну как?"
    neerwox "9000 гривен."
    s5 five "Ладно, по рукам."
    neerwox "Спасибо за покупку, приходите ещё."

    hide subaru_five_animation with moveoutleft
    show subaru_four_animation with moveoutleft:
        xalign 0.01

    show subaru_six_animation with moveinright:
        xalign 1.00

    "Краем глаза, Нирвокс заметил меня."
    "Он часто меня видел, так как я входил в личный разведотряд Серполле."
    "А поэтому раз в 2-3 дня пробегал через его лавку."
    "Сама лавка находилась на левой стороне дороги, ведущей прямо к западным внутренним воротам."

    neerwox "Привет Мартин."
    neerwox "~ Сегодня он бежит быстрее обычного. ~"
    neerwox "~ Что же с ним такое? ~"

    s4 four "Спасибо."
    hide subaru_four_animation with moveoutleft
    neerwox "Следующий."
    show subaru_six_animation with moveoutleft:
        xalign 0.01

    show subaru_seven_animation with moveinright:
        xalign 1.00

    "Пустым, наполненным рутины голосом, Нирвокс продолжил принимать покупателей."
    neerwox "~ Обычно, я слышал новости от Мартина, когда он пробегал через мой магазинчик, однако сегодня, я думаю, ему не суждено побеседовать. ~"
    hide subaru_six_animation with moveoutleft
    show subaru_seven_animation with moveinright:
        xalign 0.01

    "Небольшая толпа Субару начала заканчиваться, увеличивая пространство на дороге, а новых клиентов не наблюдалось."

    "Но меня беспокоит не отсутствие денежного потока."
    "Спустя две - три минуты, я заметил то, что никак не могло быть обычным."
    neerwox "~ Ещё кто-то бежит? ~"
    "После одного бегущего Субару, которого я знал как Мартина - лидера личной троицы Субару для Серполле, бежал следующий, незнакомый."
    neerwox "~ Они чёт зашевелились, как я посмотрю. ~"

    subaru_from_the_crowd "А разве к Серполле два Субару бегают?"
    subaru_from_the_crowd "— Права есть у трёх, а вот бегал обычно один."
    subaru_from_the_crowd "— Мисс Нирвокс, что думаете по этому поводу?"

    "Субару из толпы начали разговаривать между собой."
    "Я, озадаченный вопросом, отложил эдиты в сторону."
    "Через несколько секунд я дал свой ответ."

    neerwox "— Один Субару забыл что-то сказать второму, и из-за этого бежит за ним."
    subaru_from_the_crowd "А может, чрезвычайная ситуация."
    neerwox "~ Я тоже так думаю, но не стану говорить напрямую им. Скажу то, что по-моему правда. ~"
    neerwox "— Смотрите, все бегут к западной стене."

    "Я выглянул из лавки."
    "Я заметил повышенную активность вблизи некоторых находившихся Субару, но далеко не всех."
    "Поэтому сам не подал беспокойства и вернулся обратно на своё рабочее место."

    subaru_from_the_crowd_two "— Я на всякий случай побегу туда."
    hide subaru_seven_animation with moveoutleft
    subaru_from_the_crowd "— Я тоже."

    "Через несколько секунд вся находившаяся возле меня толпа Субару разбежалась в разные стороны."
    "По краям дороги находились житловые дома, которые в разных местах были то сильно сгущены, то довольно редки."
    "Стабильности и постоянства в этом плане не наблюдалось."

    neerwox "— Может и мне пойти посмотреть?"

    hide neerwox_animation with moveoutleft
    "Я решил выйти из своей лавки и также посмотреть со всеми Субару, что произошло, и почему поднялся такой шум."
    "Уходя, я убрал рабочее место, открыл двери, а после, закрыл их на ключ."
    "Также я вышел на переднюю часть магазинчика и опустил железную занавеску, чтобы какой-то Субару не решил залезть через кассу и не ограбить его."
    "Закончив все свои дела, я направился к западным воротам."

    scene friend_solo_left with dissolve
    show subaru_one_bed_animation with dissolve
    "Тем временем, я уже прошёл через вторые ворота королевства и направился к главному зданию, в котором находилась вся элита Френдсоло."
    "Там же решались важные вопросы, и принимались важные решения."
    "Это место было настолько секретным, что даже ступить на территорию вторых врат было подвигом для обычных Субару."
    "Поэтому все могли наблюдать за происходящим лишь тогда, когда врата были открытыми."
    "Не было у вторых врат даже маленьких щелей, через которые можно было наблюдать."
    "Не было у вторых стен даже маленьких неровностей, по которым можно было взобраться и перелезть на ту сторону."
    "Подкопаться под землёй также было плохим вариантом, поскольку даже там были прочные, непреодолимые стены"
    "Настолько это место должно быть секретным."

    s1 one bed "— Серполле!"
    "Я подбежал к дверям большого здания, которые можно было считать третьими воротами, и начал яростно стучать по ним."
    "Через минуту, двери легко открылись, и оттуда показалась голова темноволосой девушки."

    serpolle_question "— Извини Мартин, у меня гости из юга, ты не мог бы стучать потише?"
    serpolle_question "— И вообще, почему ты не на задании?"
    s1 one bed "— Я обнаружил последнего участника, и им оказался тот самый Резо!"

    "Услышанное вогнало в ступор смотрящую девушку."
    "Однако спустя несколько секунд её вернули обратно в сознание."

    s1 one bed "— Серполле, ты скоро?"
    serpolle_question "— Прошу пяааать минут."

    hide subaru_one_bed_animation with moveoutleft
    show serpolle_animation with dissolve

    "Серполле вышел из здания и уже полность оказался на улице, также закрыв за собой дверь."
    serpolle "— Ты видел Резо значит?"
    s1 one bed "— Да, но…"
    serpolle "— Через Ирис видел?"
    s1 one bed "— Конечно, но, у нас не вышло его забрать себе."
    s1 one bed "— Мы были втроём все, как вы и говорили собирать голубику."
    s1 one bed "— А после, мы его нашли, но нам попался тот самолёт."
    serpolle "— Наса?"
    s1 one bed "— Да, он забрал Резо с собой в КПфаги."
    s1 one bed "— Мы решили оставить их и убежать."

    "Тяжело вздохнув, Серполле положил руки на грудь и сказал."
    serpolle "— Ничего с этим не поделать."
    serpolle "— Что есть то есть."
    serpolle "— Самое главное это то, что Резо обнаружен, жаль что не в нас."
    serpolle "— Спасибо за отчёт."

    show serpolle_animation with moveoutleft:
        xalign 0.01

    "Серполле развернулся и уже хотел открыть двери, как вдруг услышал ещё один крик."
    $ persistent.threeChapter = True

    $ persistent.menuOneChapter = False
    $ persistent.menuTwoChapter = False
    $ persistent.menuThreeChapter = True
    s1 one bed "— Серполле!"

    show screen map