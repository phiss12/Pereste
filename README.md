# Pereste Assistant

Pereste Assistant is a Flask-based web application powered by the OpenAI API. It serves as an intelligent chatbot designed to assist with electronic discharge summaries. By providing real-time responses to user queries, it helps clarify medical procedures, diagnoses, and related information.

## Project Structure

The Pereste Assistant project includes the following main components:

- `app.py` - This Python script runs the Flask application and contains the necessary routes for request handling.
- `templates/index.html` - This HTML file creates the user interface for the Pereste Assistant. It includes a chat area where the dialogue between the user and the assistant is displayed.
- `static/styles.css` - This CSS file styles the application, defining the visual layout and design of the HTML elements.
- `static/logo.png` - This image file is the logo displayed in the application's header.
- `static/favicon.ico` - This image file serves as the favicon for the webpage, visible in the browser tab.

## Installation and Execution

To set up and run the Pereste Assistant, follow these steps:

1. Ensure you have Python 3.6 or a newer version installed.
2. Install the required Python packages using this command: `pip install -r requirements.txt`
3. Launch the Flask application with: `python app.py`
4. Open a web browser and navigate to `http://localhost:5000` to interact with the Pereste Assistant.

## Customization

You can customize the HTML, CSS, and Python files to modify the functionality and appearance of the Pereste Assistant. For instance, replace `logo.png` and `favicon.ico` in the `static` directory with your own images and adjust the styles in `styles.css` to change the visual design of the webpage. If you change the filenames, remember to update the references in `index.html` and `app.py`.
