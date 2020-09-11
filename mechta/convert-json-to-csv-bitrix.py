import os
import json
import os
from time import sleep
# from json2xml import json2xml
# from dicttoxml import dicttoxml
from datetime import datetime

def findItemByKey(obj, key):
	try:
		if key in obj: return obj[key]
		for k, v in obj.items():
			if isinstance(v,dict):
				item = findItemByKey(v, key)
				if item is not None:
						return item
	except:
		return False

now = datetime.now()
current_time = now.strftime("%y%m%d-%H%M%S")
print("Current Time =", current_time)

delimiter = '^'

source_folder = 'result-200907-092549/'
target_folder = 'csv/'
if not os.path.isdir(target_folder):
	os.mkdir(target_folder)
# target_filename = 'stanki-test' + '-' + current_time + '.csv'
# target_xml_filename = 'stanki-test' + '-' + current_time + '.xml'
target_filename = 'mechta-' + current_time + '.csv'
target_xml_filename = 'stanki-test.xml'
xml_id = 'MECHTAKZ'

files = os.listdir(source_folder)
limit = 10000
# os.remove(target_folder+target_filename)
# os.remove(target_folder+target_xml_filename)

ft = open(target_folder+target_filename, 'w+', encoding='utf-8')
# ftx = open(target_folder+target_xml_filename, 'w+', encoding='utf-8')

