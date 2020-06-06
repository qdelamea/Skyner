from flask import Flask
from flask_webglearth import WebGlEarth, WebGl, MAP_TYPES, Marker, Polygon

app = Flask(__name__)
WebGl(app)

from app import views