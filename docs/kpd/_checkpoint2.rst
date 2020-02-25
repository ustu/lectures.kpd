.. _dz2:

Работа с протоколом HTTPS через openssl
=======================================

Цель работы
-----------

Получить практические навыки по работе с ``HTTPS`` протоколом посредством
``openssl``. Научиться создавать сертификаты.

Замечания к выполнению
----------------------

.. note::
    * :ref:`openssl <openssl>`
    * `OpenSSL для Windows <https://wiki.openssl.org/index.php/Binaries>`_

Задания
-------

.. _issue1:

Задание 1
^^^^^^^^^


Подключиться по `openssl` к https://wikipedia.org и отправить запрос:

.. code-block:: bash

    $ openssl s_client -connect wikipedia.org:443

::

   GET /wiki/страница HTTP/1.1
   Host: ru.wikipedia.org
   User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5
   Accept: text/html
   Connection: close
   (пустая строка)

Проанализировать ответ сервера. Описать работу HTTP протокола в данном случае.

Разрешается выбрать любой другой веб-сайт вместо https://wikipedia.org

.. _issue2:

Задание 2
^^^^^^^^^

1. Создать ключ шифрования для работы по зашифрованному каналу связи

   .. code-block:: bash

        $ openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

2. Поднять веб сервер работающий по протоколу HTTPS

   .. code-block:: python

        import ssl
        from http.server import HTTPServer, SimpleHTTPRequestHandler

        httpd = HTTPServer(("0.0.0.0", 4443), SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(
            httpd.socket,
            certfile="server.pem",
            keyfile="key.pem",
            server_side=True,
            ssl_version=ssl.PROTOCOL_TLS,
        )
        httpd.serve_forever()

3. Отправить запрос на локальный сервер

   .. code-block:: bash

        $ openssl s_client -connect 127.0.0.1:443

.. 3. Сгенерировать публичный ключ шифрования
..
..    .. note::
..
..     * https://letsencrypt.org/
..     * https://certbot.eff.org/
..

.. _issue3:

Задание 3
^^^^^^^^^

Отправить запросы на https://httpbin.org, проанализировать ответ и код
состояния. Описать работу HTTP протокола в каждом запросе.

.. code-blocK:: text
   :caption: /ip

   GET /ip HTTP/1.1
   Host: httpbin.org
   Accept: */*

.. code-blocK:: text
   :caption: /get

   GET /get?foo=bar&1=2&2/0&error=True HTTP/1.1
   Host: httpbin.org
   Accept: */*

.. code-blocK:: text
   :caption: /post
   :emphasize-lines: 4,7

   POST /post HTTP/1.1
   Host: httpbin.org
   Accept: */*
   Content-Length: вычислить длину контента и втавить сюда число!!!
   Content-Type: application/x-www-form-urlencoded

   foo=bar&1=2&2%2F0=&error=True

.. code-blocK:: text
   :caption: /cookies/set

   GET /cookies/set?country=Ru HTTP/1.1
   Host: httpbin.org
   Accept: */*

.. code-blocK:: text
   :caption: /cookies

   GET /cookies HTTP/1.1
   Host: httpbin.org
   Accept: */*

.. code-blocK:: text
   :caption: /redirect

   GET /redirect/4 HTTP/1.1
   Host: httpbin.org
   Accept: */*

Содержание отчета
-----------------

На каждое задание создать отчет, который должен быть оформлен в виде
репозитария на :l:`GitHub` или заметок на сервисе :l:`Gist`. В отчете должно
быть описание последовательности действий, результат выполнения заданий и
выводы по работе.
