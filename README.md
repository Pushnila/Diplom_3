# UI-тесты Stellar Burgers

Автоматизированные UI-тесты учебного приложения Stellar Burgers.

## Проверки
- переход по клику на «Конструктор»;
- переход по клику на «Лента Заказов»;
- открытие и закрытие окна деталей ингредиента;
- увеличение счётчика ингредиента после добавления в заказ;
- увеличение счётчиков выполненных заказов;
- отображение номера нового заказа в разделе «В работе».

## Запуск в Chrome
python -m pytest -v --browser chrome --alluredir=allure_results --clean-alluredir

## Запуск в Firefox
python -m pytest -v --browser firefox --alluredir=allure_results --clean-alluredir

## Allure-отчёт
allure serve allure_results
