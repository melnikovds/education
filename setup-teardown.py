# Фикстуры с setup и teardown -
# это функции для подготовки тестового окружения перед запуском теста
# и очистки тестового окружения после завершения теста

# во фреймворках типо Pytest они работают через ключевое слово yield - код до него выполняет setup, а после - terdown

import pytest

@pytest.fixture
def db_connection():
    # Setup - подключение к базе данных
    db = connect_to_db()
    print("подключение к БД утсановлено")

    yield db #передача управления в тестовую функцию

    # Teardown - отключение от базы и очистка
    db.close()
    print("соединение с БД закрыто")

def test_data_reading(db_connection):
    assert db_connection.get_status() == "online"

    