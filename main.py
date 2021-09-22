
from flask import Flask
from flask import request, Response

from jinja2 import Template
# from sqlalchemy.sql import select
# from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy import create_engine, Column, Integer, String, MetaData
# from flask_sqlalchemy import SQLAlchemy

# DB = SQLAlchemy

# class User(DB.Base):
#     __tablename__ = 'user'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     logic = Column(String, nullable=False, unique=True)
#     name = Column(String, nullable=False)
#     age = Column(Integer, nullable=True)


def setup_db() -> None:
    global engine, db_session

    engine = create_engine('sqlite:///foo.db')
    db_session = sessionmaker(engine, expire_on_commit=False)

    Meta.create_all(engine)


def web():
    app = Flask('test')
    # setup_db()
    return app


app = web()

TEMPLATE = '''

<html>
<head>
    <title>Users</title>
    <style>
        .table_row{
            border: blue;
            border-style: dotted;
        }
    </style>
</head>
<body>
    <table>
    {% for user in users -%}
        <tr class="table_row">
         <th class="table_row">{{user.id}}</th> 
         <th class="table_row">{{user.login}}</th>
         <th class="table_row">{{ user.name }}</th>
         <th class="table_row">{{ user.age }}</th>
        </tr>
    {% endfor %}
    </table>
<body>
</html>
'''


@app.route('/')
def index():
    users = [
        {'id': 1, 'login': 'login1', 'name': 'Vova', 'age': 123},
        {'id': 2, 'login': 'login6', 'name': 'Petya', 'age': 23},
        {'id': 3, 'login': 'login5', 'name': 'Marat', 'age': 42},
        {'id': 4, 'login': 'login2', 'name': 'Anya', 'age': 54},
    ]

    tm = Template(TEMPLATE)

    msg = tm.render(users=users)

    import ipdb
    ipdb.set_trace()

    print(dict(request.headers))
    return Response(
        msg,
        headers={
            'set-cookie': 'client_id=554',
        },
    )


@app.route('/ping')
def ping():
    return 'pong'


"""
run:
$ export FLASK_APP=main.py # set Environment Variable = "main.py"
$ python -m flask run

"""