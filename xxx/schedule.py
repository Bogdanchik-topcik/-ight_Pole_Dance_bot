from os import getenv
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from db import new_mesidDB, give_mesidBD, del_mesidDB

sRT = Router()
bot = Bot(getenv('TOKEN'))


Ikb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='POLE DANCE', callback_data='POLE DANCE')],
    [InlineKeyboardButton(text='ФИТНЕС, ТАНЦЫ', callback_data='ФИТНЕС, ТАНЦЫ')]
])

Ikb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Видео", url='https://vk.com/video_ext.php?oid=-3408169&id=456239245&hd=2&autoplay=1')]
])

Ikb3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ТЕХНИКА БЕЗОПАСНОСТИ', callback_data='rules')]
])



async def delmess(chatID):
    ID = give_mesidBD(chatID)
    if ID:
        await bot.delete_messages(chat_id=chatID, message_ids=ID)
        del_mesidDB(chatID)


@sRT.callback_query(F.data == 'Расписание')
async def records(call: CallbackQuery, state: FSMContext): 

    await state.clear()

    chatID = call.from_user.id
    await delmess(chatID)
    await call.answer()

    new_mesidDB(await call.message.answer("По залам:"))
    media = await bot.send_media_group(chat_id=chatID, media=[
                               InputMediaPhoto(type='photo', media='AgACAgIAAxkBAAIBaGbQnv6CaOIzqCkJQdv14qjRbUVzAAJM5DEbrIWISrqIcYVdKcQrAQADAgADeAADNQQ'),
                               InputMediaPhoto(type='photo', media='AgACAgIAAxkBAAIBaWbQnxTVWJrx2ru4kWpJKLZ-EzKTAAJP5DEbrIWISrN8d31nr_tOAQADAgADeAADNQQ')
                               ])
    

    for i in media: 
        new_mesidDB(i)
    

    new_mesidDB(await call.message.answer('''По дням недели:
                              
Понедельник: 
18:30 POLE SPORT начинающие  
19:00  SALSATION
19:30 POLE SPORT продолжающие
                              
Вторник: 
8:45 POLE DANCE ART
18:30 POLE  SPORT с нуля
19:30 STRETCHING
20:00 POLE DANCE ART
                              
Среда: 
19:00 STRIP
20:00 EXOTIC POLE DANCE
20:00 CHOREO
                              
Четверг: 
18:30 POLE SPORT начинающие 
19:00 SALSATION
19:30 POLE SPORT продолжающие
                              
Пятница: 
8:45 POLE DANCE ART
18:00 POLE  SPORT с нуля
19:00 STRETCHING
20:00 POLE DANCE ART
                              
Суббота:
-
                              
Воскресенье:  
12:00 CHOREO
15:30 POLE DANCE CHOREO
16:30 EXOTIC POLE DANCE  
17.00 HANDSTAND (Стойки на руках)
18:00 STRIP
18:00 POLE SPORT смешанная
19:00 STRETCHING   '''))
    
    new_mesidDB(await call.message.answer('''По направлениям: 

💜POLE SPORT с нуля| ВТ - 18:30, ПТ - 18:00
💜POLE SPORT начинающие| ПН, ЧТ - 18:30, ВС - 18:00 (смешанная)
💜POLE SPORT продолжающие| ПН, ЧТ - 19:30
💜POLE DANCE ART| ВТ, ПТ - 8:45 | ВТ, ПТ - 20:00
💜POLE DANCE EXOTIC| СР - 20:00, ВС - 16:30
💜POLE DANCE CHOREO| ВС - 15:30
💜STRETCHING| ВТ 19:30, ПТ, ВС - 19:00
💜HANDSTAND (Стойки на руках) |ВС - 17:00
💜STRIP| СР 19:00, ВС 18:00
💜CHOREO| СР 20:00, ВС 14:30
💜SALSATION| ПН, ЧТ - 19:000'''))
    


