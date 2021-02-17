def get_absolute_url(url, *args, **kwargs):
    """Формирование полного url адреса из переданного домена и параметров
    :param url: домен
    :param args: произвольное количество позиционных аргументов
    :param kwargs: произвольное количество именованных аргументов"""

    #добовляем '/' +  позиционные элементы и по окончанию всех элементов '?'
    for i in args:
        url += '/' + i  
    url += '?'

    #добавляем именованные аргументы + '&' и отсекаем последний символ
    for k,v in kwargs.items():
        url += k + '=' + v + '&'
    url = url[0:-1]
    
    return (url)



print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))