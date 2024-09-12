# EffectiveMobile

 Этот репозиторий является тестовым заданием для компании EffectiveMobile

## Шаги по установке:

1. **Клонирование репозитория**
    ```bash
    git clone https://github.com/qwonfery/EffectiveMobile.git
    cd EffectiveMobile
    ```

2. **Создание и активация виртуального окружения (рекомендуется)**

    На Windows:
    ```bash
    python -m venv venv
    venv\\Scripts\\activate
    ```

    На macOS и Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Установка зависимостей**

    Выполните команду для установки всех необходимых зависимостей:
    ```bash
    pip install -r requirements.txt
    ```

4. **Настройка переменных окружения**

    Добавьте в файл `.env` все необходимые переменные окружения. Пример заполнения есть в самом файле `.env`

## Запуск тестов

Для запуска тестов используйте следующие команды:

1. **e2e тесты** :
    ```bash
    py -m unittest e2e_test
    ```

2. **API тесты**:
    ```bash
    py -m unittest test_api
    ```
