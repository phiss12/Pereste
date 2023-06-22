from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key =  "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"

messages = [{"role": "system", "content": "You are a kind helpful assistant."}]

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.form['user_message']
        messages.append({"role": "user", "content": user_message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return render_template('index.html', assistant_message=reply)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
