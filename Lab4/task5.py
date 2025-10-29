def order():
    string_space = "Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz"
    string = string_space.replace(" ", "")
    in_set = set(string)

    order_list = list(in_set)
    order_list.sort()

    print("Результат:")
    print(order_list)
order()
