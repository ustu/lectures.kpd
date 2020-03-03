.. _dz4:

Работа с протоколом WebSocket
=============================

Цель работы
-----------

Получить практические навыки по работе с протоколом ``WebSocket``.

Замечания к выполнению
----------------------

.. seealso::

    * https://www.websocket.org/echo.html
    * https://docs.aiohttp.org/en/stable/index.html

Пример ``WebSocket`` echo сервера на ``Python``:

.. code-block:: python
    :linenos:

    import aiohttp
    from aiohttp import web


    async def hello(request):
        return web.Response(text="Hello, world")


    async def websocket_handler(request):

        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == "close":
                    await ws.close()
                else:
                    await ws.send_str(msg.data + "/answer")
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print("ws connection closed with exception %s" % ws.exception())

        print("websocket connection closed")

        return ws


    app = web.Application()
    app.add_routes([web.get("/", hello)])
    app.add_routes([web.get("/ws", websocket_handler)])
    web.run_app(app)

Пример ``AJAX`` запроса:

.. code-block:: js
    :linenos:

    function get(url, callback, timeout=5 * 1000) {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", url, true);
      xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
      xhr.timeout = timeout;
      xhr.ontimeout = () => {
        console.error("Timed out " + timeout + " " + url);
      };
      xhr.onerror = (e) => {
        console.error(
            "Error "
            + e.target.status
            + " occurred while receiving the document."
        );
      };
      xhr.onreadystatechange = () => {
        if (xhr.readyState === 4
          && (xhr.status   === 200
            || (xhr.status === 0 && xhr.responseText))) {
          try {
            callback(JSON.parse(xhr.responseText));
          } catch(e) {
            callback(xhr.responseText);
          }
        } else {

        }
      };
      xhr.send();
    };

Задания
-------

.. _ws_issue1:

Задание 1
^^^^^^^^^

.. seealso::

    https://docs.aiohttp.org/en/stable/index.html

Написать ``WebSocket`` сервер на языке ``Python`` с использованием библиотеки
``aiohttp``. Сервер должен уметь отдавать файлы по ``HTTP`` запросу:

* http://127.0.0.1:8080/myfile1.txt
* http://127.0.0.1:8080/myserver.py
* http://127.0.0.1:8080/README.rst

На этом же порту иметь возможность получить файлы по адресу
``http://127.0.0.1:8080/ws`` при помощи протокола ``WebSocket``.


.. _ws_issue2:

Задание 2
^^^^^^^^^

.. seealso::

    * `WebSocket <https://developer.mozilla.org/ru/docs/WebSockets/Writing_WebSocket_client_applications>`_
    * `AJAX <https://developer.mozilla.org/ru/docs/Web/Guide/AJAX/%D0%A1_%D1%87%D0%B5%D0%B3%D0%BE_%D0%BD%D0%B0%D1%87%D0%B0%D1%82%D1%8C>`_
    * `JavaScript <https://developer.mozilla.org/ru/docs/Web/JavaScript>`_

Создать проект со следующей структурой:

::

   myproject/
   └── index.html

* В файле ``index.html`` добавить ``javascript`` код для получения содержимого
  файлов с нашего сервер при помощи ``AJAX`` и протокола ``WebSocket``.

.. _ws_issue3:

Задание 3
^^^^^^^^^

Добавить в ``index.html`` форму для отправки запросов на получения содержимого
файлов.

Содержание отчета
-----------------

На каждое задание создать отчет, который должен быть оформлен в виде
репозитария на :l:`GitHub` или заметок на сервисе :l:`Gist`. В отчете должно
быть описание последовательности действий, результат выполнения заданий и
выводы по работе.
