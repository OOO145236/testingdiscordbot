# Импортируем библиотеку discord.py
import discord
# Создаем экземпляр класса Client, который представляет бота
client = discord.Client()

# Декоратор, который регистрирует функцию как обработчик события
@client.event
# Функция, которая срабатывает, когда бот подключается к серверу
async def on_ready():
    # Выводим в консоль имя и идентификатор бота
    print(f"Бот {client.user.name} ({client.user.id}) подключен к серверу")

# Декоратор, который регистрирует функцию как обработчик события
@client.event
# Функция, которая срабатывает, когда бот получает сообщение
async def on_message(message):
    # Проверяем, что сообщение не от самого бота
    if message.author != client.user:
        # Проверяем, что сообщение содержит цифру 4
        if "4" in message.content:
            # Отправляем в чат сообщение с реакцией бота
            await message.channel.send("Я вижу, что вы написали 4. Это мое любимое число! 😊")

# Запускаем бота, используя токен, который мы скопировали на портале для разработчиков в Discord
client.run("MTE3NzE4NDkwODcyMTAxNjkyMw.GFahxw.u4VyijwV7MuG--GsycWQDfol-4VEFMqu6Y_g4o
")
