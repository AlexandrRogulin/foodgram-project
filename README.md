## [Foodgram](http://84.201.176.153/?page=1&tag=Завтрак&tag=Обед&tag=Ужин)
Представляю вашему вниманию продуктовый помощник Foodgram. Это онлайн-сервис, где пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

<a target="_blank" href="https://radikal.ru"><img src="https://d.radikal.ru/d31/2104/9f/03eddc263227.gif" /></a>


Посмотреть его можно [тут](http://84.201.176.153/?page=1&tag=Завтрак&tag=Обед&tag=Ужин)

## Установка

### С помощью [Docker](https://docs.docker.com/engine/install/) и [docker-compose](https://docs.docker.com/compose/install/)
    
Как устаноивть эти инструменты к себе на компьютер можно будет посмотреть перейдя по ссылкам, указанным выше.


1. Создайте в главной дирректории проекта файл **.env** Данные для него можно взять из файла env_example

2. Создайте и запустите виртуальное окружение, а в терминале выполните следующую команду

    ```
    docker-compose up -d --build
    ```
3. После того, как будут запущены контейнеры, вы увидете в терминале похожие записи:
    ```
   	Starting foodgram_db_1 … done
	Recreating foodgram_web_1 … done
	Creating foodgram_nginx_1 … done
   ```
4. Остается выполнить миграции, создать суперюзера, статику и залить базу ингредиентов
    ```
   	docker-compose exec web python manage.py migrate --noinput
	docker-compose exec web python manage.py createsuperuser
	docker-compose exec web python manage.py collectstatic --no-input
	docker-compose exec web python manage.py load_data

   ```
5. Готово! Проверить работу сайта можно будет по этому адресу: [http://127.0.0.1/](http://127.0.0.1/)
    



### Если вариант с Docker и PostgreSQL, вас не устраивает, то можно запустить проект локально:

Для этого следует расскоментировать в файле settings.py слудующие строки:
    
    
    	DATABASES = {
    		'default': {
        		'ENGINE': 'django.db.backends.sqlite3',
        		'NAME': BASE_DIR / 'db.sqlite3',
    		}
		}

А строки:
    
    
    	DATABASES = {
    		'default': {
        		'ENGINE': os.getenv('DB_ENGINE'),
        		'NAME': os.getenv('DB_NAME'),
        		'USER': os.getenv('DB_USER'),
        		'PASSWORD': os.getenv('DB_PASSWORD'),
        		'HOST': os.getenv('DB_HOST'),
        		'PORT': os.getenv('DB_PORT'),
 			}
		} 

Наоборот, закомментируем.
Плюс надо указать **SECRET_KEY** в settings.py. Сгенерировать его можно [на этом сайте](https://djecrety.ir/)

Дальше, все просто. Выполняем последовательно команды в терминале.

1. Предварительная миграция

    ```
    python manage.py migrate
    ```
2. Импорт ингредиентов и тегов для заполнения БД

    ```
    python manage.py load_data
    ```
3. Создание суперпользователя
    ```
   python manage.py createsuperuser
   ```
4. Сбор статики
    ```
   python manage.py collectstatic
   ```
5. Запуск сервера
    ```
   python manage.py runserver
   ```


## Создано с помощью
* [Python](https://www.python.org/)
* [Django](https://docs.djangoproject.com/en/3.1/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [JavaScript](https://www.javascript.com/)
* [Docker](https://www.docker.com/)
* [Docker-compose](https://docs.docker.com/compose/)
* [Postgresql](https://www.postgresql.org/)
