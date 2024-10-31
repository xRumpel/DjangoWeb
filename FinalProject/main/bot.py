import telebot

# Инициализация бота с использованием вашего токена
TOKEN = 'Token'
bot = telebot.TeleBot(TOKEN)

# Фиксированный chat_id для отправки сообщений
CHAT_ID = 'CHAT_ID'


def send_order_notification(order_data):
    message = (
        f"Новый заказ!\n"
        f"ID заказа: {order_data['order_id']}\n"
        f"Имя клиента: {order_data['customer_name']}\n"
        f"Общая стоимость: {order_data['total_price']} руб.\n"
    )
    bot.send_message(CHAT_ID, message)