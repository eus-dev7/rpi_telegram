# Raspberry PI telegram boot

## Configuracion telegram
Telegram tiene un bot para crear bots llamado BotFather, buscar en Telegram y pulsar sobre éste para iniciar una conversación.
Iniciar BotFather con 
```
    /start
```
Crear un bot en BotFather enviando el mensaje: 
```
    /newbot
```
A continuación BotFather preguntará:
* El nombre visible del bot: 
```
    nombre_visible
```
* El nombre público del bot, éste tiene que terminar en bot o _bot, como pasa con los dominios es posible que el nombre ya esté registrado: 
```
    nombre_publico_bot
```
Si todo ha salido bien devolverá un token que usaremos para interactuar con nuestro bot, por ejemplo:
```
    392034817:AAHVGuFiL2z3uX9M5e9hc9OXXI-SUbS0GUc (token de ejemplo)
```
## Configuraciones Raspberry PI
Instalar paquetes python en la Raspberry "Python Package Index":
```ssh
    sudo apt-get install python-pip
```
Instalar paquetes "telepot" en la Raspberry:
```ssh
    sudo pip install telepot
```
Ejecutar telegram_bot.py:
```ssh
    python telegram_bot.py
```
## Telegram iniciamos bot
Iniciamos bot en telegram: nombre_visible
```
    /start
```
Enviamos desde telegram  ```On``` y ```Off``` para encender y apagar led
