import os

# Get the absolute path to the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "3D Scene"

# Camera settings
CAMERA_POSITION = (0.0, 0.0, 3.0)
CAMERA_YAW = -90.0
CAMERA_PITCH = 0.0
CAMERA_SPEED = 0.05
CAMERA_SENSITIVITY = 0.1

# Lighting settings
LIGHT_POSITION = (1.2, 1.0, 2.0)
LIGHT_COLOR = (1.0, 1.0, 1.0)
OBJECT_COLOR = (0.2, 0.5, 0.8)

# Rendering settings
FOV = 45.0
NEAR_PLANE = 0.1
FAR_PLANE = 100.0

# Shader paths
VERTEX_SHADER_PATH = os.path.join(PROJECT_ROOT, "shaders", "vertex.glsl")
FRAGMENT_SHADER_PATH = os.path.join(PROJECT_ROOT, "shaders", "fragment.glsl")

# Texture paths
TEXTURE_PATH = os.path.join(PROJECT_ROOT, "assets", "textures", "container.jpg") 