@sRT.callback_query(F.data == 'Цены')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    await delmess(chatID)
    await call.answer()

    new_mesidDB(await call.message.answer("<b>Групповые занятия:</b>", parse_mode='HTML'))
    new_mesidDB(await call.message.answer_photo('AgACAgIAAxkBAAIFQmbUed1m5KeQrEgKGuFfeLeiiUiLAAJp4TEbEAABqUpVg-8eRm403gEAAwIAA3gAAzUE', 
            caption=" Пробное занятие БЕСПЛАТНО при покупке абонемента в день пробного занятия, срок активации абонемента 7 дней со дня покупки"))
    new_mesidDB(await call.message.answer("<b>Индивидуальный абонемент:</b>", 'HTML'))
    new_mesidDB(await call.message.answer_photo('AgACAgIAAxkBAAIFTWbUeimXBdE9EDjpVunyWoae2UNtAAJx4TEbEAABqUr1KZVtgHybhgEAAwIAA3gAAzUE'))
    new_mesidDB(await call.message.answer("<b>Аренда зала:</b>", parse_mode='HTML'))
    new_mesidDB(await call.message.answer_photo('AgACAgIAAxkBAAIFTmbUejNdK6-z4GA10cWMe8tjWLPlAAJy4TEbEAABqUqNbJhQdzvADwEAAwIAA3gAAzUE',
caption='''* Максимальная плата за 1 час - 600 рублей, даже если в зале более 4 учеников 
                
**Если тренируются ученики вместе с гостями - оплата по прайсу гостей студии.  

Условия субаренды для проведения собственных тренировок на постоянной основе обговариваются в персональном порядке. Для этого просто напишите @lightpoledancestudio .'''))
    new_mesidDB(await call.message.answer("<b>Правила использования абонементов:</b>", parse_mode='HTML'))
    new_mesidDB(await call.message.answer(
'''1. <b>СРОК абонемента</b> - 31 день (кроме безлимитного абонемента на 14 дней)
2. <b>ПРОДЛЕНИЕ АБОНЕМЕНТА</b> возможно не более, чем на 14 дней <b>по справке от врача</b> о болезни или больничному листу. Детям возможно продление до 21 дня также по справке.
3. <b>ОТРАБОТКА </b> пропущенных занятий возможна на любом направлении. Отработать можно в течение срока действия абонемента. Если пропущено часовое занятие - отработка только в часовых группах (при отработке в 1,5 часовой группе списываются 2 занятия).
4. <b>ПРОПУСК БЕЗ ПРЕДУПРЕЖДЕНИЯ</b> (не менее чем за 2 часа до занятия) при наличии действующего абонемента считается присутствием на занятии (занятие нельзя будет отработать). Предупредить можно позвонив по телефону студии +7 (996) 545-40-20 или написав в сообщения группы студии, либо можно предупредить своего тренера любым способом.
5<b>. СТУДЕНЧЕСКАЯ СКИДКА 10%</b> предоставляется при предъявлении студенческого билета. Не распостраняется на пробные и разовые занятия
6<b>. СЕМЕЙНАЯ СКИДКА 10%</b> предоставляется при покупке 2х абонементов одновременно (родитель + ребенок).  Не распостраняется на пробные и разовые занятия
7<b>. ПРИВЕДИ ДРУГА</b>
Если вы с другом приходите впервые, то оба получаете скидку 10% на свой первый абонемент в нашей студии.
Если вы уже занимаетесь и приводите к нам друга, то друг получает скидку 10% на первый абонемент, а вы скидку 10% на следующий свой абонемент.
8<b>. СКИДКА БЕЗ ПРОПУСКОВ 15%</b> предоставляется на новый абонемент в случае, если у вас есть 2 абонемента (от 8 занятий и больше) подряд без пропусков (это значит, что вы отходили 2 абонемента подряд на одно или несколько выбранных направлений без пропусков). Далее через 2 абонемента вы вновь можете получить эту скидку (абонемент со скидкой &quot;без пропусков&quot; будет первый из двух для получения новой скидки). Разница в дате покупки абонементов не должна быть больше 7 дней.
Скидка &quot;без пропусков&quot; не суммируется с семейной и студенческой скидкой.
9<b>. СРОК АКТИВАЦИИ АБОНЕМЕНТА</b> 7 дней со дня покупки, либо с даты окончания прошлого абонемента ''', parse_mode='HTML'))
    



@sRT.callback_query(F.data == 'Направления')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    await delmess(chatID)
    await call.answer()

    new_mesidDB(await call.message.answer("Направления:", reply_markup=Ikb1))
    

