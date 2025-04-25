restful_booker_tests/
│
├── conftest.py                 # Фикстуры (token, test data)
├── utils/
│   └── data_generator.py       # Генератор случайных данных (Faker)
│
├── client/
│   └── booking_client.py       # API-клиент с методами CRUD
│
├── models/
│   └── booking_model.py        # Класс Booking для хранения/передачи данных
│
├── tests/
│   └── test_booking.py         # Основные тесты API
│
├── requirements.txt
├── pytest.ini
└── run.sh                      # (по желанию) для запуска всех тестов

Запуск тестов с созданием HTML-отчета:
pytest --html=report.html --self-contained-html