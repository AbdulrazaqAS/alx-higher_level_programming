#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by zero")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except Exception as e:
            print(type(e))
        else:
            res.append(ans)
        finally:
            res.append(0)
    return res
