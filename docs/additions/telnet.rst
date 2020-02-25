.. _telnet_install:

.. meta::
   :description: Установка Telnet на Windows, MacOS
   :keywords: HTTP, протокол, telnet, Windows, MacOS, MSYS2, WSL

Telnet
======

Установка на Windows
--------------------

Служба Telnet
^^^^^^^^^^^^^

По умолчанию в Window выше XP не активирован клиент `Telnet`.
Активация производится в разделе "Включение/Отключение компонентов".

.. figure:: /_static/additions/telnet_windows_1.png

    Поиск раздела "Включение/Отключение компонентов"


.. figure:: /_static/additions/telnet_windows_2.png

    Включение компонента `Telnet`

После этих манипуляций в консоле (`cmd.exe`) появится команда ``telnet``.
Команда ``telnet`` от ``Microsoft`` имеет свою специфику.

Пример работы:

.. code-block:: bash

    $ telnet httpbin.org 80

После установки соединения появится пустой (черный) экран.
Можно вводить текст для отправки, но он не будет виден. Чтобы это исправить
необходимо задать опцию ``localecho``. Делается это следующим образом, вначале
выходим в командный режим при помощи сочетания клавиш :kbd:`Ctrl` + :kbd:`]`
(:kbd:`Ctrl` + :kbd:`ъ`). Затем вводим команду ``set localecho``.


.. figure:: /_static/additions/telnet_windows_3.png
    :width: 100%

    Включение опции localecho

После нажатия :kbd:`Enter` установится режим передачи.

.. figure:: /_static/additions/telnet_windows_4.png
    :width: 100%

    HTTP запрос к сайту httpbin.org в cmd.exe

MSYS2
^^^^^

`MSYS2 <http://www.msys2.org/>`_ это окружение `Unix` для `Windows`, после его
установки команда `Telnet` станет сразу доступна в `MSYS2` терминале.

.. code-block:: bash

    user@DESKTOP-9JPISDO MSYS ~
    $ telnet.exe httpbin.org 80
    Trying 50.16.228.34...
    Connected to httpbin.org.
    Escape character is '^]'.
    GET /cookies HTTP/1.1
    Host: httpbin.org

    HTTP/1.1 200 OK
    Connection: keep-alive
    Server: meinheld/0.6.1
    Date: Mon, 18 Sep 2017 08:02:00 GMT
    Content-Type: application/json
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Credentials: true
    X-Powered-By: Flask
    X-Processed-Time: 0.000805139541626
    Content-Length: 20
    Via: 1.1 vegur

    {
      "cookies": {}
    }

Windows Subsystem for Linux (WSL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

    Работает только в Windows 10 с 64х разрядной архитектурой.

После установки https://msdn.microsoft.com/en-us/commandline/wsl/install_guide
команда `Telnet` так же будет доступна в терминале.

Установка на MacOS
------------------

1. Необходимо установить пакетный менеджер `Homebrew <https://brew.sh/index_ru>`_

   .. code-block:: bash

        $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

2. При помощи пакетного менеджера установить `Telnet`:

   .. code-block:: bash

        $ brew install telnet

3. После этого команда ``telnet`` появится в терминале
