import cherrypy
from peewee import *

db = SqliteDatabase('data_base.db')

# модель для Истории столовой


class Posts(Model):
    id = AutoField()
    Nickname = CharField()
    Text = CharField()
    Likes = IntegerField()


    class Meta:
        database = db  # модель будет использовать базу данных data_dabe.db


db.create_tables([Posts])  # создание таблицы в базе данных


class WebInterface(object):
    @cherrypy.expose
    def index(self):

        canteens = Posts.select()  # получение объектов из базы данных

        # генерация HTML-страницы для отображения истории столовой
        html = '<head><link rel="stylesheet" href="style.css"></head>'
        html += '<body><h1>История публикаций</h1>'
        html += '<table>'
        html += '<tr><th>№</th>' \
                '<th>Имя пользователя</th>' \
                '<th>Текст</th>' \
                '<th>Количество лайков</th>' \
                '<th>Изменить</th></tr>'

        for canteen in canteens:
            html += f'<tr><td>{canteen.id}</td><td>{canteen.Nickname}</td><td>{canteen.Text}</td><td>{canteen.Likes}</td>'
            html += f'<td><a href="/edit_canteen?id={canteen.id}">Изменить</a></td></tr>'

        html += '</table>'

        # форма для добавления записей
        html += '''
            <h2>Добавить запись:</h2>
            <form method="post" action="add_history">
                <input type="text" name="nickname" placeholder="Имя пользователя" required><br>
                <input type="text" name="text" placeholder="Текст" required><br>
                <input type="number" name="likes" placeholder="Количество лайков" required><br>
                <input type="submit" value="Добавить">
            </form>
        '''

        html += '</body>'

        return html

    @cherrypy.expose
    def add_history(self, nickname, text, likes):
        # создание новой истории столовой
        canteen = Posts(Nickname=nickname,
                             Text=text,
                             Likes=likes)

        canteen.save()


        return 'Запись добавлена успешно.'

    @cherrypy.expose
    def edit_canteen(self, id):
        canteen = Posts.get(Posts.id == id)

        html = '<head><link rel="stylesheet" href="style.css"></head>'
        html += '<body>'
        html += f'<h2>Изменение истории публикаций (ID: {canteen.id}):</h2>'
        html += f'<form method="post" action="update_visit?id={canteen.id}">'
        html += f'<input type="text" name="nickname" placeholder="Имя пользователя" value="{canteen.Nickname}" required><br>'
        html += f'<input type="text" name="text" placeholder="Текст" value="{canteen.Text}" required><br>'
        html += f'<input type="number" name="likes" placeholder="Количество лайков" value="{canteen.Likes}" required><br>'
        html += '<input type="submit" value="Обновить">'
        html += '</form>'
        html += '</body>'

        return html

    @cherrypy.expose
    def update_visit(self, id, nickname, text, likes):
        canteen = Posts.get(Posts.id == id)
        canteen.Nickname= nickname
        canteen.Text=text
        canteen.Likes=likes
        canteen.save()

        return f'Запись (ID: {canteen.id}) успешно обновлена!'


# Запуск CherryPy
cherrypy.quickstart(WebInterface())


