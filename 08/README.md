# Homework 8
[Описание](https://github.com/mailcourses/hse_algorithms_and_data_structures_spring_2024/blob/main/lesson-12/homework.md)
### Идея
- реализация алгоритма Флойда-Уоршелла

### Содержимое
- `floydwarshall.py` - имплементация алгоритма Флойда-Уоршелла
- `requirements.txt` - зависимости для тестов, содержат модули `numpy` и `scipy`
- `tests.py` - тесты
- `Makefile` - для запуска

### Запуск
- `make` или `make test` - создаёт виртуальное окружение для тестов, подгружает зависимости, запускает тесты
- `make clean` - удаляет `__pycache__`, загруженные модули и созданное виртульное окружение

### Тесты
Тест-кейсы сравнивают решение имплементированного алгоритма с решением, реализованным в библиотеке `scipy`:
- неориентированный граф с положительными рёбрами
- ориентированный граф с положительными рёбрами
- ориентированный граф с некоторыми отрицательными рёбрами