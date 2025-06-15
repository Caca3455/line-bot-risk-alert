# scheduler.py
from main import send_line_message
from content.daily_message import generate_daily_message

if __name__ == '__main__':
    message = generate_daily_message()
    result = send_line_message(message)
    print("訊息已發送，狀態碼:", result)
