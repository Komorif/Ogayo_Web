# 1 Глава: Игра
label chapterOne:
    scene black with dissolve
    $ renpy.movie_cutscene("videos/1chapter.ogv")
    scene black with dissolve
    "Словно Марио в недавно вышедшем фильме я также летел в пространстве, напоминающим длинную трубу."
    "Однако вокруг меня не было ярких радужных картинок и разных фэнтезийных мест."
    "Только чернота без единого очертания знакомых объектов."
    show stool with dissolve
    "Позже я приземлился на каком-то стуле, всё также окружённый чернотой."
    "Это не был дым, скорее коробка, стены которой окрашены в чёрный цвет, {w}но при этом, существовал какой-то невидимый источник света."
    "Я был немного в смятении, однако потроху начал привыкать к необычной обстановке."

    nameQuestion "— Если это действительно место приземления, то я бы сделал его более заметным."
    nameQuestion "— Хотя это меня не волнует."

    show window1 with dissolve:
        xalign 0.5 yalign 0.4

    "Через несколько секунд, передо мной показалось сообщение, просто висящее в воздухе, и похожее на то, которое показывают перед вхождением в игру."

    play sound loudspeaker1
    loudspeaker "Введите ваш никнейм: user1400000 (last on the list)"

    "Перед тем как анализировать сообщение я попытался коснуться сообщения, но моя рука проходила сквозь него, словно через текстуру."
    "А когда я попытался коснуться 'пола' то чуть не упал со стула."

    nameQuestion "~ Это похоже на сообщение, которое дают новым игрокам. ~"
    nameQuestion "~ А как мне его изменить? ~"
    nameQuestion "~ Может просто силой мысли? ~"

    "Передо мной показалась клавиатура. {w}Она находилась на уровне рук и была удобно расположенная, чтобы печатать."

    play sound loudspeaker2
    loudspeaker "Введите ваш никнейм:"

    "Когда я решил что-то нажать на ней я поднёс свой палец к букве 'ю'."

    hide window1 with dissolve

    show window2 with dissolve:
        xalign 0.5 yalign 0.4

    "Сама клавиша засветилась зелёным, и в сообщении появилась новая буква."

    play sound loudspeaker3

    loudspeaker "Введите ваш никнейм:\nю"

    "А дальше, после более 5 минут экспериментов я решил стать серьёзным и наконец записать имя."

    jump Name
    return

label Name:
    hide window2 with dissolve

    show window3 with dissolve:
        xalign 0.5 yalign 0.4

    nameQuestion "~ Наверное подтвердить имя можно с помощью кнопки Ентер - также как и в реальном мире. ~"

    play sound loudspeaker7
    "Введите ваш никнейм: Rezo"

    play sound click
    "Клац"

    play sound loudspeaker4
    loudspeaker "Спасибо за регистрацию приятной игры."

    jump continueChapterOne
    return

