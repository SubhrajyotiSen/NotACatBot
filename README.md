# This is Not a Cat Bot
Since you think this is a cat bot, here we go

## Deploy to Vercel
This bot is ready to be deployed to Vercel as a Serverless Function.

1. Fork this repository.
2. Import the project into Vercel.
3. Add the Environment Variable `TG_BOT_TOKEN` with your Telegram Bot Token.
4. Set the Telegram Webhook to your Vercel URL:
   ```bash
   curl "https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://<YOUR_VERCEL_PROJECT>.vercel.app/"
   ```

## Local Development
### Using Polling (main.py)
To run the bot locally using polling (no webhook needed):

```bash
pip install -r requirements.txt
export TG_BOT_TOKEN=YOUR_API_TOKEN
python main.py
```

### Using Docker
```
git clone https://github.com/SubhrajyotiSen/NotACatBot
cd NotACatBot
docker build -t catbot .
docker run -d -e TG_BOT_TOKEN=YOUR_API_TOKEN catbot
```
(Note: File logging to `/data` has been replaced with standard output logging for cloud compatibility.)

## Screenshots
<p>
  <img width="285" src="screenshots/ss1.jpg?raw=true">
  <img width="285" src="screenshots/ss2.jpg?raw=true">
</p>