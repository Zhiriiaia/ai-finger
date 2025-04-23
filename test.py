from flask import Flask, render_template
from pythreejs import *

app = Flask(__name__)

# Create a 3D cube
cube = Mesh(
    geometry=BoxGeometry(1, 1, 1),
    material=MeshBasicMaterial(color='red'),
    position=[0, 0, 0]
)

# Create a scene
scene = Scene(children=[cube])

# Create a camera and set it in position
camera = PerspectiveCamera(fov=75, aspect=1, near=0.1, far=1000)
camera.position = [3, 3, 3]
camera.lookAt([0, 0, 0])

# Setup a WebGLRenderer
renderer = WebGLRenderer(width=800, height=600)
renderer.set_state(800, 600)

# Define a rotation update function
def update_rotation():
    # Ensure cube.rotation is a Vector3 object (not a tuple)
    if isinstance(cube.rotation, tuple):
        cube.rotation = [0, 0, 0]  # Initializing as a list, can also be Vector3 if needed

    # Update rotation (this assumes cube.rotation is a list with 3 elements: [x, y, z])
    cube.rotation[0] += 0.01  # Rotate around the X-axis
    cube.rotation[1] += 0.01  # Rotate around the Y-axis
    cube.rotation[2] += 0.01  # Rotate around the Z-axis

# Define a simple route to serve the page
@app.route('/')
def home():
    update_rotation()  # Update the rotation each time the route is called
    return render_template('index.html', cube=cube, scene=scene, camera=camera, renderer=renderer)

if __name__ == '__main__':
    app.run(debug=True)
