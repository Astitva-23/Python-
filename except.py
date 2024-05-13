def divide_number():
    try:
        n1 = 5
        n2 = 8
        res = n1/n2
        print("The result : ", res)
    except ValueError:
        print("Not Valid")
    except ZeroDivisionError:
        print("Not devide by 0")
    except Exception as e:
        print("unexpected error")
    finally:
        print("program executed")
divide_number()