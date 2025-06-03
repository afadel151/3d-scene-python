from OpenGL.GL import *
from OpenGL.GLUT import *

vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)

faces = (
    (0,1,2,3), (4,5,7,6),
    (0,1,5,4), (2,3,6,7),
    (1,2,7,5), (0,3,6,4)
)

tex_coords = (
    (0,0), (1,0), (1,1), (0,1)
)

def draw_cube(texture_id=None):
    if texture_id:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        for j, vertex in enumerate(face):
            if texture_id:
                glTexCoord2fv(tex_coords[j % 4])
            glVertex3fv(vertices[vertex])
    glEnd()

    if texture_id:
        glDisable(GL_TEXTURE_2D)
