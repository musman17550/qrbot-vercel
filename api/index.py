from flask import Flask, render_template_string

app = Flask(__name__)

CHATBOT_CONFIGS = {
    'QRBot': {
        'location_id': '0MurORC3LWv7IzsD7ht2',
        'widget_id': 'b4bac550-6c87-4304-bc58-9fd22d2ce2b4',
        'background_url': 'https://client-philipp.s3.ap-southeast-2.amazonaws.com/signatures/SCR-20241209-tjef.png'
    }
}

def get_chatbot_html(config):
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chatbot</title>
        <style>
            html, body {
                margin: 0;
                padding: 0;
                height: 100%;
                width: 100%;
                overflow: hidden;
            }
            body {
                background-image: url('{}');
                background-size: contain;
                background-position: center;
                background-repeat: no-repeat;
                display: flex;
                align-items: center;
                justify-content: center;
            }
        </style>
    </head>
    <body>
        <script>
        (function(w, d, s, o, f, js, fjs) {{
            w['LiveChatWidget'] = o;
            w[o] = w[o] || function() {{
            (w[o].q = w[o].q || []).push(arguments);
            }};
            js = d.createElement(s);
            js.id = o;
            js.src = f;
            js.async = 1;
            fjs = d.getElementsByTagName(s)[0];
            fjs.parentNode.insertBefore(js, fjs);
            js.onload = function() {{
            w.LiveChatWidget.init({{
                locationId: "{}",
                id: "{}"
            }});
            }};
        }}(window, document, 'script', 'LiveChatWidget', 'https://live-chat-widget.hlbots.com/live-chat-widget.iife.js'));
        </script>
    </body>
    </html>
    '''.format(
        config['background_url'],
        config['location_id'],
        config['widget_id']
    )

@app.route('/QRBot/')
def qr_bot():
    return render_template_string(get_chatbot_html(CHATBOT_CONFIGS['QRBot']))

@app.route('/')
def home():
    return "Server is running!"