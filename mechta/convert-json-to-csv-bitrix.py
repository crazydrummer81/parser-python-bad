import os
import json
import os
from time import sleep
# from json2xml import json2xml
# from dicttoxml import dicttoxml
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%y%m%d-%H%M%S")
print("Current Time =", current_time)

csv_headers = ['IE_XML_ID', 'IE_NAME', 'IE_ID', 'IE_ACTIVE', 'IE_ACTIVE_FROM', 'IE_ACTIVE_TO', 'IE_PREVIEW_PICTURE', 'IE_PREVIEW_TEXT', 'IE_PREVIEW_TEXT_TYPE', 'IE_DETAIL_PICTURE', 'IE_DETAIL_TEXT', 'IE_DETAIL_TEXT_TYPE', 'IE_CODE', 'IE_SORT', 'IE_TAGS', 'IP_PROP2770', 'IP_PROP2771', 'IP_PROP2772', 'IP_PROP2773', 'IP_PROP2774', 'IP_PROP2775', 'IP_PROP2776', 'IP_PROP2777', 'IP_PROP2778', 'IP_PROP2779', 'IP_PROP2780', 'IP_PROP2781', 'IP_PROP2782', 'IP_PROP2783', 'IP_PROP2784', 'IP_PROP2785', 'IP_PROP2786', 'IP_PROP2787', 'IP_PROP2788', 'IP_PROP2996', 'IP_PROP2997', 'IP_PROP2998', 'IP_PROP2999', 'IP_PROP3000', 'IP_PROP3001', 'IP_PROP3002', 'IP_PROP3003', 'IP_PROP3004', 'IP_PROP3005', 'IP_PROP3006', 'IP_PROP3007', 'IP_PROP3008', 'IP_PROP3010', 'IP_PROP3009', 'IP_PROP3011', 'IP_PROP3012', 'IP_PROP3013', 'IP_PROP3014', 'IP_PROP3015', 'IP_PROP3016', 'IP_PROP3017', 'IP_PROP3018', 'IP_PROP3019', 'IP_PROP3020', 'IP_PROP3021', 'IP_PROP3022', 'IP_PROP3023', 'IP_PROP3024', 'IP_PROP3025', 'IP_PROP3026', 'IP_PROP3027', 'IP_PROP3028', 'IP_PROP3029', 'IP_PROP3030', 'IP_PROP3031', 'IP_PROP3032', 'IP_PROP3033', 'IP_PROP3034', 'IP_PROP3035', 'IP_PROP3036', 'IP_PROP3037', 'IP_PROP3038', 'IP_PROP3039', 'IP_PROP3040', 'IP_PROP3041', 'IP_PROP3042', 'IP_PROP3043', 'IP_PROP3044', 'IP_PROP3045', 'IP_PROP3046', 'IP_PROP3047', 'IP_PROP3048', 'IP_PROP3049', 'IP_PROP3050', 'IP_PROP3051', 'IP_PROP3052', 'IP_PROP3053', 'IP_PROP3054', 'IP_PROP3055', 'IP_PROP3056', 'IP_PROP3057', 'IP_PROP3058', 'IP_PROP3059', 'IP_PROP3060', 'IP_PROP3061', 'IP_PROP3062', 'IP_PROP3063', 'IP_PROP3064', 'IP_PROP3065', 'IP_PROP3066', 'IP_PROP3067', 'IP_PROP3068', 'IP_PROP3069', 'IP_PROP3070', 'IP_PROP3071', 'IP_PROP3072', 'IP_PROP3073', 'IP_PROP3074', 'IP_PROP3075', 'IP_PROP3076', 'IP_PROP3077', 'IP_PROP3078', 'IP_PROP3079', 'IP_PROP3080', 'IP_PROP3081', 'IP_PROP3082', 'IP_PROP3083', 'IP_PROP3084', 'IP_PROP3085', 'IP_PROP3086', 'IP_PROP3087', 'IP_PROP3088', 'IP_PROP3089', 'IP_PROP3090', 'IP_PROP3091', 'IP_PROP3092', 'IP_PROP3093', 'IP_PROP3094', 'IP_PROP3095', 'IP_PROP3096', 'IP_PROP3097', 'IP_PROP3098', 'IP_PROP3099', 'IP_PROP3100', 'IP_PROP3101', 'IP_PROP3102', 'IP_PROP3103', 'IP_PROP3104', 'IP_PROP3105', 'IP_PROP3106', 'IP_PROP3107', 'IP_PROP3108', 'IP_PROP3109', 'IP_PROP3110', 'IP_PROP3111', 'IP_PROP3112', 'IP_PROP3113', 'IP_PROP3114', 'IP_PROP3115', 'IP_PROP3116', 'IP_PROP3117', 'IP_PROP3118', 'IP_PROP3119', 'IP_PROP3120', 'IP_PROP3121', 'IP_PROP3122', 'IP_PROP3123', 'IP_PROP3124', 'IP_PROP3125', 'IP_PROP3126', 'IP_PROP3127', 'IP_PROP3128', 'IP_PROP3129', 'IP_PROP3130', 'IP_PROP3131', 'IP_PROP3132', 'IP_PROP3133', 'IP_PROP3134', 'IP_PROP3135', 'IP_PROP3136', 'IP_PROP3137', 'IP_PROP3138', 'IP_PROP3139', 'IP_PROP3140', 'IP_PROP3141', 'IP_PROP3142', 'IP_PROP3143', 'IP_PROP3144', 'IP_PROP3145', 'IP_PROP3146', 'IP_PROP3147', 'IP_PROP3148', 'IP_PROP3149', 'IP_PROP3150', 'IP_PROP3151', 'IP_PROP3152', 'IP_PROP3153', 'IP_PROP3154', 'IP_PROP3155', 'IP_PROP3156', 'IP_PROP3157', 'IP_PROP3158', 'IP_PROP3159', 'IP_PROP3160', 'IP_PROP3161', 'IP_PROP3162', 'IP_PROP3163', 'IP_PROP3164', 'IP_PROP3165', 'IP_PROP3166', 'IP_PROP3167', 'IP_PROP3168', 'IP_PROP3169', 'IP_PROP3170', 'IP_PROP3171', 'IP_PROP3172', 'IP_PROP3173', 'IP_PROP3174', 'IP_PROP3175', 'IC_GROUP0', 'IC_GROUP1', 'IC_GROUP2', 'IC_GROUP3', 'IC_GROUP4', 'IC_GROUP5', 'IC_GROUP6', 'IC_GROUP7', 'IC_GROUP8', 'IC_GROUP9'];

