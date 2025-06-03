import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos, radians

# Camera parameters
camera_pos = np.array([0.0, 0.0, 3.0], dtype=np.float32)
camera_front = np.array([0.0, 0.0, -1.0], dtype=np.float32)
camera_up = np.array([0.0, 1.0, 0.0], dtype=np.float32)
yaw, pitch = -90.0, 0.0
last_x, last_y = 400, 300
first_mouse = True

def perspective(fovy, aspect, near, far):
    f = 1.0 / np.tan(np.radians(fovy) / 2)
    proj = np.zeros((4, 4), dtype=np.float32)
    proj[0, 0] = f / aspect
    proj[1, 1] = f
    proj[2, 2] = (far + near) / (near - far)
    proj[2, 3] = (2 * far * near) / (near - far)
    proj[3, 2] = -1.0
    return proj

def look_at(eye, center, up):
    f = center - eye
    f = f / np.linalg.norm(f)
    s = np.cross(f, up)
    s = s / np.linalg.norm(s)
    u = np.cross(s, f)
    view = np.identity(4, dtype=np.float32)
    view[0, :3] = s
    view[1, :3] = u
    view[2, :3] = -f
    view[0, 3] = -np.dot(s, eye)
    view[1, 3] = -np.dot(u, eye)
    view[2, 3] = np.dot(f, eye)
    return view

def mouse_callback(window, xpos, ypos):
    global yaw, pitch, last_x, last_y, first_mouse, camera_front
    if first_mouse:
        last_x, last_y = xpos, ypos
        first_mouse = False
    xoffset = xpos - last_x
    yoffset = last_y - ypos
    last_x, last_y = xpos, ypos
    sensitivity = 0.1
    xoffset *= sensitivity
    yoffset *= sensitivity
    yaw += xoffset
    pitch += yoffset
    pitch = max(-89.0, min(89.0, pitch))
    front = np.array([
        cos(radians(yaw)) * cos(radians(pitch)),
        sin(radians(pitch)),
        sin(radians(yaw)) * cos(radians(pitch))
    ], dtype=np.float32)
    camera_front[:] = front / np.linalg.norm(front)

def process_input(window):
    global camera_pos
    camera_speed = 0.05
    if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
        camera_pos[:] += camera_speed * camera_front
    if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
        camera_pos[:] -= camera_speed * camera_front
    if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
        camera_pos[:] -= np.cross(camera_front, camera_up) * camera_speed
    if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
        camera_pos[:] += np.cross(camera_front, camera_up) * camera_speed

def main():
    global last_x, last_y, first_mouse
    if not glfw.init():
        print("Failed to initialize GLFW")
        return

    window = glfw.create_window(800, 600, "3D Cube with Camera", None, None)
    if not window:
        print("Failed to create GLFW window")
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_cursor_pos_callback(window, mouse_callback)
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
    print(f"OpenGL Version: {glGetString(GL_VERSION)}")

    # Cube vertices (positions only)
    vertices = np.array([
        # Front face
        -0.5, -0.5,  0.5,
         0.5, -0.5,  0.5,
         0.5,  0.5,  0.5,
        -0.5,  0.5,  0.5,
        # Back face
        -0.5, -0.5, -0.5,
         0.5, -0.5, -0.5,
         0.5,  0.5, -0.5,
        -0.5,  0.5, -0.5,
    ], dtype=np.float32)

    indices = np.array([
        0, 1, 2, 2, 3, 0,  # Front
        1, 5, 6, 6, 2, 1,  # Right
        5, 4, 7, 7, 6, 5,  # Back
        4, 0, 3, 3, 7, 4,  # Left
        3, 2, 6, 6, 7, 3,  # Top
        4, 5, 1, 1, 0, 4   # Bottom
    ], dtype=np.uint32)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, None)
    glEnableVertexAttribArray(0)

    vertex_shader_source = """
    #version 330 core
    layout (location = 0) in vec3 aPos;
    uniform mat4 model;
    uniform mat4 view;
    uniform mat4 projection;
    void main()
    {
        gl_Position = projection * view * model * vec4(aPos, 1.0);
    }
    """

    fragment_shader_source = """
    #version 330 core
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(1.0, 0.0, 0.0, 1.0);  // Red color
    }
    """

    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, vertex_shader_source)
    glCompileShader(vertex_shader)

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragment_shader_source)
    glCompileShader(fragment_shader)

    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    glLinkProgram(shader_program)

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(window):
        process_input(window)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(shader_program)
        glBindVertexArray(vao)

        # Model matrix (rotate cube)
        angle = glfw.get_time()
        model = np.identity(4, dtype=np.float32)
        c, s = np.cos(angle), np.sin(angle)
        model[0, 0], model[0, 2] = c, s
        model[2, 0], model[2, 2] = -s, c

        # View and projection
        view = look_at(camera_pos, camera_pos + camera_front, camera_up)
        projection = perspective(45.0, 800/600, 0.1, 100.0)

        # Set uniforms
        loc = glGetUniformLocation(shader_program, "model")
        glUniformMatrix4fv(loc, 1, GL_FALSE, model)
        loc = glGetUniformLocation(shader_program, "view")
        glUniformMatrix4fv(loc, 1, GL_FALSE, view)
        loc = glGetUniformLocation(shader_program, "projection")
        glUniformMatrix4fv(loc, 1, GL_FALSE, projection)

        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)
        glfw.poll_events()

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

    glDeleteVertexArrays(1, [vao])
    glDeleteBuffers(1, [vbo])
    glDeleteBuffers(1, [ebo])
    glDeleteProgram(shader_program)
    glfw.terminate()

if __name__ == "__main__":
    main()