label continueChapterOne:
    play sound explosion
    "..."
    play sound krik
    rezo "ААААААА"

    scene black with dissolve

    "После того, как я подтвердил своё имя, начал стремительно падать вниз и в скором времени упал на поверхность."
    "Вокруг всё также была чернота, однако сама поверхность ощущалась неровной."
    "Я лежал на спине, и немного отойдя от шока начал подниматься на ноги."
    "В процессе поднятия я заметил на поверхности странные явления - я как будто нащупал траву."

    rezo "— Похоже, я уже на земле."

    "В этот миг вся чернота стала туманом и начала растворятся, словно бумажная коробка в воде."
 
    scene forest_out_of_sight with dissolve

    play music forest

    "Первые проблески света коснулись моих роговиц и я смог увидеть перед собой небольшую ель."

    scene poster2 with dissolve
    $ persistent.forest = True

    "За несколько секунд вся чернота исчезла и я осознал, что теперь нахожусь в каком-то смешанном лесу - где есть и хвойные и лиственные деревья."
    "Неизвестность создавала страх, но при этом добавляла азарта."
    "Теперь я знал, что мне придётся всеми силами выживать в этом мире, а зачем?"
    "Я надеюсь в скором времени понять."

    play sound loudspeaker5
    loudspeaker "Внимание! {w}Последний участник прибыл в этот мир."
    play sound loudspeaker6
    loudspeaker "Набор участников официально завершён. {w}Всем приятной игры!"

    rezo "~ Вот как, значит я последний? ~"
    rezo "~ Скорее всего в этом мире есть 1400000 игроков если их можно так назвать. ~"

    "Также я не вижу каких либо изменений."
    rezo "~ Похоже, для начала событий не обязательно присутствие всех участников. ~"
    rezo "~ Ладно, вопросы оставлю на потом. ~"
    rezo "~ Сейчас нужно определить где я."
    rezo "~ И понять в каком направлении мне двигаться. ~"
    "Вдруг в моём сознании появилось какое-то странное сообщение."

    play sound memories1
    memories "До появления способности осталось ждать: 23.59.34-33-32."

    rezo "~ Способности? У меня будет способность? ~"

    "Однако я почти сразу прекратил на этом зацикливатся и начал своё передвижение в лесу."

    rezo "~ А он не такой густой как я думал. ~"
    rezo "~ Это радует. ~"

    scene forest_meadow with dissolve
    "Спустя примерно 20-30 минут ходьбы по лесу я нашёл большое поле голубики."

    rezo "~ Наконец-то у меня есть хоть какая-то еда, но этого, конечно же, мало. ~"
    rezo "~ До конца дня было бы неплохо ещё и воду найти."
    play sound eat
    "Я начал понемногу поглощать найденную голубику."
    "Однако в процессе я заметил, что на траве есть места, где могла бы находиться голубика, но её нету."
    "И эти места были преимущественно сверху."

    rezo "~ Похоже, это место часто посещалось животными. ~"
    rezo "~ Вот почему примерно половина голубики отсутствовала. ~"
    rezo "~ Если бы это были люди, то они старались бы брать не только сверху, но и снизу, и грамотный сбор явно будет легко отличить от обычного дикарства. ~"
    rezo "~ До того как я нашёл это место, я видел несколько слизней, но слизи вокруг кустов я пока не вижу. ~"

    "Я сделал вывод о том, что слизни не ели эту голубику как минимум несколько часов назад."
    "Также не было следов шерсти, перьев, помёта и других следов присутствия животных."
    "Я не старался обнаружить чьи то следы, поэтому посчитал, что просто не заметил их."

    rezo "~ Если её ели животные больших размеров, то у меня могут возникнуть проблемы когда попаду на одного из них. ~"

    "~ Всё таки этот мир неизвестный, может только эта часть напоминает прошлый мир, а остальная до корня изменена? ~"
    "~ В любом случае нужно поторопится и найти воду, а то при перемещении появилось желание пить. ~"

    "Ещё немного побыв на поле с голубикой я заметил кое-что весьма интересное."
    "В некоторых местах были заметны человеческие следы, не видные мне с прежней позиции."
    "Попробовав траву на ощупь я определил её, как совсем свежую."

    rezo "~ Здесь были люди около пяти минут назад. ~"
    rezo "~ Судя по тому, что следов немного, они скорее всего зашли на перекус, а после ушли по своим делам. ~"
    rezo "~ Также возможно и то, что этих людей напугали местные звери, но я ещё не встретил ни одного из них. ~"

    "Где то на юго-востоке послышались человеческие крики."
    "У меня был выбор."
    "Помочь людям, если они в беде и попасть хоть в какую-нибудь цивилизацию, или проигнорировать."
    "Я выбрал первый вариант."
    "Пытаясь пробраться через лес, чтобы как можно скорее попасть к людям я поцарапал ногу."
    "Однако не было времени обращать на это внимание."
    "Вполне возможно, что если потеряю этих людей, то больше никогда не выйду из этого леса."
    "Сам факт этой вероятности был довольно гнетущим, поэтому я решил посмотреть на происходящее, а уже после делать какие-то выводы."
    "Чем ближе я был к месту происшествия, тем лучше слышал звуки разговоров, несущихся с разных сторон."
    "Но вместе с этим я слышал и свои шаги, поэтому приближался осторожно."

    play sound leaves
    scene forest_battlefield with dissolve
    show leaves with dissolve
    "Через несколько секунд я увидел бой одной группы людей против другой."
    "Это происходило на небольшой площадке."

    show warrior with dissolve

    "С правой стороны были 9 воинов, скорее всего мужчин."
    "Из них шестеро были с мечами для ближнего боя, а трое имели в своём распоряжении луки."
    "Также воины имели лёгкие латы, и на своей спине какой-то непонятный Оранжевый рисунок."
    "А с левой стороны было что-то совершенно иное."

    hide warrior with moveoutleft
    hide leaves with dissolve

    show subaru_one_animation with dissolve:
        xalign 0.1

    show subaru_two_animation with dissolve

    show subaru_three_animation with dissolve:
        xalign 0.9

    show leaves with dissolve

    $ persistent.three_subaru = True

    rezo "Что здесь твориться?"
    "Воины на левой стороне выглядели точно также, как и главный герой аниме и ранобэ Ре зеро - Нацуки Субару."
    "Одежда, прическа, лицо - почти всё было похоже на него."

    rezo "— Неужели это как-то связано с Френдом?"
    rezo "~ Хотя с другой стороны, я не могу быть полностью уверен в этом. ~"
    rezo "~ Также возможно, что я единственный человек из моего прошлого мира среди всех этих участников. ~"
    rezo "~ Хорошо, просто понаблюдаю, может узнаю что-то. ~"

    coePhages "— Сдавайтесь, королевство Френдсоло."
    coePhages "— Когда наш юный господин Понаценко попадёт на трон и будет править всей империей КПфагов вас уже не будет защищать никакой договор."
    coePhages "— Вы будете стёрты с лица этого мира и попадёте в БАН (бесконечный ад неудачников)."

    s3 three "— Вы хоть себя слышите, КПфаги?"
    s2 two "— Когда ваш Понаценко попадёт на трон, мы уже полмира захватим, и тогда уже вы будете служить нам."

    coePhages "— Этому не бывать!"
    coePhages "— Даже наши нынешние правители, не то, что юный господин, не видят никаких причин вас уважать."
    coePhages "— Потому что вы предатели, и в мире кпфагов переодеваетесь как какие то додики, каких нету в кп!"

    s1 one "— Это расизм!"

    coePhages "— Нет, это справедливость."
    coePhages "— Нападайте ребята!"
    coePhages "— Их всего трое, покажем этим предателям, где ичиносефаги зимуют!"

    play music fight
    hide subaru_one_animation with moveoutleft
    hide subaru_two_animation with moveoutleft
    hide subaru_three_animation with moveoutleft

    "Такой большой поток информации полностью меня озадачил."
    "Поэтому я решил посмотреть на исход этого сражения и присоединится к победителям, а уже после анализировать информацию."
    "Самое очевидное что я заметил, так это то, что в этом мире есть мои знакомые, а также страны могут называтся в их честь."
    "И что самое главное - это мир, скорее всего, населен исключительно теми людьми, что интересуются классом превосходства. "
    
    scene battlefield with dissolve
    show leaves with dissolve
    stop music
    play music forest

    "Переведя свой взгляд обратно на поле боя я увидел, что все воины, которые принадлежали к КПфагам уже лежали на земле."
    "Но на их телах, как и под ними не было крови."

    hide leaves with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9
    show leaves with dissolve

    "При этом, смотря на трёх Нацуки Субару я не увидел у них какого либо оружия."
    "Это были смертельные газы или что-то другое?"

    coePhages "— Чёрт, мы не можем им проиграть!"
    s2 two "— Запомните новенькие. Один воин королевства Френдсоло равен по силе 5 воинам КПфагов."

    s2 two "— Мы даже не использовали оружия, а с ним у вас бы не было шансов."

    coePhages "— Это позор для нас, проиграть вам, предателям и отбросам этого мира."
    coePhages "— Это не справедливо, что такие как они имеют такую силу!"

    play sound bump
    "“Бам”."
    "Произошёл звук удара."
    "Второй Субару нанёс удар рукой в живот самому разговорчивому воину."

    s3 three "— Эй, если убьёшь его, то Серполле нас накажет."
    s2 two "— Ой, да он всё равно не узнает. Тем более эти ботики первыми напали на нас."
    s2 two "— Если будут сопротивляться, то мы их точно прибьём."
    s2 two "— Но, похоже, они уже не могут сражаться."
    s2 two "— Ладно. Сделаем то, за чем мы пришли."

    hide subaru_one_animation with moveoutleft
    hide subaru_two_animation with moveoutleft
    hide subaru_three_animation with moveoutleft

    scene forest_meadow with dissolve
    show subaru_one_animation with dissolve:
        xalign 0.1
    show subaru_two_animation with dissolve
    show subaru_three_animation with dissolve:
        xalign 0.9
    show leaves with dissolve

    "Троё Субару оставили девятерых воинов из КПфагов и выдвинулись на север - туда, откуда я пришёл."
    s3 three "— Давайте ещё по пути голубику съедим?"
    s1 one "— Да, я не против."
    "Я подумал, что сейчас самый лучший момент для того, чтобы показаться им на глаза и спросить о происходящем."
    play sound leaves
    "В кустах неподалеку от Субару начался шум и они, услышав его, насторожились."
    s2 two "— Кто-то уже проснулся?"
    $ persistent.oneChapter = True

    $ persistent.menuOneChapter = True
    rezo "— Добрый день, я тут новенький, можете рассказать мне о происходящем?"
    jump chapterTwo
    return