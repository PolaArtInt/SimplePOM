## Авторизация::standard_user  
Авторизация используя корректные данные  
#### Test:  
test_login.py::  
test_auth_positive  
#### Предусловие:  
Открыть url: https://www.saucedemo.com/v1    
#### Шаги:  
1. Ввести 'standard_user' в 'Username'  
2. Ввести 'secret_sauce' в 'Password'  
3. Кликнуть 'Login'  
#### Ожидаемый результат:  
Переход на новый url:  
https://www.saucedemo.com/inventory.html  
Заголовок страницы: 'Products'  
#### Постусловие: -  

----------------------------------------------------------------

## Авторизация::wrong_login  
Авторизация используя некорректные данные  
#### Test:  
test_login.py::  
test_auth_negative_wrong_login  
#### Предусловие:  
Открыть url: https://www.saucedemo.com/v1  
#### Шаги:  
1. Ввести 'user' в 'Username'  
2. Ввести 'user' в 'Password'  
3. Кликнуть 'Login'  
#### Ожидаемый результат:  
Появление сообщения об ошибке:  
'Epic sadface: Username and password do not match any user in this service'  
Нахождение на том же url: https://www.saucedemo.com/  
#### Постусловие: -  

----------------------------------------------------------------
