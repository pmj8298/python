import asyncio
# import nest_asyncio #주피터랩용
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()


from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
# nest_asyncio.apply()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start( update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="봇이 가동되었습니다!")

async def handle_message(update , context ):
    user_message = update.message.text.lower()  # Text -> text

    if "선생님" in user_message:
        response = "수업열심히 해봅시다!"
    elif "날씨" in user_message:
        response = "오늘은 추워요~~"
    print(response)

    #응답 메세지 전송
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    await application.initialize() # 초기화 필수

    # 핸들러 추가
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    await application.start()
    print("봇이 실행중 입니다.")

    await application.updater.start_polling()

if __name__=='__main__':
    asyncio.run(main())