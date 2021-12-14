# Tello EDU управление с ПК
1. Tello

Для пользования данной програмой вам нужно подключиться к Wi-Fi дрона Tello EDU

2. SwarmTello


Для пользования программой вам надо подключить дрона Tello EDU к роутеру:

1.Скачать файл ap-tello
2.Зайти в директорию загрузки файла
3.В строке адреса написать "cmd" (без кавычек)
4.Включить дрон и подключиться к нему
5.В командной строке нужно написать "ap-tello.py -s SSID -p PASSWORD" (без кавычек), где "SSID" - название роутера, к которому вы хотите подключить дрона Tello EDU,
a "PASSWORD" - пароль роутера.
6.Подключение Готово но не до конца


Для дальнейших действий вам понадобиться зайти в Панель Управления роутера.


Настройка со стороны роутера


1.Заходим в ПУ Роутера
2.Ищем настройки DHCP (Если надо, то включаем DHCP)
4.Ищем пункт "Назначение IP Вручную" или "Резервирование IP"
5.Далее надо выдать каждому Дрону IP с 192.168.0.120 до 192.168.0.125 (Вы можете менять 0.120 и 0.125 на любые другие но тогда вам нужнр будет изменять програмный код).
6.Готово! Перезагружаем роутер.


Далее вы запускаете программу.Главное, чтобы компьютер и дроны были подключены к одной сети. 
Если дроны перестали мигать и горят фиолетовым или зелёным цветом то все работает как надо и они были переведены в режим принятия команд.

Управление:
'w'-вперёд
'a'-влево
's'-назад
'd'-вправо
'p'-подъем дронa(oв)
'l'-снижение дронa(oв)
'2'-сделать переворот в воздухе вперёд
'3'-сделать переворот в воздухе назад
'4'-сделать переворот в воздухе влево
'5'-сделать переворот в воздухе вправо
'0'-быстрая посадка 
'1'-быстрый взлёт

ТОЛЬКО в Tello:
'z'-проверить заряд батареи

ТОЛЬКО в Swarm Tello:
'r'-вкл. управление 1 дроном
't'-вкл. управление 2 дроном
'y'-вкл. управление 3 дроном
'u'-вкл. управление 4 дроном
'i'-вкл. управление 5 дроном
'['-вкл. управление всеми дронами
']'-выкл. управление всеми дронами

Доп 1. Активирование дрона :
1.Если вы подключили дрон к роутеру то сбросьте его
2.Подключите дрон к телефону и скачайте приложение Tello
3.В приложении внизу в красном окошке будет запрос на активирование серийного кода дрона, нажимаем
4.Дрон активирован


Сброс дрона :
1.Выключите дрон.
2.При включении удерживайте кнопку включения дрона. (~10 сек.)


Известные ошибки


Q:Что делать если нужно подключиться к дрону как обычно?
A:Сбросьте его. Других решений нет. Потом придётся снова подключать к роутеру


P:Дроны не взлетают.
A:Проверьте заряд батареи дронов, а также не перегрелись ли они и подключены ли они.
S:Зарядите аккумулятор или поставьте дрон охлаждаться


P:Некоторые дроны не выполняют команду
A:Возможно это связано из-за расстояния между роутером и дроном
S:Подвиньте роутер поближе к дрону 


Q:Дроны долго "думают"
A:Это связано с тем что дроны сами по себе долго обрабатывают команды.


P:Дроны замигали красным цветом
A:Дрон не активирован
S:Активируй дрон. Инструкция выше

Р:Дрон поключён, но программа не работает(Для Swarm Tello)
A:Есть две возможные проблемы
 1.Возможно дроны или компьютер не подключились к роутеру. 
  2.IP локальный в настройках роутера и коде перепутаны
S:Перечитайте инструкцию!


P: Неизвестная ошибка, дрон плохо летит и т.д. 
S: Сбросьте дрон и через приложение на телефоне проверьте его и обновите(если он не обновлён).