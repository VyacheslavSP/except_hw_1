def except_zerro_div(a,b):
    return a/b
def except_value_error(string):
    return int(string)
def except_type_error():
    raise TypeError
try:
    except_zerro_div(5,0)
    except_value_error('string')
    except_type_error()
except (ZeroDivisionError):
    print("ошибка деления на 0")
except (ValueError):
    print("ошибка невалидное значение")
except Exception as e:
    if type(e)==TypeError:
        print("ошибка типа")