csv_line = {
'IE_XML_ID': '', # Внешний код (B_IBLOCK_ELEMENT.XML_ID) | 10
'IE_NAME': '', # Название (B_IBLOCK_ELEMENT.NAME) | 20
'IE_ID': '', # ID (B_IBLOCK_ELEMENT.ID) | 30
'IE_ACTIVE': '', # Активность (B_IBLOCK_ELEMENT.ACTIVE) | 40
'IE_ACTIVE_FROM': '', # Начало активности (время) (B_IBLOCK_ELEMENT.ACTIVE_FROM) | 50
'IE_ACTIVE_TO': '', # Окончание активности (время) (B_IBLOCK_ELEMENT.ACTIVE_TO) | 60
'IE_PREVIEW_PICTURE': '', # Картинка для анонса (B_IBLOCK_ELEMENT.PREVIEW_PICTURE) | 70
'IE_PREVIEW_TEXT': '', # Описание для анонса (B_IBLOCK_ELEMENT.PREVIEW_TEXT) | 80
'IE_PREVIEW_TEXT_TYPE': '', # Тип описания для анонса (B_IBLOCK_ELEMENT.PREVIEW_TEXT_TYPE) | 90
'IE_DETAIL_PICTURE': '', # Детальная картинка (B_IBLOCK_ELEMENT.DETAIL_PICTURE) | 100
'IE_DETAIL_TEXT': '', # Детальное описание (B_IBLOCK_ELEMENT.DETAIL_TEXT) | 110
'IE_DETAIL_TEXT_TYPE': '', # Тип детального описания (B_IBLOCK_ELEMENT.DETAIL_TEXT_TYPE) | 120
'IE_CODE': '', # Символьный код (B_IBLOCK_ELEMENT.CODE) | 130
'IE_SORT': '', # Сортировка (B_IBLOCK_ELEMENT.SORT) | 140
'IE_TAGS': '', # Теги (B_IBLOCK_ELEMENT.TAGS) | 150
'IP_PROP2770': '', # Свойство "Регионы" | 160
'IP_PROP2771': '', # Свойство "Бренд " | 170
'IP_PROP2772': '', # Свойство "Услуги" | 180
'IP_PROP2773': '', # Свойство "Похожие товары" | 190
'IP_PROP2774': '', # Свойство "Хит" | 200
'IP_PROP2775': '', # Свойство "Новинка" | 210
'IP_PROP2776': '', # Свойство "Распродажа" | 220
'IP_PROP2777': '', # Свойство "Картинки" | 230
'IP_PROP2778': '', # Свойство "Видео в контенте" | 240
'IP_PROP2779': '', # Свойство "Видео в табах" | 250
'IP_PROP2780': '', # Свойство "Файлы" | 260
'IP_PROP2781': '', # Свойство "Документы" | 270
'IP_PROP2782': '', # Свойство "Рейтинг" | 280
'IP_PROP2783': '', # Свойство "Количество проголосовавших" | 290
'IP_PROP2784': '', # Свойство "Сумма оценок" | 300
'IP_PROP2785': '', # Свойство "ID поста блога для комментариев" | 310
'IP_PROP2786': '', # Свойство "Количество комментариев" | 320
'IP_PROP2787': '', # Свойство "discounted" | 330
'IP_PROP2788': '', # Свойство "full" | 340
'IP_PROP2996': '', # Свойство "Производитель" | 350
'IP_PROP2997': '', # Свойство "Страна производства" | 360
'IP_PROP2998': '', # Свойство "SIM-карта" | 370
'IP_PROP2999': '', # Свойство "Графический процессор" | 380
'IP_PROP3000': '', # Свойство "Встроенные динамики" | 390
'IP_PROP3001': '', # Свойство "Встроенный микрофон" | 400
'IP_PROP3002': '', # Свойство "Микрофон" | 410
'IP_PROP3003': '', # Свойство "HDMI" | 420
'IP_PROP3004': '', # Свойство "Разъем для наушников" | 430
'IP_PROP3005': '', # Свойство "Индикация" | 440
'IP_PROP3006': '', # Свойство "Индикация уровня заряда" | 450
'IP_PROP3007': '', # Свойство "Количество аккумуляторов в трубке" | 460
'IP_PROP3008': '', # Свойство "Количество трубок в комплекте" | 470
'IP_PROP3010': '', # Свойство "Светочувствительность ISO" | 480
'IP_PROP3009': '', # Свойство "Материал корпуса" | 490
'IP_PROP3011': '', # Свойство "Тип и размер матрицы" | 500
'IP_PROP3012': '', # Свойство "Эффект. разрешение, Мпикс" | 510
'IP_PROP3013': '', # Свойство "Мобильная ОС" | 520
'IP_PROP3014': '', # Свойство "Объектив" | 530
'IP_PROP3015': '', # Свойство "Светосила (F-число)" | 540
'IP_PROP3016': '', # Свойство "Фокусное расстояние" | 550
'IP_PROP3017': '', # Свойство "Дополнительные опции" | 560
'IP_PROP3018': '', # Свойство "Ёмкость, мАч" | 570
'IP_PROP3019': '', # Свойство "Автоответчик" | 580
'IP_PROP3020': '', # Свойство "Возможность настенной установки" | 590
'IP_PROP3021': '', # Свойство "Дальность действия в помещении, м" | 600
'IP_PROP3022': '', # Свойство "Диаметр мембран, мм" | 610
'IP_PROP3023': '', # Свойство "Диапазон воспроизводимых частот, Гц" | 620
'IP_PROP3024': '', # Свойство "Диапазон частот, Гц" | 630
'IP_PROP3025': '', # Свойство "Дисплей" | 640
'IP_PROP3026': '', # Свойство "Дисплей трубки" | 650
'IP_PROP3027': '', # Свойство "Длина кабеля, м" | 660
'IP_PROP3028': '', # Свойство "Для моделей" | 670
'IP_PROP3029': '', # Свойство "Для телефонов" | 680
'IP_PROP3030': '', # Свойство "Защита от воды и пыли" | 690
'IP_PROP3031': '', # Свойство "Индикатор уровня зарядки" | 700
'IP_PROP3032': '', # Свойство "Количество каналов" | 710
'IP_PROP3033': '', # Свойство "Количество раций в комплекте" | 720
'IP_PROP3034': '', # Свойство "Количество сигналов вызова" | 730
'IP_PROP3035': '', # Свойство "Макс. входное напряжение" | 740
'IP_PROP3036': '', # Свойство "Максимальная высота, см" | 750
'IP_PROP3037': '', # Свойство "Максимальная нагрузка, кг" | 760
'IP_PROP3038': '', # Свойство "Максимальный вес нагрузки, кг" | 770
'IP_PROP3039': '', # Свойство "Материал сумки/чехла" | 780
'IP_PROP3040': '', # Свойство "Минимальная высота, см" | 790
'IP_PROP3041': '', # Свойство "Мощность передатчика, Вт" | 800
'IP_PROP3042': '', # Свойство "Наличие лицензии" | 810
'IP_PROP3043': '', # Свойство "Определитель номера" | 820
'IP_PROP3044': '', # Свойство "Память принятых вызовов" | 830
'IP_PROP3045': '', # Свойство "Повторный набор номера" | 840
'IP_PROP3046': '', # Свойство "Рабочая частота, МГц" | 850
'IP_PROP3047': '', # Свойство "Рабочий диапазон температур, C" | 860
'IP_PROP3048': '', # Свойство "Радиус действия в помещении, м" | 870
'IP_PROP3049': '', # Свойство "Радиус действия, км" | 880
'IP_PROP3050': '', # Свойство "Радиус действия, м" | 890
'IP_PROP3051': '', # Свойство "Размер ремешка, см" | 900
'IP_PROP3052': '', # Свойство "Режимы дисплея" | 910
'IP_PROP3053': '', # Свойство "Ремешок" | 920
'IP_PROP3054': '', # Свойство "Совместимость" | 930
'IP_PROP3055': '', # Свойство "Совместимость со смартфономи" | 940
'IP_PROP3056': '', # Свойство "Спикерфон" | 950
'IP_PROP3057': '', # Свойство "Текстовый дисплей трубки" | 960
'IP_PROP3058': '', # Свойство "Телефонная книга" | 970
'IP_PROP3059': '', # Свойство "Тип кабеля (шнура)" | 980
'IP_PROP3060': '', # Свойство "Тип наушников" | 990
'IP_PROP3061': '', # Свойство "Тип подключения" | 1000
'IP_PROP3062': '', # Свойство "Тональный набор" | 1010
'IP_PROP3063': '', # Свойство "Управление" | 1020
'IP_PROP3064': '', # Свойство "Управление через bluetooth" | 1030
'IP_PROP3065': '', # Свойство "Управление через аудио линейный порт телефона" | 1040
'IP_PROP3066': '', # Свойство "Формат записи" | 1050
'IP_PROP3067': '', # Свойство "Число USB портов" | 1060
'IP_PROP3068': '', # Свойство "Чувствительность наушников, дБ/В" | 1070
'IP_PROP3069': '', # Свойство "Чувствительность, дБ" | 1080
'IP_PROP3070': '', # Свойство "Штекер" | 1090
'IP_PROP3071': '', # Свойство "я удален" | 1100
'IP_PROP3072': '', # Свойство "Встроенная память, Гб" | 1110
'IP_PROP3073': '', # Свойство "Максимальная емкость карты памяти, Гб" | 1120
'IP_PROP3074': '', # Свойство "Объем оперативной памяти, Гб" | 1130
'IP_PROP3075': '', # Свойство "Объем памяти, ГБ" | 1140
'IP_PROP3076': '', # Свойство "Тип карты памяти" | 1150
'IP_PROP3077': '', # Свойство "Тип носителя данных" | 1160
'IP_PROP3078': '', # Свойство "Беспроводная зарядка" | 1170
'IP_PROP3079': '', # Свойство "Быстрая зарядка" | 1180
'IP_PROP3080': '', # Свойство "Время в режиме ожидания, ч" | 1190
'IP_PROP3081': '', # Свойство "Время в режиме разговора, ч" | 1200
'IP_PROP3082': '', # Свойство "Время зарядки" | 1210
'IP_PROP3083': '', # Свойство "Время зарядки аккумулятора, ч" | 1220
'IP_PROP3084': '', # Свойство "Время работы от аккумулятора, ч" | 1230
'IP_PROP3085': '', # Свойство "Емкость аккумулятора, мАч" | 1240
'IP_PROP3086': '', # Свойство "Питание" | 1250
'IP_PROP3087': '', # Свойство "Работа от аккумулятора, ч" | 1260
'IP_PROP3088': '', # Свойство "Размер аккумулятора" | 1270
'IP_PROP3089': '', # Свойство "Тип аккумулятора" | 1280
'IP_PROP3090': '', # Свойство "Модель процессора" | 1290
'IP_PROP3091': '', # Свойство "Процессор, (МГц, количество ядер)" | 1300
'IP_PROP3092': '', # Свойство "LBS" | 1310
'IP_PROP3093': '', # Свойство "Бренд" | 1320
'IP_PROP3094': '', # Свойство "Гарантия" | 1330
'IP_PROP3095': '', # Свойство "Длина кабеля" | 1340
'IP_PROP3096': '', # Свойство "Для корпуса размером, мм" | 1350
'IP_PROP3097': '', # Свойство "Дополнительно" | 1360
'IP_PROP3098': '', # Свойство "Индикатор состояния" | 1370
'IP_PROP3099': '', # Свойство "Кнопки управления" | 1380
'IP_PROP3100': '', # Свойство "Компас" | 1390
'IP_PROP3101': '', # Свойство "Комплектация" | 1400
'IP_PROP3102': '', # Свойство "Крепление на ремень" | 1410
'IP_PROP3103': '', # Свойство "Макс. выходное напряжение" | 1420
'IP_PROP3104': '', # Свойство "Материал" | 1430
'IP_PROP3105': '', # Свойство "Материал ремешка" | 1440
'IP_PROP3106': '', # Свойство "Модель" | 1450
'IP_PROP3107': '', # Свойство "Наличие регулятора громкости" | 1460
'IP_PROP3108': '', # Свойство "Поддержка 5G" | 1470
'IP_PROP3109': '', # Свойство "Поддержка видеозвонков" | 1480
'IP_PROP3110': '', # Свойство "Поддержка голосовой связи" | 1490
'IP_PROP3111': '', # Свойство "Поддержка казахского языка" | 1500
'IP_PROP3112': '', # Свойство "Поддержка сервисов Google Play" | 1510
'IP_PROP3113': '', # Свойство "Подключение дополнительных трубок" | 1520
'IP_PROP3114': '', # Свойство "Процессор" | 1530
'IP_PROP3115': '', # Свойство "Серия" | 1540
'IP_PROP3116': '', # Свойство "Страна производитель" | 1550
'IP_PROP3117': '', # Свойство "Тип батареи" | 1560
'IP_PROP3118': '', # Свойство "Фонарик" | 1570
'IP_PROP3119': '', # Свойство "Фотокамера" | 1580
'IP_PROP3120': '', # Свойство "Шумоподавление" | 1590
'IP_PROP3121': '', # Свойство "Стандарты сети" | 1600
'IP_PROP3122': '', # Свойство "Формат мелодии" | 1610
'IP_PROP3123': '', # Свойство "ANT+" | 1620
'IP_PROP3124': '', # Свойство "Bluetooth" | 1630
'IP_PROP3125': '', # Свойство "GPRS" | 1640
'IP_PROP3126': '', # Свойство "GPS" | 1650
'IP_PROP3127': '', # Свойство "NFC" | 1660
'IP_PROP3128': '', # Свойство "USB" | 1670
'IP_PROP3129': '', # Свойство "WAP" | 1680
'IP_PROP3130': '', # Свойство "Wi-Fi" | 1690
'IP_PROP3131': '', # Свойство "Поддержка 4G (LTE)" | 1700
'IP_PROP3132': '', # Свойство "Автофокус" | 1710
'IP_PROP3133': '', # Свойство "Макс. разрешение фотоснимков, Пикс" | 1720
'IP_PROP3134': '', # Свойство "Особенности тыловой камеры" | 1730
'IP_PROP3135': '', # Свойство "Особенности фронтальной камеры" | 1740
'IP_PROP3136': '', # Свойство "Разрешение фотокамеры, Мпикс" | 1750
'IP_PROP3137': '', # Свойство "Режим видеосъемки" | 1760
'IP_PROP3138': '', # Свойство "Фронтальная камера (для видеозвонков), Мпикс" | 1770
'IP_PROP3139': '', # Свойство "Сканер отпечатка пальца" | 1780
'IP_PROP3140': '', # Свойство "Акселерометр" | 1790
'IP_PROP3141': '', # Свойство "Барометр" | 1800
'IP_PROP3142': '', # Свойство "Блокировка клавиатуры" | 1810
'IP_PROP3143': '', # Свойство "Вибрация" | 1820
'IP_PROP3144': '', # Свойство "Встроенное оборудование и функции" | 1830
'IP_PROP3145': '', # Свойство "Гироскоп" | 1840
'IP_PROP3146': '', # Свойство "Голосовой набор" | 1850
'IP_PROP3147': '', # Свойство "Датчик освещенности" | 1860
'IP_PROP3148': '', # Свойство "Датчик сердечного ритма" | 1870
'IP_PROP3149': '', # Свойство "Ожидание/удержание вызова" | 1880
'IP_PROP3150': '', # Свойство "Ответить/закончить разговор" | 1890
'IP_PROP3151': '', # Свойство "Панорамная съемка" | 1900
'IP_PROP3152': '', # Свойство "Повтор последнего номера" | 1910
'IP_PROP3153': '', # Свойство "Подтверждение окончания передачи" | 1920
'IP_PROP3154': '', # Свойство "Распознавание лица" | 1930
'IP_PROP3155': '', # Свойство "Режим мониторинга/сканирования" | 1940
'IP_PROP3156': '', # Свойство "Режимы видеосъемки" | 1950
'IP_PROP3157': '', # Свойство "Система стабилизации изображения" | 1960
'IP_PROP3158': '', # Свойство "Вес без упаковки (нетто), кг" | 1970
'IP_PROP3159': '', # Свойство "Вес в упаковке (брутто), кг" | 1980
'IP_PROP3160': '', # Свойство "Вес трубки, гр" | 1990
'IP_PROP3161': '', # Свойство "Габариты в упаковке (ВхШхГ), см" | 2000
'IP_PROP3162': '', # Свойство "Габариты устройства (ВхШхГ), см" | 2010
'IP_PROP3163': '', # Свойство "Размер базы (ВхШхГ), мм" | 2020
'IP_PROP3164': '', # Свойство "Размер трубки (ВхШхГ), мм" | 2030
'IP_PROP3165': '', # Свойство "Цвет" | 2040
'IP_PROP3166': '', # Свойство "Датчик ориентации экрана" | 2050
'IP_PROP3167': '', # Свойство "Диагональ экрана, дюйм" | 2060
'IP_PROP3168': '', # Свойство "Количество цветов дисплея" | 2070
'IP_PROP3169': '', # Свойство "Контраст" | 2080
'IP_PROP3170': '', # Свойство "Разрешение" | 2090
'IP_PROP3171': '', # Свойство "Разрешение дисплея, пикс" | 2100
'IP_PROP3172': '', # Свойство "Сенсорный дисплей" | 2110
'IP_PROP3173': '', # Свойство "Технология изготовления дисплея" | 2120
'IP_PROP3174': '', # Свойство "Формат" | 2130
'IP_PROP3175': '', # Свойство "Частота обновления, Гц" | 2140
'IC_GROUP0': '', # Группа уровня (1) | 2150
'IC_GROUP1': '', # Группа уровня (2) | 2160
'IC_GROUP2': '', # Группа уровня (3) | 2170
'IC_GROUP3': '', # Группа уровня (4) | 2180
'IC_GROUP4': '', # Группа уровня (5) | 2190
'IC_GROUP5': '', # Группа уровня (6) | 2200
'IC_GROUP6': '', # Группа уровня (7) | 2210
'IC_GROUP7': '', # Группа уровня (8) | 2220
'IC_GROUP8': '', # Группа уровня (9) | 2230
'IC_GROUP9': '', # Группа уровня (10)
}
csv_headers = csv_line.keys()
delimiter = '^'

