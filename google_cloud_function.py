import os
from datetime import datetime
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.models import (
    ImageSendMessage
)
import pytz

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_bot_api = LineBotApi(channel_access_token)

shirt_color = {
    0: 'https://github.com/bentocast/shirt-color-advisor-bot/blob/main/resources/Cloth_Monday.jpg?raw=true',
    1: 'https://github.com/bentocast/shirt-color-advisor-bot/blob/main/resources/Cloth_Tuesday.jpg?raw=true',
    2: 'https://github.com/bentocast/shirt-color-advisor-bot/blob/main/resources/Cloth_Wednesday.jpg?raw=true',
    3: 'https://github.com/bentocast/shirt-color-advisor-bot/blob/main/resources/Cloth_Thursday.jpg?raw=true',
    4: 'https://github.com/bentocast/shirt-color-advisor-bot/blob/main/resources/Cloth_Friday.jpg?raw=true',
    5: 'https://github.com/bentocast/shirt-color-advisor-bot/blob/main/resources/Cloth_Saturday.jpg?raw=true',
    6: 'https://github.com/bentocast/shirt-color-advisor-bot/blob/main/resources/Cloth_Sunday.jpg?raw=true',
}
BKK = pytz.timezone('Asia/Bangkok')

def callback(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    weekday = datetime.now().astimezone(BKK).weekday()
    image_message = ImageSendMessage(
        original_content_url=shirt_color[weekday],
        preview_image_url=shirt_color[weekday]
    )
    line_bot_api.broadcast(image_message)
    return 'OK'