from src.decorators import log


# Тестирование успешного вызова функции с логированием в файл
def test_successful_logging(tmp_path):
    # Создаем файл для логов
    log_file = tmp_path / "test_log.txt"

    # Оборачиваем функцию add декоратором log, чтобы он писал лог в файл
    @log(filename=str(log_file))
    def add(x, y):
        return x + y

    result = add(3, 4)
    # Проверяем, что функция вернула правильный результат
    assert result == 7

    # Читаем содержимое файла с логами
    content = log_file.read_text()

    # Проверяем, что в логе есть слова "start" и "ok"
    assert "start" in content
    assert "ok" in content


# Тестирование функции без файла (вывод в консоль)
def test_logging_to_console(capsys):
    @log()
    def multiply(x, y):
        print("Inside function")
        return x * y

    result = multiply(2, 5)
    assert result == 10

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "multiply start" in captured.out or "start" in captured.out
    assert "multiply ok" in captured.out


# Тестирование обработки исключения внутри функции
def test_exception_logging(tmp_path):
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def fail_func():
        raise ValueError

    try:
        fail_func()
    except ValueError:
        pass  # Исключение ожидаемо

    # Проверяем содержимое файла на наличие информации об ошибке
    content = log_file.read_text(encoding='utf-8')
    assert 'fail_func error: ValueError' in content