source_folder = 'result/'
target_folder = 'csv/'
if not os.path.isdir(target_folder):
	os.mkdir(target_folder)
# target_filename = 'stanki-test' + '-' + current_time + '.csv'
# target_xml_filename = 'stanki-test' + '-' + current_time + '.xml'
target_filename = 'mechta-' + current_time + '.csv'
target_xml_filename = 'stanki-test.xml'
xml_id = 'MECHTAKZ'

files = os.listdir(source_folder)
resutl_csv = delimiter.join(csv_headers) + '\n'
limit = 10000
# os.remove(target_folder+target_filename)
# os.remove(target_folder+target_xml_filename)

ft = open(target_folder+target_filename, 'w+', encoding='utf-8')
# ftx = open(target_folder+target_xml_filename, 'w+', encoding='utf-8')

ft.write(delimiter.join(csv_headers) + '\n')
for i, filename in enumerate(files):
	if i >= limit: break
	if not os.path.isdir(source_folder+filename):
		print('-------> '+filename+' <-------')
		with open(source_folder+filename, 'r', encoding='utf-8') as fs:
			source_dict = json.load(fs)
			target_dict = {
				'IE_XML_ID': '', # Внешний код (B_IBLOCK_ELEMENT.XML_ID) | 10
				'IE_NAME': source_dict['product_name'] or '',
				'IE_ID': '', # ID (B_IBLOCK_ELEMENT.ID) | 30
				'IE_ACTIVE': '', # Активность (B_IBLOCK_ELEMENT.ACTIVE) | 40
				'IE_ACTIVE_FROM': '', # Начало активности (время) (B_IBLOCK_ELEMENT.ACTIVE_FROM) | 50
				'IE_ACTIVE_TO': '', # Окончание активности (время) (B_IBLOCK_ELEMENT.ACTIVE_TO) | 60
				'IE_PREVIEW_PICTURE': '', # Картинка для анонса (B_IBLOCK_ELEMENT.PREVIEW_PICTURE) | 70
				'IE_PREVIEW_TEXT': '', # Описание для анонса (B_IBLOCK_ELEMENT.PREVIEW_TEXT) | 80
				'IE_PREVIEW_TEXT_TYPE': '', # Тип описания для анонса (B_IBLOCK_ELEMENT.PREVIEW_TEXT_TYPE) | 90
				'IE_DETAIL_PICTURE': source_dict['main_image']['url'] or '',
				'IE_DETAIL_TEXT': source_dict['product_description']['content'] or '',
				'IE_DETAIL_TEXT_TYPE': 'html', # Тип детального описания (B_IBLOCK_ELEMENT.DETAIL_TEXT_TYPE) | 120
				'IE_CODE': '', # Символьный код (B_IBLOCK_ELEMENT.CODE) | 130
				'IE_SORT': '', # Сортировка (B_IBLOCK_ELEMENT.SORT) | 140
				'IE_TAGS': '', # Теги (B_IBLOCK_ELEMENT.TAGS) | 150
				'IP_PROP2770': '', # Свойство "Регионы" | 160
				'IP_PROP2771': source_dict['Разное']['Бренд'] if 'Бренд' in source_dict else '',
				'IP_PROP2772': '', # Свойство "Услуги" | 180
				'IP_PROP2773': '', # Свойство "Похожие товары" | 190
				'IP_PROP2774': '', # Свойство "Хит" | 200
				'IP_PROP2775': '', # Свойство "Новинка" | 210
				'IP_PROP2776': '', # Свойство "Распродажа" | 220
				'IP_PROP2777' : '$'.join([item['url'] for item in source_dict['additional_images']]) or '',
				'IP_PROP2787' : source_dict['product_price']['discounted'] if 'discounted' in source_dict else '',
				'IP_PROP2788' : source_dict['product_price']['full'] if 'full' in source_dict else '',
				'IP_PROP2996' : source_dict['Разное']['Бренд'] if 'Бренд' in source_dict else '',
				'IP_PROP2997' : source_dict['Разное']['Страна производитель'] if 'Страна производитель' in source_dict else '',
				'IP_PROP2998' : source_dict['SIM карта']['SIM-карта'] if 'SIM-карта' in source_dict else '',
				'IP_PROP2999' : source_dict['Видеокарта']['Графический процессор'] if 'Графический процессор' in source_dict else '',
				'IP_PROP3000' : source_dict['Звук']['Встроенные динамики'] if 'Встроенные динамики' in source_dict else '',
				'IP_PROP3001' : source_dict['Звук']['Встроенный микрофон'] if 'Встроенный микрофон' in source_dict else '',
				'IP_PROP3002' : source_dict['Звук']['Микрофон'] if 'Микрофон' in source_dict else '',
				'IP_PROP3003' : source_dict['Интерфейсы']['HDMI'] if 'HDMI' in source_dict else '',
				'IP_PROP3004' : source_dict['Интерфейсы']['Разъем для наушников'] if 'Разъем для наушников' in source_dict else '',
				'IP_PROP3005' : source_dict['Информационные функции']['Индикация'] if 'Индикация' in source_dict else '',
				'IP_PROP3006' : source_dict['Информационные функции']['Индикация уровня заряда'] if 'Индикация уровня заряда' in source_dict else '',
				'IP_PROP3007' : source_dict['Комплектация']['Количество аккумуляторов в трубке'] if 'Количество аккумуляторов в трубке' in source_dict else '',
				'IP_PROP3008' : source_dict['Комплектация']['Светочувствительность ISO'] if 'Светочувствительность ISO' in source_dict else '',
				'IP_PROP3010' : source_dict['Корпус']['Количество трубок в комплекте'] if 'Количество трубок в комплекте' in source_dict else '',
				'IP_PROP3009' : source_dict['Матрица']['Материал корпуса'] if 'Материал корпуса' in source_dict else '',
				'IP_PROP3011' : source_dict['Матрица']['Тип и размер матрицы'] if 'Тип и размер матрицы' in source_dict else '',
				'IP_PROP3012' : source_dict['Матрица']['Эффект. разрешение, Мпикс'] if 'Эффект. разрешение, Мпикс' in source_dict else '',
				'IP_PROP3013' : source_dict['Операционная система']['Мобильная ОС'] if 'Мобильная ОС' in source_dict else '',
				'IP_PROP3014' : source_dict['Оптика']['Объектив'] if 'Объектив' in source_dict else '',
				'IP_PROP3015' : source_dict['Оптика']['Светосила (F-число)'] if 'Светосила (F-число)' in source_dict else '',
				'IP_PROP3016' : source_dict['Оптика']['Фокусное расстояние'] if 'Фокусное расстояние' in source_dict else '',
				'IP_PROP3017' : source_dict['Опции']['Дополнительные опции'] if 'Дополнительные опции' in source_dict else '',
				'IP_PROP3018' : source_dict['Основные характеристики']['Ёмкость, мАч'] if 'Ёмкость, мАч' in source_dict else '',
				'IP_PROP3019' : source_dict['Основные характеристики']['Автоответчик'] if 'Автоответчик' in source_dict else '',
				'IP_PROP3020' : source_dict['Основные характеристики']['Возможность настенной установки'] if 'Возможность настенной установки' in source_dict else '',
				'IP_PROP3021' : source_dict['Основные характеристики']['Дальность действия в помещении, м'] if 'Дальность действия в помещении, м' in source_dict else '',
				'IP_PROP3022' : source_dict['Основные характеристики']['Диаметр мембран, мм'] if 'Диаметр мембран, мм' in source_dict else '',
				'IP_PROP3023' : source_dict['Основные характеристики']['Диапазон воспроизводимых частот, Гц'] if 'Диапазон воспроизводимых частот, Гц' in source_dict else '',
				'IP_PROP3024' : source_dict['Основные характеристики']['Диапазон частот, Гц'] if 'Диапазон частот, Гц' in source_dict else '',
				'IP_PROP3025' : source_dict['Основные характеристики']['Дисплей'] if 'Дисплей' in source_dict else '',
				'IP_PROP3026' : source_dict['Основные характеристики']['Дисплей трубки'] if 'Дисплей трубки' in source_dict else '',
				'IP_PROP3027' : source_dict['Основные характеристики']['Длина кабеля, м'] if 'Длина кабеля, м' in source_dict else '',
				'IP_PROP3028' : source_dict['Основные характеристики']['Для моделей'] if 'Для моделей' in source_dict else '',
				'IP_PROP3029' : source_dict['Основные характеристики']['Для телефонов'] if 'Для телефонов' in source_dict else '',
				'IP_PROP3030' : source_dict['Основные характеристики']['Защита от воды и пыли'] if 'Защита от воды и пыли' in source_dict else '',
				'IP_PROP3031' : source_dict['Основные характеристики']['Индикатор уровня зарядки'] if 'Индикатор уровня зарядки' in source_dict else '',
				'IP_PROP3032' : source_dict['Основные характеристики']['Количество каналов'] if 'Количество каналов' in source_dict else '',
				'IP_PROP3033' : source_dict['Основные характеристики']['Количество раций в комплекте'] if 'Количество раций в комплекте' in source_dict else '',
				'IP_PROP3034' : source_dict['Основные характеристики']['Количество сигналов вызова'] if 'Количество сигналов вызова' in source_dict else '',
				'IP_PROP3035' : source_dict['Основные характеристики']['Макс. входное напряжение'] if 'Макс. входное напряжение' in source_dict else '',
				'IP_PROP3036' : source_dict['Основные характеристики']['Максимальная высота, см'] if 'Максимальная высота, см' in source_dict else '',
				'IP_PROP3037' : source_dict['Основные характеристики']['Максимальная нагрузка, кг'] if 'Максимальная нагрузка, кг' in source_dict else '',
				'IP_PROP3038' : source_dict['Основные характеристики']['Максимальный вес нагрузки, кг'] if 'Максимальный вес нагрузки, кг' in source_dict else '',
				'IP_PROP3039' : source_dict['Основные характеристики']['Материал сумки/чехла'] if 'Материал сумки/чехла' in source_dict else '',
				'IP_PROP3040' : source_dict['Основные характеристики']['Минимальная высота, см'] if 'Минимальная высота, см' in source_dict else '',
				'IP_PROP3041' : source_dict['Основные характеристики']['Мощность передатчика, Вт'] if 'Мощность передатчика, Вт' in source_dict else '',
				'IP_PROP3042' : source_dict['Основные характеристики']['Наличие лицензии'] if 'Наличие лицензии' in source_dict else '',
				'IP_PROP3043' : source_dict['Основные характеристики']['Определитель номера'] if 'Определитель номера' in source_dict else '',
				'IP_PROP3044' : source_dict['Основные характеристики']['Память принятых вызовов'] if 'Память принятых вызовов' in source_dict else '',
				'IP_PROP3045' : source_dict['Основные характеристики']['Повторный набор номера'] if 'Повторный набор номера' in source_dict else '',
				'IP_PROP3046' : source_dict['Основные характеристики']['Рабочая частота, МГц'] if 'Рабочая частота, МГц' in source_dict else '',
				'IP_PROP3047' : source_dict['Основные характеристики']['Рабочий диапазон температур, C'] if 'Рабочий диапазон температур, C' in source_dict else '',
				'IP_PROP3048' : source_dict['Основные характеристики']['Радиус действия в помещении, м'] if 'Радиус действия в помещении, м' in source_dict else '',
				'IP_PROP3049' : source_dict['Основные характеристики']['Радиус действия, км'] if 'Радиус действия, км' in source_dict else '',
				'IP_PROP3050' : source_dict['Основные характеристики']['Радиус действия, м'] if 'Радиус действия, м' in source_dict else '',
				'IP_PROP3051' : source_dict['Основные характеристики']['Размер ремешка, см'] if 'Размер ремешка, см' in source_dict else '',
				'IP_PROP3052' : source_dict['Основные характеристики']['Режимы дисплея'] if 'Режимы дисплея' in source_dict else '',
				'IP_PROP3053' : source_dict['Основные характеристики']['Ремешок'] if 'Ремешок' in source_dict else '',
				'IP_PROP3054' : source_dict['Основные характеристики']['Совместимость'] if 'Совместимость' in source_dict else '',
				'IP_PROP3055' : source_dict['Основные характеристики']['Совместимость со смартфономи'] if 'Совместимость со смартфономи' in source_dict else '',
				'IP_PROP3056' : source_dict['Основные характеристики']['Спикерфон'] if 'Спикерфон' in source_dict else '',
				'IP_PROP3057' : source_dict['Основные характеристики']['Текстовый дисплей трубки'] if 'Текстовый дисплей трубки' in source_dict else '',
				'IP_PROP3058' : source_dict['Основные характеристики']['Телефонная книга'] if 'Телефонная книга' in source_dict else '',
				'IP_PROP3059' : source_dict['Основные характеристики']['Тип кабеля (шнура)'] if 'Тип кабеля (шнура)' in source_dict else '',
				'IP_PROP3060' : source_dict['Основные характеристики']['Тип наушников'] if 'Тип наушников' in source_dict else '',
				'IP_PROP3061' : source_dict['Основные характеристики']['Тип подключения'] if 'Тип подключения' in source_dict else '',
				'IP_PROP3062' : source_dict['Основные характеристики']['Тональный набор'] if 'Тональный набор' in source_dict else '',
				'IP_PROP3063' : source_dict['Основные характеристики']['Управление'] if 'Управление' in source_dict else '',
				'IP_PROP3064' : source_dict['Основные характеристики']['Управление через bluetooth'] if 'Управление через bluetooth' in source_dict else '',
				'IP_PROP3065' : source_dict['Основные характеристики']['Управление через аудио линейный порт телефона'] if 'Управление через аудио линейный порт телефона' in source_dict else '',
				'IP_PROP3066' : source_dict['Основные характеристики']['Формат записи'] if 'Формат записи' in source_dict else '',
				'IP_PROP3067' : source_dict['Основные характеристики']['Число USB портов'] if 'Число USB портов' in source_dict else '',
				'IP_PROP3068' : source_dict['Основные характеристики']['Чувствительность наушников, дБ/В'] if 'Чувствительность наушников, дБ/В' in source_dict else '',
				'IP_PROP3069' : source_dict['Основные характеристики']['Чувствительность, дБ'] if 'Чувствительность, дБ' in source_dict else '',
				'IP_PROP3070' : source_dict['Основные характеристики']['Штекер'] if 'Штекер' in source_dict else '',
				'IP_PROP3071' : source_dict['Основные характеристики']['я удален'] if 'я удален' in source_dict else '',
				'IP_PROP3072' : source_dict['Память']['Встроенная память, Гб'] if 'Встроенная память, Гб' in source_dict else '',
				'IP_PROP3073' : source_dict['Память']['Максимальная емкость карты памяти, Гб'] if 'Максимальная емкость карты памяти, Гб' in source_dict else '',
				'IP_PROP3074' : source_dict['Память']['Объем оперативной памяти, Гб'] if 'Объем оперативной памяти, Гб' in source_dict else '',
				'IP_PROP3075' : source_dict['Память']['Объем памяти, ГБ'] if 'Объем памяти, ГБ' in source_dict else '',
				'IP_PROP3076' : source_dict['Память']['Тип карты памяти'] if 'Тип карты памяти' in source_dict else '',
				'IP_PROP3077' : source_dict['Память']['Тип носителя данных'] if 'Тип носителя данных' in source_dict else '',
				'IP_PROP3078' : source_dict['Питание']['Беспроводная зарядка'] if 'Беспроводная зарядка' in source_dict else '',
				'IP_PROP3079' : source_dict['Питание']['Быстрая зарядка'] if 'Быстрая зарядка' in source_dict else '',
				'IP_PROP3080' : source_dict['Питание']['Время в режиме ожидания, ч'] if 'Время в режиме ожидания, ч' in source_dict else '',
				'IP_PROP3081' : source_dict['Питание']['Время в режиме разговора, ч'] if 'Время в режиме разговора, ч' in source_dict else '',
				'IP_PROP3082' : source_dict['Питание']['Время зарядки'] if 'Время зарядки' in source_dict else '',
				'IP_PROP3083' : source_dict['Питание']['Время зарядки аккумулятора, ч'] if 'Время зарядки аккумулятора, ч' in source_dict else '',
				'IP_PROP3084' : source_dict['Питание']['Время работы от аккумулятора, ч'] if 'Время работы от аккумулятора, ч' in source_dict else '',
				'IP_PROP3085' : source_dict['Питание']['Емкость аккумулятора, мАч'] if 'Емкость аккумулятора, мАч' in source_dict else '',
				'IP_PROP3086' : source_dict['Питание']['Питание'] if 'Питание' in source_dict else '',
				'IP_PROP3087' : source_dict['Питание']['Работа от аккумулятора, ч'] if 'Работа от аккумулятора, ч' in source_dict else '',
				'IP_PROP3088' : source_dict['Питание']['Размер аккумулятора'] if 'Размер аккумулятора' in source_dict else '',
				'IP_PROP3089' : source_dict['Питание']['Тип аккумулятора'] if 'Тип аккумулятора' in source_dict else '',
				'IP_PROP3090' : source_dict['Процессор']['Модель процессора'] if 'Модель процессора' in source_dict else '',
				'IP_PROP3091' : source_dict['Процессор']['Процессор, (МГц, количество ядер)'] if 'Процессор, (МГц, количество ядер)' in source_dict else '',
				'IP_PROP3092' : source_dict['Разное']['LBS'] if 'LBS' in source_dict else '',
				'IP_PROP3093' : source_dict['Разное']['Бренд'] if 'Бренд' in source_dict else '',
				'IP_PROP3094' : source_dict['Разное']['Гарантия'] if 'Гарантия' in source_dict else '',
				'IP_PROP3095' : source_dict['Разное']['Длина кабеля'] if 'Длина кабеля' in source_dict else '',
				'IP_PROP3096' : source_dict['Разное']['Для корпуса размером, мм'] if 'Для корпуса размером, мм' in source_dict else '',
				'IP_PROP3097' : source_dict['Разное']['Дополнительно'] if 'Дополнительно' in source_dict else '',
				'IP_PROP3098' : source_dict['Разное']['Индикатор состояния'] if 'Индикатор состояния' in source_dict else '',
				'IP_PROP3099' : source_dict['Разное']['Кнопки управления'] if 'Кнопки управления' in source_dict else '',
				'IP_PROP3100' : source_dict['Разное']['Компас'] if 'Компас' in source_dict else '',
				'IP_PROP3101' : source_dict['Разное']['Комплектация'] if 'Комплектация' in source_dict else '',
				'IP_PROP3102' : source_dict['Разное']['Крепление на ремень'] if 'Крепление на ремень' in source_dict else '',
				'IP_PROP3103' : source_dict['Разное']['Макс. выходное напряжение'] if 'Макс. выходное напряжение' in source_dict else '',
				'IP_PROP3104' : source_dict['Разное']['Материал'] if 'Материал' in source_dict else '',
				'IP_PROP3105' : source_dict['Разное']['Материал ремешка'] if 'Материал ремешка' in source_dict else '',
				'IP_PROP3106' : source_dict['Разное']['Модель'] if 'Модель' in source_dict else '',
				'IP_PROP3107' : source_dict['Разное']['Наличие регулятора громкости'] if 'Наличие регулятора громкости' in source_dict else '',
				'IP_PROP3108' : source_dict['Разное']['Поддержка 5G'] if 'Поддержка 5G' in source_dict else '',
				'IP_PROP3109' : source_dict['Разное']['Поддержка видеозвонков'] if 'Поддержка видеозвонков' in source_dict else '',
				'IP_PROP3110' : source_dict['Разное']['Поддержка голосовой связи'] if 'Поддержка голосовой связи' in source_dict else '',
				'IP_PROP3111' : source_dict['Разное']['Поддержка казахского языка'] if 'Поддержка казахского языка' in source_dict else '',
				'IP_PROP3112' : source_dict['Разное']['Поддержка сервисов Google Play'] if 'Поддержка сервисов Google Play' in source_dict else '',
				'IP_PROP3113' : source_dict['Разное']['Подключение дополнительных трубок'] if 'Подключение дополнительных трубок' in source_dict else '',
				'IP_PROP3114' : source_dict['Разное']['Процессор'] if 'Процессор' in source_dict else '',
				'IP_PROP3115' : source_dict['Разное']['Серия'] if 'Серия' in source_dict else '',
				'IP_PROP3116' : source_dict['Разное']['Страна производитель'] if 'Страна производитель' in source_dict else '',
				'IP_PROP3117' : source_dict['Разное']['Тип батареи'] if 'Тип батареи' in source_dict else '',
				'IP_PROP3118' : source_dict['Разное']['Фонарик'] if 'Фонарик' in source_dict else '',
				'IP_PROP3119' : source_dict['Разное']['Фотокамера'] if 'Фотокамера' in source_dict else '',
				'IP_PROP3120' : source_dict['Разное']['Шумоподавление'] if 'Шумоподавление' in source_dict else '',
				'IP_PROP3121' : source_dict['Разное']['Стандарты сети'] if 'Стандарты сети' in source_dict else '',
				'IP_PROP3122' : source_dict['Стандарт']['Формат мелодии'] if 'Формат мелодии' in source_dict else '',
				'IP_PROP3123' : source_dict['Тип звонка']['ANT+'] if 'ANT+' in source_dict else '',
				'IP_PROP3124' : source_dict['Типы передачи данных']['Bluetooth'] if 'Bluetooth' in source_dict else '',
				'IP_PROP3125' : source_dict['Типы передачи данных']['GPRS'] if 'GPRS' in source_dict else '',
				'IP_PROP3126' : source_dict['Типы передачи данных']['GPS'] if 'GPS' in source_dict else '',
				'IP_PROP3127' : source_dict['Типы передачи данных']['NFC'] if 'NFC' in source_dict else '',
				'IP_PROP3128' : source_dict['Типы передачи данных']['USB'] if 'USB' in source_dict else '',
				'IP_PROP3129' : source_dict['Типы передачи данных']['WAP'] if 'WAP' in source_dict else '',
				'IP_PROP3130' : source_dict['Типы передачи данных']['Wi-Fi'] if 'Wi-Fi' in source_dict else '',
				'IP_PROP3131' : source_dict['Типы передачи данных']['Поддержка 4G (LTE)'] if 'Поддержка 4G (LTE)' in source_dict else '',
				'IP_PROP3132' : source_dict['Фотокамера']['Автофокус'] if 'Автофокус' in source_dict else '',
				'IP_PROP3133' : source_dict['Фотокамера']['Макс. разрешение фотоснимков, Пикс'] if 'Макс. разрешение фотоснимков, Пикс' in source_dict else '',
				'IP_PROP3134' : source_dict['Фотокамера']['Особенности тыловой камеры'] if 'Особенности тыловой камеры' in source_dict else '',
				'IP_PROP3135' : source_dict['Фотокамера']['Особенности фронтальной камеры'] if 'Особенности фронтальной камеры' in source_dict else '',
				'IP_PROP3136' : source_dict['Фотокамера']['Разрешение фотокамеры, Мпикс'] if 'Разрешение фотокамеры, Мпикс' in source_dict else '',
				'IP_PROP3137' : source_dict['Фотокамера']['Режим видеосъемки'] if 'Режим видеосъемки' in source_dict else '',
				'IP_PROP3138' : source_dict['Фотокамера']['Фронтальная камера (для видеозвонков), Мпикс'] if 'Фронтальная камера (для видеозвонков), Мпикс' in source_dict else '',
				'IP_PROP3139' : source_dict['Функции']['Сканер отпечатка пальца'] if 'Сканер отпечатка пальца' in source_dict else '',
				'IP_PROP3140' : source_dict['Функции']['Акселерометр'] if 'Акселерометр' in source_dict else '',
				'IP_PROP3141' : source_dict['Функции']['Барометр'] if 'Барометр' in source_dict else '',
				'IP_PROP3142' : source_dict['Функции']['Блокировка клавиатуры'] if 'Блокировка клавиатуры' in source_dict else '',
				'IP_PROP3143' : source_dict['Функции']['Вибрация'] if 'Вибрация' in source_dict else '',
				'IP_PROP3144' : source_dict['Функции']['Встроенное оборудование и функции'] if 'Встроенное оборудование и функции' in source_dict else '',
				'IP_PROP3145' : source_dict['Функции']['Гироскоп'] if 'Гироскоп' in source_dict else '',
				'IP_PROP3146' : source_dict['Функции']['Голосовой набор'] if 'Голосовой набор' in source_dict else '',
				'IP_PROP3147' : source_dict['Функции']['Датчик освещенности'] if 'Датчик освещенности' in source_dict else '',
				'IP_PROP3148' : source_dict['Функции']['Датчик сердечного ритма'] if 'Датчик сердечного ритма' in source_dict else '',
				'IP_PROP3149' : source_dict['Функции']['Ожидание/удержание вызова'] if 'Ожидание/удержание вызова' in source_dict else '',
				'IP_PROP3150' : source_dict['Функции']['Ответить/закончить разговор'] if 'Ответить/закончить разговор' in source_dict else '',
				'IP_PROP3151' : source_dict['Функции']['Панорамная съемка'] if 'Панорамная съемка' in source_dict else '',
				'IP_PROP3152' : source_dict['Функции']['Повтор последнего номера'] if 'Повтор последнего номера' in source_dict else '',
				'IP_PROP3153' : source_dict['Функции']['Подтверждение окончания передачи'] if 'Подтверждение окончания передачи' in source_dict else '',
				'IP_PROP3154' : source_dict['Функции']['Распознавание лица'] if 'Распознавание лица' in source_dict else '',
				'IP_PROP3155' : source_dict['Функции']['Режим мониторинга/сканирования'] if 'Режим мониторинга/сканирования' in source_dict else '',
				'IP_PROP3156' : source_dict['Функции']['Режимы видеосъемки'] if 'Режимы видеосъемки' in source_dict else '',
				'IP_PROP3157' : source_dict['Функции']['Система стабилизации изображения'] if 'Система стабилизации изображения' in source_dict else '',
				'IP_PROP3158' : source_dict['Цвет, размеры и вес']['Вес без упаковки (нетто), кг'] if 'Вес без упаковки (нетто), кг' in source_dict else '',
				'IP_PROP3159' : source_dict['Цвет, размеры и вес']['Вес в упаковке (брутто), кг'] if 'Вес в упаковке (брутто), кг' in source_dict else '',
				'IP_PROP3160' : source_dict['Цвет, размеры и вес']['Вес трубки, гр'] if 'Вес трубки, гр' in source_dict else '',
				'IP_PROP3161' : source_dict['Цвет, размеры и вес']['Габариты в упаковке (ВхШхГ), см'] if 'Габариты в упаковке (ВхШхГ), см' in source_dict else '',
				'IP_PROP3162' : source_dict['Цвет, размеры и вес']['Габариты устройства (ВхШхГ), см'] if 'Габариты устройства (ВхШхГ), см' in source_dict else '',
				'IP_PROP3163' : source_dict['Цвет, размеры и вес']['Размер базы (ВхШхГ), мм'] if 'Размер базы (ВхШхГ), мм' in source_dict else '',
				'IP_PROP3164' : source_dict['Цвет, размеры и вес']['Размер трубки (ВхШхГ), мм'] if 'Размер трубки (ВхШхГ), мм' in source_dict else '',
				'IP_PROP3165' : source_dict['Цвет, размеры и вес']['Цвет'] if 'Цвет' in source_dict else '',
				'IP_PROP3166' : source_dict['Экран']['Датчик ориентации экрана'] if 'Датчик ориентации экрана' in source_dict else '',
				'IP_PROP3167' : source_dict['Экран']['Диагональ экрана, дюйм'] if 'Диагональ экрана, дюйм' in source_dict else '',
				'IP_PROP3168' : source_dict['Экран']['Количество цветов дисплея'] if 'Количество цветов дисплея' in source_dict else '',
				'IP_PROP3169' : source_dict['Экран']['Контраст'] if 'Контраст' in source_dict else '',
				'IP_PROP3170' : source_dict['Экран']['Разрешение'] if 'Разрешение' in source_dict else '',
				'IP_PROP3171' : source_dict['Экран']['Разрешение дисплея, пикс'] if 'Разрешение дисплея, пикс' in source_dict else '',
				'IP_PROP3172' : source_dict['Экран']['Сенсорный дисплей'] if 'Сенсорный дисплей' in source_dict else '',
				'IP_PROP3173' : source_dict['Экран']['Технология изготовления дисплея'] if 'Технология изготовления дисплея' in source_dict else '',
				'IP_PROP3174' : source_dict['Экран']['Формат'] if 'Формат' in source_dict else '',
				'IP_PROP3175' : source_dict['Экран']['Частота обновления, Гц'] if 'Частота обновления, Гц' in source_dict else '',
				'IC_GROUP0': '', # Группа уровня (1) | 2150
				'IC_GROUP1': '', # Группа уровня (2) | 2160
				'IC_GROUP2': '', # Группа уровня (3) | 2170
				'IC_GROUP3': '', # Группа уровня (4) | 2180
				'IC_GROUP4': '', # Группа уровня (5) | 2190
				'IC_GROUP5': '', # Группа уровня (6) | 2200
				'IC_GROUP6': '', # Группа уровня (7) | 2210
				'IC_GROUP7': '', # Группа уровня (8) | 2220
				'IC_GROUP8': '', # Группа уровня (9) | 2230
				'IC_GROUP9': '', # Группа уровня (10)
			}
			csv_line_list = list(value for value in target_dict.values())
			csv_line = delimiter.join(csv_line_list)
			ft.write(csv_line + '\n')
			# ftx.write(dicttoxml(source_dict))
			# ftx.write(str(dicttoxml(source_dict)))
ft.close()
# ftx.close()