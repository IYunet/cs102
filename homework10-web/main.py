# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument


from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def read_items():
    html_content = """
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>
    <h1>Регистрация</h1>
    <form action="/cgi-bin/read_form.py">
        Введите имя: <input type="text" name="in_name"><br />
        Введите фамилию: <input type="text" name="in_surname"><br />
        <button type="submit">Зарегестрироваться</button>
    </form>
</body
</html>
    """

    return HTMLResponse(content=html_content, status_code=200)
