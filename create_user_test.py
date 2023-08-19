# Алена Урасова, 7 когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# Тест проверки, что код ответа равен 200.
def test_status_code_200():
   assert sender_stand_request.response.status_code == 200