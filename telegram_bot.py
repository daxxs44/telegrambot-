import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# ----- Configuration -----
BOT_TOKEN = "YOUR_NEW_BOT_TOKEN_HERE"  # REPLACE THIS with your NEW token from BotFather
GROUP_CHAT_ID = "YOUR_GROUP_CHAT_ID"  # Replace with your group chat ID (e.g., -1001234567890)
AUTHORIZED_USER_ID = YOUR_USER_ID_HERE  # Replace with your Telegram user ID (numbers only, no quotes)

# ----- Handlers -----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /start is issued."""
    await update.message.reply_text(
        "👋 Hi! Send me an address and I'll forward it to the group for confirmation."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages and forward to group chat."""
    # Only accept messages from authorized user
    if update.effective_user.id != AUTHORIZED_USER_ID:
        await update.message.reply_text("❌ You are not authorized to use this bot.")
        return
    
    # Get the address from the message
    address = update.message.text
    
    # Create confirmation buttons
    keyboard = [
        [
            InlineKeyboardButton("✅ Confirmed", callback_data=f"confirm_{update.effective_user.id}"),
            InlineKeyboardButton("❌ Not Confirmed", callback_data=f"reject_{update.effective_user.id}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send to group chat
    try:
        await context.bot.send_message(
            chat_id=GROUP_CHAT_ID,
            text=f"📍 **New Address:**\n\n{address}\n\n👤 From: {update.effective_user.first_name}",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        await update.message.reply_text("✅ Address sent to the group!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error sending to group: {e}")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks."""
    query = update.callback_query
    await query.answer()
    
    # Parse callback data
    action, user_id = query.data.split("_")
    
    if action == "confirm":
        await query.edit_message_text(
            text=f"{query.message.text}\n\n✅ **CONFIRMED** by {query.from_user.first_name}",
            parse_mode="Markdown"
        )
    elif action == "reject":
        await query.edit_message_text(
            text=f"{query.message.text}\n\n❌ **NOT CONFIRMED** by {query.from_user.first_name}",
            parse_mode="Markdown"
        )

# ----- Main -----
def main():
    """Start the bot."""
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Start the bot
    print("🤖 Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
