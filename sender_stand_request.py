import configuration
import requests
import data

#Создание заказа

def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body,
                         headers=data.headers)

# Функция получения заказа по треку заказа
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK + '?t=' + str(track),
                         headers=data.headers)
response = post_new_orders(data.order_body);
print(response.status_code)
print(response.json())

#Сохраняем номер трека заказа, для использования в тестах

track = response.json()['track']

response = get_order_by_track(track);
print(response.status_code)
print(response.json())
