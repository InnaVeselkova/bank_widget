def log(filename=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                # Логируем начало выполнения
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"Функция {func.__name__} start\n")
                else:
                    print(f"Функция {func.__name__} start")

                res = func(*args, **kwargs)

                # Логируем успешное завершение
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")

                return res

            except Exception as e:
                error_type = type(e).__name__
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"Функция {func.__name__} error: {error_type}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"Функция {func.__name__} error: {error_type}. Inputs: {args}, {kwargs}")
                raise

        return inner
    return wrapper


if __name__ == '__main__':  # pragma: no cover
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y


    my_function(1, 2)