@sRT.callback_query(F.data == 'POLE DANCE')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    ID = give_mesidBD(chatID)
    ID = ID[1:]
    #print(ID)
    if ID:
        await bot.delete_messages(chat_id=chatID, message_ids=ID)
        del_mesidDB(chatID, all=False)
    await call.answer()

    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAIBzmbRBA7AWZaKrOKqvef5_eRk21kzAAJ_5jEbrIWISkaDA6OFf8uXAQADAgADeAADNQQ', 
    caption='Pole Dance Art\nЭто танец на пилоне, который в равной мере должен включать в себя владение трюковым пилоном и хореографией. Трюки и элементы должны быть подобранны и наложены на музыку и составлять единый образ с танцевальной составляющей. Соотношение трюков и хореографии варьируется от 50/50 до 70/30.'))

    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAIBz2bRBCZmBgfYHOzyw-XZibW1T6MyAAKA5jEbrIWISoGsdXfhXX4rAQADAgADeAADNQQ',
    caption="Pole Sport\nЗанятия направлены на изучение базовых движений, элементов, методов работы на пилоне. Люди без спортивной подготовки научатся управлять своим телом, готовить его к пилону, а имеющие спортивный опыт освоят основные принципы работы на снаряде. В группе продолжающих изучают элементы более сложного уровня."))

    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAIB0GbRBDAr8n6c1RH6vkwSDU1bLdtHAAKB5jEbrIWISoIhT86QgVgjAQADAgADeAADNQQ',
    caption="Exotic Pole Dance\nЭто женственность, грация и свобода от всего, что осталось за пределами зала. Приглушенный свет и глубокая музыка позволяют раствориться в танце и следовать за своими движениями. Раскрыть свою женскую энергетику, наслаждаться собой в отражении - это именно то, что нужно каждой женщине. "))

    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAIB0WbRBDq0mpX-L-iKT6xvK-yZiAUsAAKC5jEbrIWISq4qTpHveQ1EAQADAgADeAADNQQ',
    caption='''Pole Dance Choreo\nЕсли вы:
- любите танцы и не представляете их без пилона
- хотите развить музыкальность и чувство ритма
- понимаете важность "Dance" в вашем "Pole Dance"
приходите на тренировки #PoleDanceChoreo!

Тренировка будет состоять из разогрева, танцевальной разминки и разучивания хореографии с пилоном. Весь час, который длится занятие, вы будете учиться слушать музыку, работать над чистотой линий и исполнения.
Тренировки подойдут как начинающим полдэнсерам, так и опытным трюкачам для развития танцевальной составляющей.'''))
    

@sRT.callback_query(F.data == 'ФИТНЕС, ТАНЦЫ')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    ID = give_mesidBD(chatID)
    ID = ID[1:]
    if ID:
        await bot.delete_messages(chat_id=chatID, message_ids=ID)
        del_mesidDB(chatID, all=False)
    await call.answer()
    await call.answer()

    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICImbRC56EjrM4FfqaxkTLAAGrboBLOQAChOYxG6yFiEpx37iC6fn9nQEAAwIAA3gAAzUE',
caption='''Stretching\nЭто комплекс упражнений, направленный на растяжку связок, мышц и сухожилий. 
Положительные эффекты от занятий стрейчингом: 
· стимулирующее воздействие на кровообращение и циркуляцию лимфы в организме; 
· повышение эластичности мышц и связок;
· развитие гибкости суставов и позвоночника;
 · снижение риска болей в спине и мышечных травм;
 · улучшение координации движений.
При регулярных тренировках Вы сможете улучшить осанку, сесть на шпагат, встать на мостик. В группе используется индивидуальный подход, поэтому занятия подойдут как для начинающего, так и продвинутого уровня.'''))
    
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICI2bRC6lzVPqd3LgpxdOZ5bV4XpGDAAKF5jEbrIWISrapHq1F_Y2TAQADAgADeAADNQQ',
caption='Strip\nStrip - не просто танец на высоких каблуках, это невероятно многогранный стиль танца. Он таит в себе почти неограниченные возможности: это игра с мельчайшими музыкальными акцентами, это всегда новый образ и новая история вашей души. Насыщенность, чёткость, лаконичность - всё это Strip.'))

    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICJGbRC7QpjJVIJo52kT5ErRLRdKiAAAKG5jEbrIWISoYr4ELHI8OaAQADAgADeAADNQQ',
