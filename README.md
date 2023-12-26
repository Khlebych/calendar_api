## запуск приложения

```
./venv/bin/flask --app ./api-calendar/calendar/api.py run
```


## cURL тестирование

### добавление новой заметки
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "yyyy-mm-dd|title|text"
```

### получение всего списка заметок
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### обновление текста заметки по идентификатору / ID == 1 /  новый текст == "new text"
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "yyyy-mm-dd|title|new text"
```

### удаление заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "yyyy-mm-dd|title_1|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|yyyy-mm-dd|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|yyyy-mm-dd|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "yyyy-mm-dd|title_2|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|yyyy-mm-dd|title|new text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "yyyy-mm-dd|title_1|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: text lenght > MAX: 200

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "yyyy-mm-dd|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 30

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/calendar/
-- пусто --
```