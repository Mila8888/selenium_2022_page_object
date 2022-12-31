# selenium_2022_page_object
дз по page_object

## Домашнее задание PageObject:

1. Переписать уже имеющиеся тесты в проекта opencart на PageObject паттерн.
2. Добавить автотесты на следующие сценарии:
* Добавление нового товара в разделе администратора.
* Удаление товара из списка в разделе администартора.
* Регистрация нового пользователя в магазине опенкарта.
* Переключение валют из верхнего меню опенкарта.

## Отчёты Allure
1. Настройте логирование внутри PageObject'ов. (черед модуль logging).
2. Добавьте аннотации для шагов и тестов для трансляции в отчёт Allure.
3. Настройте Selenoid, добавьте несколько браузеров и запустите на них тесты.
4. Предусмотрите возможность запуска тестов как на удаленных сервисах так и локально.
5. Предусмотрите снятие скриншота и добавление его в отчёт при падении тестов.
- выполнить тесты через алюр
pytest tests/examples/ --alluredir allure-results/
- собрать алюр отчет
~/Documents/drivers/allure/bin/allure generate allure-results/

## Selenoid
1. Настройте Selenoid, добавьте несколько браузеров и запустите на них тесты.
2. Documentation https://aerokube.com/selenoid/latest/
3. Browser images https://aerokube.com/images/latest/
4. https://github.com/aerokube/cm
- ./cm selenoid (start, stop, status)
- директория .aerokube
- Урлы: /status /ping
- Для executor {HOST}:4444/wd/hub
- Добавялем selenoid-ui {HOST}:8080
- ./cm selenoid-ui start
- Записываем видео “enableVideo”: True 
- Сохраняем логи сессий “enableLog”: True
- Включаем vnc через “enableVnc”: True (MANUAL)
- Добавляем браузер
- docker pull {BROWSER CONTAINER}
- добавляем браузер в конфиг
- https://aerokube.com/selenoid/latest/#_updating_browsers
- Добавляем нод ./cm selenoid start --args "-limit=10"
