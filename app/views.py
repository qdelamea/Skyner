from flask import render_template
from app import app, WebGl
from flask_webglearth import WebGlEarth, MAP_TYPES, Marker, Polygon


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/more/project-management')
def projectManagement():
    return render_template('project-management.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/more/sidebar-left')
def technicalAspect():
    return render_template('technical-aspect.html')


@app.route('/more/sidebar-right')
def contribute():
    return render_template('contribute.html')


@app.route('/sign-in')
def signIn():
    return render_template('signin.html')


@app.route('/sign-up')
def signUp():
    return render_template('signup.html')


@app.route("/live")
def live():
    webgl_earth = WebGlEarth(zoom=1, map_type=MAP_TYPES.get('osm'),
                             center=[46.3, 30.4], atmosphere=True,
                             markers=[Marker(49.3, 30.4, "Hello world!")],
                             polygons=[Polygon(([45.1, 30.3],
                                                [46.1, 40.56], [50.3, 20.8]))])
    return render_template('live.html', webgl_map=webgl_earth)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