caption='Salsation\nSalsation® - это увлекательное сочетание различных танцевальных направлений и музыкальных ритмов. Все хореографии направления разработаны на основе трех главных принципов - сочетание лиричности, музыкальности и функциональности.'))
    
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICJWbRC7weysCLn_hsxsXnUQKC3kAcAAKH5jEbrIWISsNUbcQnEg_SAQADAgADeAADNQQ',
caption='Choreo\nАвторская хореография, совмещающая в себе несколько танцевальных направлений. Танец отражает то, как хореограф видит музыку. Автор передает настроение с помощью всех доступных ему танцевальных техник, соединяя их в единую гармоничную композицию. Если вам хочется разнообразия в танце, и вы за эксперименты - Choreo определенно для вас!'))
    
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICJmbRC8PZcAsoIwg6QfW3Ktb44aK3AAKI5jEbrIWISp8CH58a48toAQADAgADeAADNQQ',
caption='''HANDSTAND (стойки на руках)\nСтойка на руках одна из самых сложных и в тоже время необычный и эффектный трюк. Она способствует укреплению мышц плечевого пояса и спины, улучшает работу вестибулярного аппарата, укрепляет психоэмоциональное состояние и повышает самооценку.
Стойки также помогут вам при занятиях на пилоне'''))
    


@sRT.callback_query(F.data == 'Как найти')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    await delmess(chatID)
    await call.answer()

    new_mesidDB(await bot.send_location(chat_id=chatID, latitude='54.862812', longitude='83.093690'))
    new_mesidDB(await call.message.answer(text="улица Мусы Джалиля, 21/4 микрорайон Академгородок, Советский район, Новосибирск", reply_markup=Ikb2))



@sRT.callback_query(F.data == 'Тренеры')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    await delmess(chatID)
    await call.answer()

    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICMGbRL37udLThLzyh848O05k6dvy5AALP4TEb1FmISmSD9O-NVJfPAQADAgADeAADNQQ',
caption='''Юля Солопова
(Pole Dance Art, Pole Choreo, Strip)''', parse_mode=ParseMode.HTML))
    
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICMWbRL4_zoAVzlJqDIMR3DPbXByGXAAKs5jEbrIWISiPSx2XIOlT6AQADAgADeAADNQQ',
caption='''Екатерина Гольд
(Pole Sport, Stretching)'''))
    
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICMmbRL5Z-RJAHnxOQN7qhsPJ5EmtoAAKt5jEbrIWISvDjpMZ8G5EiAQADAgADeAADNQQ',
caption='''Катя Ропперт
(Exotic Pole Dance)'''))
    
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICM2bRL56m8IB_8_LX8jpw7H5y4gtRAAKG5jEbrIWISoYr4ELHI8OaAQADAgADeAADNQQ',
caption='''Марина Герлиц
(Salsation)'''))
    
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICNGbRL6ePD6zU9I0yM5RzaA49TvX-AAKI5jEbrIWISp8CH58a48toAQADAgADeAADNQQ',
caption='''Наталья Бажина
(Handstand)'''))
    
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAICNWbRL6wAASzvQBFSqZ_sFqKrwd6FmgACruYxG6yFiEqCQPfOTontPAEAAwIAA3gAAzUE',
caption='''Надя Солопова
(Choreo)'''))
    

@sRT.callback_query(F.data == 'Правила')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    await delmess(chatID)
    await call.answer()

    new_mesidDB(await call.message.answer("<b>АКЦИИ и ПРАВИЛА</b>", parse_mode='HTML'))
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAIC3GbRbkzvW-V-yzkAAezQZD8X4mj0ngACnecxG6yFiEo7Jx1e7n_pQgEAAwIAA3gAAzUE',
                                                caption="<b>ОБЯЗАТЕЛЬНО ОЗНАКОМЬТЕСЬ С ТЕХНИКОЙ БЕЗОПАСНОСТИ</b>", parse_mode='HTML',
                                                reply_markup=Ikb3))
    


