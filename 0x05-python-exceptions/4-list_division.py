#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listdiv = []
    for i in range(list_length):
        try:
            listdiv.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            listdiv.append(0)
        except ZeroDivisionError:
            print("division by 0")
            listdiv.append(0)
        except IndexError:
            print("out of range")
            listdiv.append(0)
        finally:
            pass
    return listdiv
