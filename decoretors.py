def print_result(func_arg):
    def decorated_func(*args):
        print(func_arg.__name__)
        # Если возвращает список - печатать в столбик
        if type(func_arg(*args)) == list:
            for i in func_arg(*args):
                print(i)
        # Если словарь - печатать парами ключ-значение
        elif type(func_arg(*args)) == dict:
            for key, val in func_arg(*args).items():
                print('{} = {}'.format(key, val))
        # Во всех прочих случаях - выводить результат как есть
        else:
            print(func_arg(*args))
    return decorated_func
