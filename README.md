
## Описание
Скрипт парсит локальный HTML-файл по странице: https://ads.vk.com/cases, находит карточки кейсов и извлекает:
1. Заголовок кейса.
2. Абсолютную ссылку на кейс.
3. Дату публикации (в формате YYYY-MM-DD).

Данные сохраняются в файл `cases_data.json`.

## Установка и запуск

1. **Клонируйте репозиторий** 
2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Запустите файл parser.py:**
   ```bash
   python parser.py
   ```

## Пример вывода в json

    ```json
    [
    {
        "title": "Как привлечь ВКонтакте потенциальных покупателей моторного масла",
        "url": "https://ads.vk.com/cases/privlekaem-potencialnykh-klientov-v-soobshchestvo-vkontakte-kejs-alleya-grupp",
        "date": "2025-11-27"
    },
    {
        "title": "Эмоции, а не футболки: как привлекать 650 заявок в день в сообщения ВКонтакте",
        "url": "https://ads.vk.com/cases/kak-privlekat-650-zayavok-v-den-v-soobshcheniya-vkontakte-kejs-brenda-podarochnykh-futbolok",
        "date": "2025-11-20"
    }
    ]