@sRT.callback_query(F.data == 'rules')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    await delmess(chatID)
    await call.answer()

    new_mesidDB(await call.message.answer('''<b>Техника безопасности при проведении танцевальных занятий в студии "Light pole dance</b>"
1. Общие требования правил техники безопасности (далее ПТБ)
1.1. К танцевальным занятиям допускаются участники, прошедшие инструктаж по технике
безопасности, соблюдающие указания преподавателя, расписавшиеся в журнале регистрации инструктажа.
1.2. При проведении занятий по танцам соблюдать правила поведения, расписание танцевальных занятий, установленные режимы занятий и отдыха.
1.3. При несчастном случае пострадавший или очевидец несчастного случая обязан немедленно сообщить руководителю (преподавателю) о случившемся, который в дальнейшем принимает решения по ситуации.
1.4. Ответственность за выполнение данных правил техники безопасности, несут участники, достигшие 18 лет и родители (законные представители) несовершеннолетних посетителей студии.
1.5. Участники, допустившие невыполнение или нарушение инструкции правил техники
безопасности, привлекаются к ответственности. Со всеми обучающимися в таком случае,
проводится внеплановый инструктаж по ПТБ.
1.7. В случае не выполнения или нарушения данных правил техники безопасности
занимающимися, преподаватели групп и руководство студии ответственности не несут .
1.8. Клиент, осознавая всю сложность и травмоопасность, связанную с отработкой трюков на пилоне и акробатических номеров, всю ответственность за жизнь и здоровье берет на себя.

Техника безопасности при работе на пилоне:
1. При наличии перенесенных и хронических заболеваний перед посещением занятий необходимо в обязательном порядке проконсультироваться с врачом. Обязательно сообщайте преподавателю, ведущему занятие, о наличии таковых. После перенесенного заболевания дозируйте нагрузку, увеличивая ее постепенно.
1.1. Совершенно неприемлемо заниматься на пилоне в состоянии алкогольного или
наркотического опьянения.
1.2. В целях безопасности нельзя заниматься на голодный желудок.
1.3. Во избежание несчастных случаев рекомендуется перед началом занятий снять все
украшения (кольца, серьги, пирсинг, цепочки и тд.) и часы.
1.5. Приходить на занятие в случае плохого самочувствия запрещено.
1.6. Во время занятий соблюдать дисциплину и правила посещения студии.
2. К занятиям допускаются участники в форме предназначенной для занятий pole dance,
специальной обуви.
2.1. Перед началом занятия, приготовьте свое место. Протрите пилон спиртом для обезжиривания поверхности, используйте специальные средства, обеспечивающие более надежное сцепление с пилоном. Не пытайтесь выполнить элемент, если вы не уверены в хорошем сцеплении с пилоном. Во время тренировки протирайте пилон тряпочкой и спиртом.
2.2. Разминка перед занятиями обязательна для всех. Если Вы опоздали на разминку, необходимо провести ее самостоятельно, включая разогрев всех групп мышц, затем их растяжку и укрепление.
2.3. При выполнении элементов вниз головой не отпускайте ноги с пилона, если вы их не контролируете. Рекомендуем сползти вниз на предплечья и выйти из группировки на полу. Нельзя отпускать ноги и спину в свободное падение, когда вы находитесь невысоко у пола - это чревато ушибами ног и позвоночника! Запрещено спрыгивать с высоты.
2.4. Выполнять трюки на высоте и вниз головой до момента их освоения можно только при условии разрешения и страховки преподавателем.
2.5. Во время тренировок не подходите к танцующим на пилоне слишком близко, будьте
внимательны, ведь крутки и трюки выполняются с большим размахом, скоростью и силой.
2.9. При появлении во время занятий боли, в каких-либо частях тела, а также при плохом самочувствии, прекратить занятия и сообщить об этом преподавателю. При получении травмы немедленно сообщить об этом преподавателю.
Показать список оценивших
''', parse_mode='HTML'))
    
    new_mesidDB(await call.message.answer('''<b>Общие правила посещения студии "Light pole dance"</b>
1. При первом посещении Студии рекомендуем Вам:
- ознакомиться с расписанием групповых занятий;
- ознакомиться с правилами техники безопасности Студии.
2. Групповые занятия проводятся по расписанию, которое может быть изменено администрацией.
Также возможна замена тренера при необходимости.
Убедительная просьба: приходите на занятия БЕЗ ОПОЗДАНИЙ! Преподаватель имеет право не допустить клиента на тренировку в случае его опоздания и других случаях, когда это может быть опасно для здоровья клиента.
3. Обращаем внимание, что Вы несете полную материальную ответственность за вред,
причиненный Студии (например, за уничтожение, утерю, повреждение материальных ценностей и т.п.). Не оставляйте ценные вещи без присмотра. За утерянные вещи и вещи, оставленные без присмотра, администрация ответственности не несет.
4. Посещать занятия на пилоне можно только при отсутствии медицинских противопоказаний для таких занятий. Необходимо соблюдать технику безопасности при занятиях на пилоне, не выполнять сложные элементы без страховки тренера.
Запрещается :
1. Посещение тренировки в состоянии алкогольного и наркотического опьянения, с признаками ОРЗ, гриппа, а также других инфекционных или заразных заболеваний.
2. Курить, находиться в нетрезвом состоянии или под действием наркотических средств, а также употреблять таковые;
3. Нарушать порядок, создавать конфликтные ситуации;
4. Мешать проведению занятий;
5. Разговаривать по мобильному телефону во время занятия ,если это мешает ведению
тренировки;
6. Наблюдать за ходом проведения занятий, не оплатив занятие и не принимая в нем участие (исключение только для родителей, чьи дети посещают группу Pole kids);
7. Оставлять за собой мусор;
8. Приводить посторонних лиц, не имеющих целью заниматься в студии;
9. Ходить по залу в уличной обуви, и верхней одежде, ее необходимо снять и оставить у двери на специально предназначенном для этого пространстве.
10. Запрещается неуважительное отношение , оскорбительные высказывания в адрес тренера и других занимающихся.
11. В случае нарушения клиентом Правил посещения студии, администрация оставляет за собой право отказать клиенту в обслуживании.
12. До начала занятий необходимо ознакомиться с правилами техники безопасности, правилами посещения студии, правилами использования абонементов и посещения занятий.
ПРИОБРЕТЕНИЕ АБОНЕМЕНТА ПОДТВЕРЖДАЕТ ВАШЕ СОГЛАСИЕ СО ВСЕМИ
ПЕРЕЧИЛЕННЫМИ ПРАВИЛАМИ И ОБЯЗЫВАЕТ К ИХ ВЫПОЛНЕНИЮ.''', parse_mode='HTML'))
    

