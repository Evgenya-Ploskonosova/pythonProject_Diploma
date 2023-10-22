import configuration
import requests


# POST Запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body)  # подставляем тело


# GET Запрос на получение заказа по его номеру
def get_order(new_order_track):
    # В переменную order_track_url подставляем эндпоинт и новый трек заказа
    order_track_url = configuration.RECEIVING_ORDER + "?t=" + str(new_order_track)
    return requests.get(configuration.URL_SERVICE + order_track_url)  # подставляем полный url
