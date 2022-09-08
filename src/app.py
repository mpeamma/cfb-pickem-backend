import firebase_admin
from flask import Flask
from dotenv import load_dotenv
from controllers.group_controller import groups_api
from controllers.schedule_controller import schedule_api
from controllers.selection_controller import selection_api
from controllers.game_set_controller import game_set_api


load_dotenv(".env.local")
app = Flask(__name__)

app.register_blueprint(groups_api, url_prefix="/api/groups")
app.register_blueprint(schedule_api, url_prefix="/api/schedule")
app.register_blueprint(selection_api, url_prefix="/api/selection")
app.register_blueprint(game_set_api, url_prefix="/api/game_set")

firestore_app = firebase_admin.initialize_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
