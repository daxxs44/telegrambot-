# Telegram Bot Setup Instructions

## ⚠️ IMPORTANT - FIRST STEPS:
1. Go to @BotFather on Telegram
2. Send `/mybots`
3. Select your bot
4. Click "API Token" → "Revoke current token"
5. Copy your NEW token (your old one was exposed publicly!)

## 🔧 Configuration Steps:

### Step 1: Get Your User ID
1. Message @userinfobot on Telegram
2. It will reply with your User ID (a number like 123456789)
3. Copy this number

### Step 2: Get Your Group Chat ID
Option A - Easy way:
1. Add @RawDataBot to your group
2. It will send a message with the chat ID
3. Look for "chat":{"id":-1001234567890}
4. Copy the number (including the minus sign!)
5. Remove the bot after

Option B - Manual way:
1. Add your bot to the group
2. Send a message in the group
3. Visit: https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
4. Look for "chat":{"id":-1001234567890}
5. Copy the chat ID

### Step 3: Edit the Script
Open `telegram_bot.py` and replace:

```python
BOT_TOKEN = "YOUR_NEW_BOT_TOKEN_HERE"  # Paste your NEW token from BotFather
GROUP_CHAT_ID = "-1001234567890"  # Paste your group chat ID (keep the quotes)
AUTHORIZED_USER_ID = 123456789  # Paste your user ID (no quotes, just the number)
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Bot
```bash
python telegram_bot.py
```

## 📱 How to Use:

1. **Send a DM to your bot** with an address
2. **The bot forwards it to the group** with confirmation buttons
3. **Group members click** "✅ Confirmed" or "❌ Not Confirmed"
4. **The message updates** to show the response

## 🚀 Deploy to Railway (Optional):

1. Create a `Procfile`:
   ```
   worker: python telegram_bot.py
   ```

2. Set environment variables in Railway:
   - `BOT_TOKEN` = your bot token
   - `GROUP_CHAT_ID` = your group chat ID
   - `AUTHORIZED_USER_ID` = your user ID

3. Update the script to use environment variables:
   ```python
   BOT_TOKEN = os.getenv("BOT_TOKEN")
   GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")
   AUTHORIZED_USER_ID = int(os.getenv("AUTHORIZED_USER_ID"))
   ```

## ⚡ Quick Test:

1. Start the bot
2. Send it a test message: "123 Main Street"
3. Check your group - should see the message with buttons
4. Click a button - should see it update

## 🔒 Security Tips:

- ✅ Never share your bot token publicly
- ✅ Use environment variables for production
- ✅ Only authorized users can send messages
- ✅ Revoke and regenerate tokens if exposed
