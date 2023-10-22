# Евгения Плосконосова, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data


# Функция для получения трека при создании нового заказа
def get_new_order_track():
    # В переменную new_order_track сохраняется результат запроса на создание нового заказа
    new_order_track = sender_stand_request.post_new_order(data.order_body)
    # Возвращается созданный трек
    return new_order_track.json()["track"]


def test_get_order():
    # В переменную track сохраняется обновлённое тело запроса созданного заказа
    track = get_new_order_track()
    # В переменную act сохраняется результат запроса на получение заказа по треку и статус код
    act = sender_stand_request.get_order(track).status_code
    # Ожидаемый статус код
    exp = 200
    assert act == 200
