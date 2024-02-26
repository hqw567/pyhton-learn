x = 10
try:
    # print(x / 0)
    raise TypeError("Name error")
except NameError:
    print("Variable x is not defined")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as e:
    print(e)
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")
