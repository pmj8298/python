from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = '77245608318279:AAHGYVXEDLbGdRduaJxMrfGSX7lvwuh9QRw'

TRIGGER_WORDS = {
    '안녕':'안녕하세요! 반가워용😊',
    '정보':'어떤 정보가 필요하세요?🤔',
    '기분':'오늘 기분이 좋아요😍'
}

async def start(update, context):
    await update.message.reply_text('안녕! 무엇을 도와드릴까요?')
async def monitor_chat(update, context):
    user_text = update.message.text # 감지된 메시지들 ex.택배물건
    chat_id = update.message.chat_id # 메시지가 온 채팅방  ex. 택배 배송지

    for key, res in TRIGGER_WORDS.items():
        if key in user_text:
            await context.bot.send_message(chat_id = chat_id, text = res)
            break #한개의 키워드에만 반응

def main():
    app = Application.builder().token(TOKEN).build()

    # 명령어 핸들러 추가
    app.add_handler(CommandHandler('start',start))

    # 응답 핸들러 추가
    # ~은 TEXT는 하되, COMMAND는 하지마라
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))

    print('봇이 실행중입니다. 모니터링 중...')
    app.run_polling()




if __name__=='__main__':
   main()