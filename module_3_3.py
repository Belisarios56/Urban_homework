def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
#print_params() # Работет
#print_params(a, b) #Не работет
#print_params(b = 25) print_params(c = [1,2,3]) #Проверьте, работают ли вызовы - не работает
#print_params(b = 25), print_params(c = [1,2,3]) #Проверьте, работают ли вызовы - работает

values_list = [1805, True, 'Привет']
values_dict = {'a' : 6, 'b' : 18, 'c' : 99}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
