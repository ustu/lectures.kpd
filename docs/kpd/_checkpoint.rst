.. _dz1:

Закрепление материала "Протокол HTTP"
=====================================

Цель работы
-----------

Получить практические навыки по работе с ``HTTP`` протоколом посредством
``Telnet``.

Замечания к выполнению
----------------------

Connection closed by foreign host
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Некоторые веб-сайты расположены на серверах с установленной задержкой
соединения, поэтому при истечении нескольких секунд сервер может принудительно
оборвать соединение.

.. note::

    * `Настройка задержки соединенний в Apache
      <http://httpd.apache.org/docs/2.2/mod/core.html#timeout>`_
    * `Настройка задержки соединенний в Nginx
      <http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_send_timeout>`_

Например:

.. code-block:: bash
    :emphasize-lines: 5

    $ telnet wikipedia.org 80
    Trying 91.198.174.192...
    Connected to wikipedia.org.
    Escape character is '^]'.
    GET Connection closed by foreign host.

Для выполнения лабораторной работы, обойти эту проблему можно сохранив текст
запроса в начале в текстовом редакторе, а затем после установки соединения
скопировать его в консоль.

HTTPS и 400 Bad Request
^^^^^^^^^^^^^^^^^^^^^^^

Многие сайты работают по протоколу `HTTPS`, который подразумевает обмен
сертификатами для шифрования трафика. `Telnet` не умеет это делать в
автоматическом режиме, поэтому если подключиться на порт `443` (HTTPS) при
помощи `Telnet` и попробовать отправить запрос, то наверняка в ответе будет
ошибка `400 Bad Request`.

.. code-block:: bash
    :emphasize-lines: 16

    $ telnet wikipedia.org 443
    Trying 91.198.174.192...
    Connected to wikipedia.org.
    Escape character is '^]'.
    GET /ip HTTP/1.1
    Host: wikipedia.org

    HTTP/1.1 400 Bad Request
    Server: nginx/1.11.13
    Date: Mon, 18 Sep 2017 06:05:45 GMT
    Content-Type: text/html
    Content-Length: 272
    Connection: close

    <html>
    <head><title>400 The plain HTTP request was sent to HTTPS port</title></head>
    <body bgcolor="white">
    <center><h1>400 Bad Request</h1></center>
    <center>The plain HTTP request was sent to HTTPS port</center>
    <hr><center>nginx/1.11.13</center>
    </body>
    </html>
    Connection closed by foreign host.

Отправлять запросы по `HTTPS` можно используя утилиту :ref:`openssl <openssl>`.

Задания
-------

.. _issue1:

Задание 1
^^^^^^^^^

* Создать проект со следующей структурой:

::

   myproject/
   ├── about
   │   └── aboutme.html
   └── index.html

* В файле ``index.html`` написать 2 ссылки с прямым и абсолютным обращением к
  ``aboutme.html``. В файле ``aboutme.html`` создать такие же ссылки на файл
  ``index.html``.

.. _issue2:

Задание 2
^^^^^^^^^

.. note::

   * :ref:`telnet`
   * http://hurl.quickblox.com.

Подключиться по telnet к http://wikipedia.org и отправить запрос:

::

   GET /wiki/страница HTTP/1.1
   Host: ru.wikipedia.org
   User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5
   Accept: text/html
   Connection: close
   (пустая строка)

Проанализировать ответ сервера. Описать работу HTTP протокола в данном случае.

Разрешается выбрать любой другой веб-сайт вместо http://WikiPedia.org

.. _issue3:

Задание 3
^^^^^^^^^

Отправить запросы на http://httpbin.org, проанализировать ответ и код
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

.. _issue4:

Задание 4
^^^^^^^^^

.. note::

   * https://html5book.ru/html5-forms/

* Создать HTML форму c ``action="http://httpbin.org/post"`` ``method="POST"`` и
  ``enctype="multipart/form-data"``
* Добавить в форму поля ``firstname``, ``lastname``, ``group``, ``message``
  (textarea), ``myimg`` (file).
* Проверить результат отправки данных формы.

Проанализировать ответ. Описать работу HTTP протокола в данном случае.

Содержание отчета
-----------------

На каждое задание создать отчет, который должен быть оформлен в виде
репозитария на :l:`GitHub` или заметок на сервисе :l:`Gist`. В отчете должно
быть описание последовательности действий, результат выполнения заданий и
выводы по работе.