for i, filename in enumerate(files):
	if i >= limit: break
	if not os.path.isdir(source_folder+filename):
		print('-------> '+filename+' <-------')
		with open(source_folder+filename, 'r', encoding='utf-8') as fs:
			source_dict = json.load(fs)
			target_dict = {}
			try: 
				target_dict['IE_XML_ID'] =  xml_id + '' + f'{i+1:04d}' 
			except: # Внешний код (B_IBLOCK_ELEMENT.XML_ID) | 10 
				target_dict['IE_XML_ID'] = ''
			try: 
				target_dict['IE_NAME'] =  source_dict['product_name'] or '' 
			except:
				target_dict['IE_NAME'] = ''
			try: 
				target_dict['IE_ACTIVE'] =  'Y'
			except: # Активность (B_IBLOCK_ELEMENT.ACTIVE) | 40
				target_dict['IE_ACTIVE'] = ''
			try: 
				target_dict['IE_PREVIEW_PICTURE'] =  '' 
			except: # Картинка для анонса (B_IBLOCK_ELEMENT.PREVIEW_PICTURE) | 70
				target_dict['IE_PREVIEW_PICTURE'] = ''
			try: 
				target_dict['IE_PREVIEW_TEXT'] =  '' 
			except: # Описание для анонса (B_IBLOCK_ELEMENT.PREVIEW_TEXT) | 80 
				target_dict['IE_PREVIEW_TEXT'] = ''
			try: 
				target_dict['IE_PREVIEW_TEXT_TYPE'] =  '' 
			except: # Тип описания для анонса (B_IBLOCK_ELEMENT.PREVIEW_TEXT_TYPE) | 90 
				target_dict['IE_PREVIEW_TEXT_TYPE'] = ''
			try: 
				target_dict['IE_DETAIL_PICTURE'] =  source_dict['main_image']['url'] or '' 
			except:
				target_dict['IE_DETAIL_PICTURE'] = ''
			try: 
				target_dict['IE_DETAIL_TEXT'] =  source_dict['product_description']['content'] or '' 
			except:
				target_dict['IE_DETAIL_TEXT'] = ''
			try: 
				target_dict['IE_DETAIL_TEXT_TYPE'] =  'html'  
			except: # Тип детального описания (B_IBLOCK_ELEMENT.DETAIL_TEXT_TYPE) | 120 
				target_dict['IE_DETAIL_TEXT_TYPE'] = ''
			try: 
				target_dict['IMAGES'] =  '$'.join([item['url'] for item in source_dict['additional_images']]) or '' 
			except:
				target_dict['IMAGES'] = ''
			try: 
				target_dict['IP_PROP2467'] =  source_dict['Разное']['Бренд']  
			except:
				target_dict['IP_PROP2467'] = ''
			try: 
				target_dict['IP_PROP2473'] =  '$'.join([item['url'] for item in source_dict['additional_images']]) or '' 
			except:
				target_dict['IP_PROP2473'] = ''
			try: 
				target_dict['IP_PROP2483'] =  '' + source_dict['product_price']['full']
			except:
				target_dict['IP_PROP2483'] = ''
			try: 
				target_dict['IP_PROP2484'] =  '' + source_dict['product_price']['discounted']  
			except:
				target_dict['IP_PROP2484'] = ''
			try: 
				target_dict['IP_PROP2485'] =  source_dict['product_params']['Разное']['Бренд']  
			except:
				target_dict['IP_PROP2485'] = ''
			try: 
				target_dict['IP_PROP2864'] =  source_dict['product_params']['Разное']['Страна производитель']  
			except:
				target_dict['IP_PROP2864'] = ''
			try: 
				target_dict['IP_PROP2676'] =  source_dict['product_params']['SIM карта']['SIM-карта']  
			except:
				target_dict['IP_PROP2676'] = ''
			try: 
				target_dict['IP_PROP2341'] =  source_dict['product_params']['Видеокарта']['Графический процессор']  
			except:
				target_dict['IP_PROP2341'] = ''
			try: 
				target_dict['IP_PROP2342'] =  source_dict['product_params']['Звук']['Встроенные динамики']  
			except:
				target_dict['IP_PROP2342'] = ''
			try: 
				target_dict['IP_PROP2700'] =  source_dict['product_params']['Звук']['Встроенный микрофон']  
			except:
				target_dict['IP_PROP2700'] = ''
			try: 
				target_dict['IP_PROP2701'] =  source_dict['product_params']['Звук']['Микрофон']  
			except:
				target_dict['IP_PROP2701'] = ''
			try: 
				target_dict['IP_PROP2702'] =  source_dict['product_params']['Интерфейсы']['HDMI']  
			except:
				target_dict['IP_PROP2702'] = ''
			try: 
				target_dict['IP_PROP2703'] =  source_dict['product_params']['Интерфейсы']['Разъем для наушников']  
			except:
				target_dict['IP_PROP2703'] = ''
			try: 
				target_dict['IP_PROP2704'] =  source_dict['product_params']['Информационные функции']['Индикация']  
			except:
				target_dict['IP_PROP2704'] = ''
			try: 
				target_dict['IP_PROP2705'] =  source_dict['product_params']['Информационные функции']['Индикация уровня заряда']  
			except:
				target_dict['IP_PROP2705'] = ''
			try: 
				target_dict['IP_PROP2706'] =  source_dict['product_params']['Комплектация']['Количество аккумуляторов в трубке']  
			except:
				target_dict['IP_PROP2706'] = ''
			try: 
				target_dict['IP_PROP2707'] =  source_dict['product_params']['Комплектация']['Светочувствительность ISO']  
			except:
				target_dict['IP_PROP2707'] = ''
			try: 
				target_dict['IP_PROP2708'] =  source_dict['product_params']['Корпус']['Количество трубок в комплекте']  
			except:
				target_dict['IP_PROP2708'] = ''
			try: 
				target_dict['IP_PROP2709'] =  source_dict['product_params']['Матрица']['Материал корпуса']  
			except:
				target_dict['IP_PROP2709'] = ''
			try: 
				target_dict['IP_PROP2710'] =  source_dict['product_params']['Матрица']['Тип и размер матрицы']  
			except:
				target_dict['IP_PROP2710'] = ''
			try: 
				target_dict['IP_PROP2711'] =  source_dict['product_params']['Матрица']['Эффект. разрешение, Мпикс']  
			except:
				target_dict['IP_PROP2711'] = ''
			try: 
				target_dict['IP_PROP2712'] =  source_dict['product_params']['Операционная система']['Мобильная ОС']  
			except:
				target_dict['IP_PROP2712'] = ''
			try: 
				target_dict['IP_PROP2713'] =  source_dict['product_params']['Оптика']['Объектив']  
			except:
				target_dict['IP_PROP2713'] = ''
			try: 
				target_dict['IP_PROP2714'] =  source_dict['product_params']['Оптика']['Светосила (F-число)']  
			except:
				target_dict['IP_PROP2714'] = ''
			try: 
				target_dict['IP_PROP2715'] =  source_dict['product_params']['Оптика']['Фокусное расстояние']  
			except:
				target_dict['IP_PROP2715'] = ''
			try: 
				target_dict['IP_PROP2716'] =  source_dict['product_params']['Опции']['Дополнительные опции']  
			except:
				target_dict['IP_PROP2716'] = ''
			try: 
				target_dict['IP_PROP2717'] =  source_dict['product_params']['Основные характеристики']['Ёмкость, мАч']  
			except:
				target_dict['IP_PROP2717'] = ''
			try: 
				target_dict['IP_PROP2718'] =  source_dict['product_params']['Основные характеристики']['Автоответчик']  
			except:
				target_dict['IP_PROP2718'] = ''
			try: 
				target_dict['IP_PROP2719'] =  source_dict['product_params']['Основные характеристики']['Возможность настенной установки']  
			except:
				target_dict['IP_PROP2719'] = ''
			try: 
				target_dict['IP_PROP2720'] =  source_dict['product_params']['Основные характеристики']['Дальность действия в помещении, м']  
			except:
				target_dict['IP_PROP2720'] = ''
			try: 
				target_dict['IP_PROP2721'] =  source_dict['product_params']['Основные характеристики']['Диаметр мембран, мм']  
			except:
				target_dict['IP_PROP2721'] = ''
			try: 
				target_dict['IP_PROP2722'] =  source_dict['product_params']['Основные характеристики']['Диапазон воспроизводимых частот, Гц']  
			except:
				target_dict['IP_PROP2722'] = ''
			try: 
				target_dict['IP_PROP2723'] =  source_dict['product_params']['Основные характеристики']['Диапазон частот, Гц']  
			except:
				target_dict['IP_PROP2723'] = ''
			try: 
				target_dict['IP_PROP2724'] =  source_dict['product_params']['Основные характеристики']['Дисплей']  
			except:
				target_dict['IP_PROP2724'] = ''
			try: 
				target_dict['IP_PROP2725'] =  source_dict['product_params']['Основные характеристики']['Дисплей трубки']  
			except:
				target_dict['IP_PROP2725'] = ''
			try: 
				target_dict['IP_PROP2726'] =  source_dict['product_params']['Основные характеристики']['Длина кабеля, м']  
			except:
				target_dict['IP_PROP2726'] = ''
			try: 
				target_dict['IP_PROP2727'] =  source_dict['product_params']['Основные характеристики']['Для моделей']  
			except:
				target_dict['IP_PROP2727'] = ''
			try: 
				target_dict['IP_PROP2728'] =  source_dict['product_params']['Основные характеристики']['Для телефонов']  
			except:
				target_dict['IP_PROP2728'] = ''
			try: 
				target_dict['IP_PROP2729'] =  source_dict['product_params']['Основные характеристики']['Защита от воды и пыли']  
			except:
				target_dict['IP_PROP2729'] = ''
			try: 
				target_dict['IP_PROP2730'] =  source_dict['product_params']['Основные характеристики']['Индикатор уровня зарядки']  
			except:
				target_dict['IP_PROP2730'] = ''
			try: 
				target_dict['IP_PROP2731'] =  source_dict['product_params']['Основные характеристики']['Количество каналов']  
			except:
				target_dict['IP_PROP2731'] = ''
			try: 
				target_dict['IP_PROP2732'] =  source_dict['product_params']['Основные характеристики']['Количество раций в комплекте']  
			except:
				target_dict['IP_PROP2732'] = ''
			try: 
				target_dict['IP_PROP2733'] =  source_dict['product_params']['Основные характеристики']['Количество сигналов вызова']  
			except:
				target_dict['IP_PROP2733'] = ''
			try: 
				target_dict['IP_PROP2734'] =  source_dict['product_params']['Основные характеристики']['Макс. входное напряжение']  
			except:
				target_dict['IP_PROP2734'] = ''
			try: 
				target_dict['IP_PROP2735'] =  source_dict['product_params']['Основные характеристики']['Максимальная высота, см']  
			except:
				target_dict['IP_PROP2735'] = ''
			try: 
				target_dict['IP_PROP2736'] =  source_dict['product_params']['Основные характеристики']['Максимальная нагрузка, кг']  
			except:
				target_dict['IP_PROP2736'] = ''
			try: 
				target_dict['IP_PROP2737'] =  source_dict['product_params']['Основные характеристики']['Максимальный вес нагрузки, кг']  
			except:
				target_dict['IP_PROP2737'] = ''
			try: 
				target_dict['IP_PROP2738'] =  source_dict['product_params']['Основные характеристики']['Материал сумки/чехла']  
			except:
				target_dict['IP_PROP2738'] = ''
			try: 
				target_dict['IP_PROP2739'] =  source_dict['product_params']['Основные характеристики']['Минимальная высота, см']  
			except:
				target_dict['IP_PROP2739'] = ''
			try: 
				target_dict['IP_PROP2740'] =  source_dict['product_params']['Основные характеристики']['Мощность передатчика, Вт']  
			except:
				target_dict['IP_PROP2740'] = ''
			try: 
				target_dict['IP_PROP2741'] =  source_dict['product_params']['Основные характеристики']['Наличие лицензии']  
			except:
				target_dict['IP_PROP2741'] = ''
			try: 
				target_dict['IP_PROP2742'] =  source_dict['product_params']['Основные характеристики']['Определитель номера']  
			except:
				target_dict['IP_PROP2742'] = ''
			try: 
				target_dict['IP_PROP2743'] =  source_dict['product_params']['Основные характеристики']['Память принятых вызовов']  
			except:
				target_dict['IP_PROP2743'] = ''
			try: 
				target_dict['IP_PROP2744'] =  source_dict['product_params']['Основные характеристики']['Повторный набор номера']  
			except:
				target_dict['IP_PROP2744'] = ''
			try: 
				target_dict['IP_PROP2745'] =  source_dict['product_params']['Основные характеристики']['Рабочая частота, МГц']  
			except:
				target_dict['IP_PROP2745'] = ''
			try: 
				target_dict['IP_PROP2746'] =  source_dict['product_params']['Основные характеристики']['Рабочий диапазон температур, C']  
			except:
				target_dict['IP_PROP2746'] = ''
			try: 
				target_dict['IP_PROP2747'] =  source_dict['product_params']['Основные характеристики']['Радиус действия в помещении, м']  
			except:
				target_dict['IP_PROP2747'] = ''
			try: 
				target_dict['IP_PROP2748'] =  source_dict['product_params']['Основные характеристики']['Радиус действия, км']  
			except:
				target_dict['IP_PROP2748'] = ''
			try: 
				target_dict['IP_PROP2749'] =  source_dict['product_params']['Основные характеристики']['Радиус действия, м']  
			except:
				target_dict['IP_PROP2749'] = ''
			try: 
				target_dict['IP_PROP2750'] =  source_dict['product_params']['Основные характеристики']['Размер ремешка, см']  
			except:
				target_dict['IP_PROP2750'] = ''
			try: 
				target_dict['IP_PROP2751'] =  source_dict['product_params']['Основные характеристики']['Режимы дисплея']  
			except:
				target_dict['IP_PROP2751'] = ''
			try: 
				target_dict['IP_PROP2752'] =  source_dict['product_params']['Основные характеристики']['Ремешок']  
			except:
				target_dict['IP_PROP2752'] = ''
			try: 
				target_dict['IP_PROP2753'] =  source_dict['product_params']['Основные характеристики']['Совместимость']  
			except:
				target_dict['IP_PROP2753'] = ''
			try: 
				target_dict['IP_PROP2754'] =  source_dict['product_params']['Основные характеристики']['Совместимость со смартфономи']  
			except:
				target_dict['IP_PROP2754'] = ''
			try: 
				target_dict['IP_PROP2755'] =  source_dict['product_params']['Основные характеристики']['Спикерфон']  
			except:
				target_dict['IP_PROP2755'] = ''
			try: 
				target_dict['IP_PROP2756'] =  source_dict['product_params']['Основные характеристики']['Текстовый дисплей трубки']  
			except:
				target_dict['IP_PROP2756'] = ''
			try: 
				target_dict['IP_PROP2757'] =  source_dict['product_params']['Основные характеристики']['Телефонная книга']  
			except:
				target_dict['IP_PROP2757'] = ''
			try: 
				target_dict['IP_PROP2758'] =  source_dict['product_params']['Основные характеристики']['Тип кабеля (шнура)']  
			except:
				target_dict['IP_PROP2758'] = ''
			try: 
				target_dict['IP_PROP2759'] =  source_dict['product_params']['Основные характеристики']['Тип наушников']  
			except:
				target_dict['IP_PROP2759'] = ''
			try: 
				target_dict['IP_PROP2760'] =  source_dict['product_params']['Основные характеристики']['Тип подключения']  
			except:
				target_dict['IP_PROP2760'] = ''
			try: 
				target_dict['IP_PROP2761'] =  source_dict['product_params']['Основные характеристики']['Тональный набор']  
			except:
				target_dict['IP_PROP2761'] = ''
			try: 
				target_dict['IP_PROP2762'] =  source_dict['product_params']['Основные характеристики']['Управление']  
			except:
				target_dict['IP_PROP2762'] = ''
			try: 
				target_dict['IP_PROP2763'] =  source_dict['product_params']['Основные характеристики']['Управление через bluetooth']  
			except:
				target_dict['IP_PROP2763'] = ''
			try: 
				target_dict['IP_PROP2764'] =  source_dict['product_params']['Основные характеристики']['Управление через аудио линейный порт телефона']  
			except:
				target_dict['IP_PROP2764'] = ''
			try: 
				target_dict['IP_PROP2765'] =  source_dict['product_params']['Основные характеристики']['Формат записи']  
			except:
				target_dict['IP_PROP2765'] = ''
			try: 
				target_dict['IP_PROP2766'] =  source_dict['product_params']['Основные характеристики']['Число USB портов']  
			except:
				target_dict['IP_PROP2766'] = ''
			try: 
				target_dict['IP_PROP2767'] =  source_dict['product_params']['Основные характеристики']['Чувствительность наушников, дБ/В']  
			except:
				target_dict['IP_PROP2767'] = ''
			try: 
				target_dict['IP_PROP2768'] =  source_dict['product_params']['Основные характеристики']['Чувствительность, дБ']  
			except:
				target_dict['IP_PROP2768'] = ''
			try: 
				target_dict['IP_PROP2769'] =  source_dict['product_params']['Основные характеристики']['Штекер']  
			except:
				target_dict['IP_PROP2769'] = ''
			try: 
				target_dict['IP_PROP2770'] =  source_dict['product_params']['Основные характеристики']['я удален']  
			except:
				target_dict['IP_PROP2770'] = ''
			try: 
				target_dict['IP_PROP2771'] =  source_dict['product_params']['Память']['Встроенная память, Гб']  
			except:
				target_dict['IP_PROP2771'] = ''
			try: 
				target_dict['IP_PROP2772'] =  source_dict['product_params']['Память']['Максимальная емкость карты памяти, Гб']  
			except:
				target_dict['IP_PROP2772'] = ''
			try: 
				target_dict['IP_PROP2773'] =  source_dict['product_params']['Память']['Объем оперативной памяти, Гб']  
			except:
				target_dict['IP_PROP2773'] = ''
			try: 
				target_dict['IP_PROP2774'] =  source_dict['product_params']['Память']['Объем памяти, ГБ']  
			except:
				target_dict['IP_PROP2774'] = ''
			try: 
				target_dict['IP_PROP2775'] =  source_dict['product_params']['Память']['Тип карты памяти']  
			except:
				target_dict['IP_PROP2775'] = ''
			try: 
				target_dict['IP_PROP2776'] =  source_dict['product_params']['Память']['Тип носителя данных']  
			except:
				target_dict['IP_PROP2776'] = ''
			try: 
				target_dict['IP_PROP2777'] =  source_dict['product_params']['Питание']['Беспроводная зарядка']  
			except:
				target_dict['IP_PROP2777'] = ''
			try: 
				target_dict['IP_PROP2778'] =  source_dict['product_params']['Питание']['Быстрая зарядка']  
			except:
				target_dict['IP_PROP2778'] = ''
			try: 
				target_dict['IP_PROP2779'] =  source_dict['product_params']['Питание']['Время в режиме ожидания, ч']  
			except:
				target_dict['IP_PROP2779'] = ''
			try: 
				target_dict['IP_PROP2780'] =  source_dict['product_params']['Питание']['Время в режиме разговора, ч']  
			except:
				target_dict['IP_PROP2780'] = ''
			try: 
				target_dict['IP_PROP2781'] =  source_dict['product_params']['Питание']['Время зарядки']  
			except:
				target_dict['IP_PROP2781'] = ''
			try: 
				target_dict['IP_PROP2782'] =  source_dict['product_params']['Питание']['Время зарядки аккумулятора, ч']  
			except:
				target_dict['IP_PROP2782'] = ''
			try: 
				target_dict['IP_PROP2783'] =  source_dict['product_params']['Питание']['Время работы от аккумулятора, ч']  
			except:
				target_dict['IP_PROP2783'] = ''
			try: 
				target_dict['IP_PROP2784'] =  source_dict['product_params']['Питание']['Емкость аккумулятора, мАч']  
			except:
				target_dict['IP_PROP2784'] = ''
			try: 
				target_dict['IP_PROP2785'] =  source_dict['product_params']['Питание']['Питание']  
			except:
				target_dict['IP_PROP2785'] = ''
			try: 
				target_dict['IP_PROP2786'] =  source_dict['product_params']['Питание']['Работа от аккумулятора, ч']  
			except:
				target_dict['IP_PROP2786'] = ''
			try: 
				target_dict['IP_PROP2787'] =  source_dict['product_params']['Питание']['Размер аккумулятора']  
			except:
				target_dict['IP_PROP2787'] = ''
			try: 
				target_dict['IP_PROP2788'] =  source_dict['product_params']['Питание']['Тип аккумулятора']  
			except:
				target_dict['IP_PROP2788'] = ''
			try: 
				target_dict['IP_PROP2789'] =  source_dict['product_params']['Процессор']['Модель процессора']  
			except:
				target_dict['IP_PROP2789'] = ''
			try: 
				target_dict['IP_PROP2790'] =  source_dict['product_params']['Процессор']['Процессор, (МГц, количество ядер)']  
			except:
				target_dict['IP_PROP2790'] = ''
			try: 
				target_dict['IP_PROP2791'] =  source_dict['product_params']['Разное']['LBS']  
			except:
				target_dict['IP_PROP2791'] = ''
			try: 
				target_dict['IP_PROP2792'] =  source_dict['product_params']['Разное']['Бренд']  
			except:
				target_dict['IP_PROP2792'] = ''
			try: 
				target_dict['IP_PROP2793'] =  source_dict['product_params']['Разное']['Гарантия']  
			except:
				target_dict['IP_PROP2793'] = ''
			try: 
				target_dict['IP_PROP2794'] =  source_dict['product_params']['Разное']['Длина кабеля']  
			except:
				target_dict['IP_PROP2794'] = ''
			try: 
				target_dict['IP_PROP2795'] =  source_dict['product_params']['Разное']['Для корпуса размером, мм']  
			except:
				target_dict['IP_PROP2795'] = ''
			try: 
				target_dict['IP_PROP2796'] =  source_dict['product_params']['Разное']['Дополнительно']  
			except:
				target_dict['IP_PROP2796'] = ''
			try: 
				target_dict['IP_PROP2797'] =  source_dict['product_params']['Разное']['Индикатор состояния']  
			except:
				target_dict['IP_PROP2797'] = ''
			try: 
				target_dict['IP_PROP2798'] =  source_dict['product_params']['Разное']['Кнопки управления']  
			except:
				target_dict['IP_PROP2798'] = ''
			try: 
				target_dict['IP_PROP2799'] =  source_dict['product_params']['Разное']['Компас']  
			except:
				target_dict['IP_PROP2799'] = ''
			try: 
				target_dict['IP_PROP2800'] =  source_dict['product_params']['Разное']['Комплектация']  
			except:
				target_dict['IP_PROP2800'] = ''
			try: 
				target_dict['IP_PROP2801'] =  source_dict['product_params']['Разное']['Крепление на ремень']  
			except:
				target_dict['IP_PROP2801'] = ''
			try: 
				target_dict['IP_PROP2802'] =  source_dict['product_params']['Разное']['Макс. выходное напряжение']  
			except:
				target_dict['IP_PROP2802'] = ''
			try: 
				target_dict['IP_PROP2803'] =  source_dict['product_params']['Разное']['Материал']  
			except:
				target_dict['IP_PROP2803'] = ''
			try: 
				target_dict['IP_PROP2804'] =  source_dict['product_params']['Разное']['Материал ремешка']  
			except:
				target_dict['IP_PROP2804'] = ''
			try: 
				target_dict['IP_PROP2805'] =  source_dict['product_params']['Разное']['Модель']  
			except:
				target_dict['IP_PROP2805'] = ''
			try: 
				target_dict['IP_PROP2806'] =  source_dict['product_params']['Разное']['Наличие регулятора громкости']  
			except:
				target_dict['IP_PROP2806'] = ''
			try: 
				target_dict['IP_PROP2807'] =  source_dict['product_params']['Разное']['Поддержка 5G']  
			except:
				target_dict['IP_PROP2807'] = ''
			try: 
				target_dict['IP_PROP2808'] =  source_dict['product_params']['Разное']['Поддержка видеозвонков']  
			except:
				target_dict['IP_PROP2808'] = ''
			try: 
				target_dict['IP_PROP2809'] =  source_dict['product_params']['Разное']['Поддержка голосовой связи']  
			except:
				target_dict['IP_PROP2809'] = ''
			try: 
				target_dict['IP_PROP2810'] =  source_dict['product_params']['Разное']['Поддержка казахского языка']  
			except:
				target_dict['IP_PROP2810'] = ''
			try: 
				target_dict['IP_PROP2811'] =  source_dict['product_params']['Разное']['Поддержка сервисов Google Play']  
			except:
				target_dict['IP_PROP2811'] = ''
			try: 
				target_dict['IP_PROP2812'] =  source_dict['product_params']['Разное']['Подключение дополнительных трубок']  
			except:
				target_dict['IP_PROP2812'] = ''
			try: 
				target_dict['IP_PROP2813'] =  source_dict['product_params']['Разное']['Процессор']  
			except:
				target_dict['IP_PROP2813'] = ''
			try: 
				target_dict['IP_PROP2814'] =  source_dict['product_params']['Разное']['Серия']  
			except:
				target_dict['IP_PROP2814'] = ''
			try: 
				target_dict['IP_PROP2815'] =  source_dict['product_params']['Разное']['Страна производитель']  
			except:
				target_dict['IP_PROP2815'] = ''
			try: 
				target_dict['IP_PROP2816'] =  source_dict['product_params']['Разное']['Тип батареи']  
			except:
				target_dict['IP_PROP2816'] = ''
			try: 
				target_dict['IP_PROP2817'] =  source_dict['product_params']['Разное']['Фонарик']  
			except:
				target_dict['IP_PROP2817'] = ''
			try: 
				target_dict['IP_PROP2818'] =  source_dict['product_params']['Разное']['Фотокамера']  
			except:
				target_dict['IP_PROP2818'] = ''
			try: 
				target_dict['IP_PROP2819'] =  source_dict['product_params']['Разное']['Шумоподавление']  
			except:
				target_dict['IP_PROP2819'] = ''
			try: 
				target_dict['IP_PROP2820'] =  source_dict['product_params']['Разное']['Стандарты сети']  
			except:
				target_dict['IP_PROP2820'] = ''
			try: 
				target_dict['IP_PROP2821'] =  source_dict['product_params']['Стандарт']['Формат мелодии']  
			except:
				target_dict['IP_PROP2821'] = ''
			try: 
				target_dict['IP_PROP2822'] =  source_dict['product_params']['Тип звонка']['ANT+']  
			except:
				target_dict['IP_PROP2822'] = ''
			try: 
				target_dict['IP_PROP2823'] =  source_dict['product_params']['Типы передачи данных']['Bluetooth']  
			except:
				target_dict['IP_PROP2823'] = ''
			try: 
				target_dict['IP_PROP2824'] =  source_dict['product_params']['Типы передачи данных']['GPRS']  
			except:
				target_dict['IP_PROP2824'] = ''
			try: 
				target_dict['IP_PROP2825'] =  source_dict['product_params']['Типы передачи данных']['GPS']  
			except:
				target_dict['IP_PROP2825'] = ''
			try: 
				target_dict['IP_PROP2826'] =  source_dict['product_params']['Типы передачи данных']['NFC']  
			except:
				target_dict['IP_PROP2826'] = ''
			try: 
				target_dict['IP_PROP2827'] =  source_dict['product_params']['Типы передачи данных']['USB']  
			except:
				target_dict['IP_PROP2827'] = ''
			try: 
				target_dict['IP_PROP2828'] =  source_dict['product_params']['Типы передачи данных']['WAP']  
			except:
				target_dict['IP_PROP2828'] = ''
			try: 
				target_dict['IP_PROP2829'] =  source_dict['product_params']['Типы передачи данных']['Wi-Fi']  
			except:
				target_dict['IP_PROP2829'] = ''
			try: 
				target_dict['IP_PROP2830'] =  source_dict['product_params']['Типы передачи данных']['Поддержка 4G (LTE)']  
			except:
				target_dict['IP_PROP2830'] = ''
			try: 
				target_dict['IP_PROP2831'] =  source_dict['product_params']['Фотокамера']['Автофокус']  
			except:
				target_dict['IP_PROP2831'] = ''
			try: 
				target_dict['IP_PROP2832'] =  source_dict['product_params']['Фотокамера']['Макс. разрешение фотоснимков, Пикс']  
			except:
				target_dict['IP_PROP2832'] = ''
			try: 
				target_dict['IP_PROP2833'] =  source_dict['product_params']['Фотокамера']['Особенности тыловой камеры']  
			except:
				target_dict['IP_PROP2833'] = ''
			try: 
				target_dict['IP_PROP2834'] =  source_dict['product_params']['Фотокамера']['Особенности фронтальной камеры']  
			except:
				target_dict['IP_PROP2834'] = ''
			try: 
				target_dict['IP_PROP2835'] =  source_dict['product_params']['Фотокамера']['Разрешение фотокамеры, Мпикс']  
			except:
				target_dict['IP_PROP2835'] = ''
			try: 
				target_dict['IP_PROP2836'] =  source_dict['product_params']['Фотокамера']['Режим видеосъемки']  
			except:
				target_dict['IP_PROP2836'] = ''
			try: 
				target_dict['IP_PROP2837'] =  source_dict['product_params']['Фотокамера']['Фронтальная камера (для видеозвонков), Мпикс']  
			except:
				target_dict['IP_PROP2837'] = ''
			try: 
				target_dict['IP_PROP2838'] =  source_dict['product_params']['Функции']['Сканер отпечатка пальца']  
			except:
				target_dict['IP_PROP2838'] = ''
			try: 
				target_dict['IP_PROP2839'] =  source_dict['product_params']['Функции']['Акселерометр']  
			except:
				target_dict['IP_PROP2839'] = ''
			try: 
				target_dict['IP_PROP2840'] =  source_dict['product_params']['Функции']['Барометр']  
			except:
				target_dict['IP_PROP2840'] = ''
			try: 
				target_dict['IP_PROP2841'] =  source_dict['product_params']['Функции']['Блокировка клавиатуры']  
			except:
				target_dict['IP_PROP2841'] = ''
			try: 
				target_dict['IP_PROP2842'] =  source_dict['product_params']['Функции']['Вибрация']  
			except:
				target_dict['IP_PROP2842'] = ''
			try: 
				target_dict['IP_PROP2843'] =  source_dict['product_params']['Функции']['Встроенное оборудование и функции']  
			except:
				target_dict['IP_PROP2843'] = ''
			try: 
				target_dict['IP_PROP2844'] =  source_dict['product_params']['Функции']['Гироскоп']  
			except:
				target_dict['IP_PROP2844'] = ''
			try: 
				target_dict['IP_PROP2845'] =  source_dict['product_params']['Функции']['Голосовой набор']  
			except:
				target_dict['IP_PROP2845'] = ''
			try: 
				target_dict['IP_PROP2846'] =  source_dict['product_params']['Функции']['Датчик освещенности']  
			except:
				target_dict['IP_PROP2846'] = ''
			try: 
				target_dict['IP_PROP2847'] =  source_dict['product_params']['Функции']['Датчик сердечного ритма']  
			except:
				target_dict['IP_PROP2847'] = ''
			try: 
				target_dict['IP_PROP2848'] =  source_dict['product_params']['Функции']['Ожидание/удержание вызова']  
			except:
				target_dict['IP_PROP2848'] = ''
			try: 
				target_dict['IP_PROP2849'] =  source_dict['product_params']['Функции']['Ответить/закончить разговор']  
			except:
				target_dict['IP_PROP2849'] = ''
			try: 
				target_dict['IP_PROP2850'] =  source_dict['product_params']['Функции']['Панорамная съемка']  
			except:
				target_dict['IP_PROP2850'] = ''
			try: 
				target_dict['IP_PROP2851'] =  source_dict['product_params']['Функции']['Повтор последнего номера']  
			except:
				target_dict['IP_PROP2851'] = ''
			try: 
				target_dict['IP_PROP2852'] =  source_dict['product_params']['Функции']['Подтверждение окончания передачи']  
			except:
				target_dict['IP_PROP2852'] = ''
			try: 
				target_dict['IP_PROP2853'] =  source_dict['product_params']['Функции']['Распознавание лица']  
			except:
				target_dict['IP_PROP2853'] = ''
			try: 
				target_dict['IP_PROP2854'] =  source_dict['product_params']['Функции']['Режим мониторинга/сканирования']  
			except:
				target_dict['IP_PROP2854'] = ''
			try: 
				target_dict['IP_PROP2855'] =  source_dict['product_params']['Функции']['Режимы видеосъемки']  
			except:
				target_dict['IP_PROP2855'] = ''
			try: 
				target_dict['IP_PROP2856'] =  source_dict['product_params']['Функции']['Система стабилизации изображения']  
			except:
				target_dict['IP_PROP2856'] = ''
			try: 
				target_dict['IP_PROP2857'] =  source_dict['product_params']['Цвет, размеры и вес']['Вес без упаковки (нетто), кг']  
			except:
				target_dict['IP_PROP2857'] = ''
			try: 
				target_dict['IP_PROP2858'] =  source_dict['product_params']['Цвет, размеры и вес']['Вес в упаковке (брутто), кг']  
			except:
				target_dict['IP_PROP2858'] = ''
			try: 
				target_dict['IP_PROP2859'] =  source_dict['product_params']['Цвет, размеры и вес']['Вес трубки, гр']  
			except:
				target_dict['IP_PROP2859'] = ''
			try: 
				target_dict['IP_PROP2860'] =  source_dict['product_params']['Цвет, размеры и вес']['Габариты в упаковке (ВхШхГ), см']  
			except:
				target_dict['IP_PROP2860'] = ''
			try: 
				target_dict['IP_PROP2861'] =  source_dict['product_params']['Цвет, размеры и вес']['Габариты устройства (ВхШхГ), см']  
			except:
				target_dict['IP_PROP2861'] = ''
			try: 
				target_dict['IP_PROP2862'] =  source_dict['product_params']['Цвет, размеры и вес']['Размер базы (ВхШхГ), мм']  
			except:
				target_dict['IP_PROP2862'] = ''
			try: 
				target_dict['IP_PROP2863'] =  source_dict['product_params']['Цвет, размеры и вес']['Размер трубки (ВхШхГ), мм']  
			except:
				target_dict['IP_PROP2863'] = ''
			try: 
				target_dict['IP_PROP3165'] =  source_dict['product_params']['Цвет, размеры и вес']['Цвет']  
			except:
				target_dict['IP_PROP3165'] = ''
			try: 
				target_dict['IC_GROUP0'] =  source_dict['product_category_chain'][0] # Группа уровня (1) | 2150 
			except:
				target_dict['IC_GROUP0'] = ''
			try: 
				target_dict['IC_GROUP1'] =  source_dict['product_category_chain'][1] # Группа уровня (2) | 2160 
			except:
				target_dict['IC_GROUP1'] = ''
			try: 
				target_dict['IC_GROUP2'] =  source_dict['product_category_chain'][2] # Группа уровня (3) | 2170 
			except:
				target_dict['IC_GROUP2'] = ''

			if i == 0:
				csv_line_list = target_dict.keys()
			else:
				csv_line_list = list(value for value in target_dict.values())
			# print(csv_line_list)
			csv_line = delimiter.join(csv_line_list)
			ft.write(csv_line + '\n')
			# ftx.write(dicttoxml(source_dict))
			# ftx.write(str(dicttoxml(source_dict)))
ft.close()
# ftx.close()