@sRT.callback_query(F.data == 'О нас')
async def prise(call: CallbackQuery, state: FSMContext):

    await state.clear()

    chatID = call.from_user.id
    await delmess(chatID)
    await call.answer()

    new_mesidDB(await call.message.answer("<b>Мы - Light Pole Dance. Студия Pole Dance и танца в Академгородке</b>", parse_mode='HTML'))
    new_mesidDB(await call.message.answer_photo(photo='AgACAgIAAxkBAAIC82bRccakmcec_2DiQSAhHxJa9yYGAALG5zEbrIWISg2Q9EFX0IYOAQADAgADeAADNQQ'))
    new_mesidDB(await call.message.answer('''Специально для вас большая профессиональная команда опытных тренеров.
Наши тренеры - чемпионы и тренеры чемпионов!

Приглашаем на занятия по направлениям:

<b>⁍ POLE DANCE ART</b>
<b>⁍ POLE SPORT</b>
<b>⁍ POLE DANCE E</b>XOTIC
<b>⁍ HANDSTAND</b>
<b>⁍ POLE CHOREO</b>
<b>⁍ STRETCHING</b>
<b>⁍ CHOREO </b>
<b>⁍ STRIP</b>

Только у нас:
- Самая большая профессиональная команда грамотных и опытных тренеров, которые развиваются в разных танцевальных стилях и видах спорта!
- 2 уютных зала с 5 пилонами и 2 пилонами;
- высота потолков 3,96 м;
- большая, удобная парковка перед студией;
- группы для новичков и продолжающих;
- индивидуальный подход и возможность заниматься персонально;
- всегда дружелюбная и комфортная атмосфера! 

<b>LightPoleDance - мы научим вас летать!</b>


Студия находится по адресу: ул.Мусы Джалиля, 21/4

Телефон студии: +7-996-545-40-20''', parse_mode='HTML'))