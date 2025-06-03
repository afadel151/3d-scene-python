from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

faces = [
    "right.jpg", "left.jpg", "top.jpg",
    "bottom.jpg", "front.jpg", "back.jpg"
]

def load_skybox(folder):
    textures = glGenTextures(6)
    for i, face in enumerate(faces):
        path = f"{folder}/{face}"
        surf = pygame.image.load(path)
        image = pygame.image.tostring(surf, "RGB", 1)
        w, h = surf.get_size()
        glBindTexture(GL_TEXTURE_2D, textures[i])
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    return textures

def draw_skybox(textures, size=50):
    glPushMatrix()
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    glColor3f(1, 1, 1)

    # Right
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f( size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f( size, -size,  size)
    glTexCoord2f(1, 1); glVertex3f( size,  size,  size)
    glTexCoord2f(0, 1); glVertex3f( size,  size, -size)
    glEnd()

    # Left
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-size, -size,  size)
    glTexCoord2f(1, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 1); glVertex3f(-size,  size, -size)
    glTexCoord2f(0, 1); glVertex3f(-size,  size,  size)
    glEnd()

    # Top
    glBindTexture(GL_TEXTURE_2D, textures[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-size, size,  size)
    glTexCoord2f(1, 0); glVertex3f( size, size,  size)
    glTexCoord2f(1, 1); glVertex3f( size, size, -size)
    glTexCoord2f(0, 1); glVertex3f(-size, size, -size)
    glEnd()

    # Bottom
    glBindTexture(GL_TEXTURE_2D, textures[3])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f( size, -size, -size)
    glTexCoord2f(1, 1); glVertex3f( size, -size,  size)
    glTexCoord2f(0, 1); glVertex3f(-size, -size,  size)
    glEnd()

    # Front
    glBindTexture(GL_TEXTURE_2D, textures[4])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f( size, -size,  size)
    glTexCoord2f(1, 0); glVertex3f(-size, -size,  size)
    glTexCoord2f(1, 1); glVertex3f(-size,  size,  size)
    glTexCoord2f(0, 1); glVertex3f( size,  size,  size)
    glEnd()

    # Back
    glBindTexture(GL_TEXTURE_2D, textures[5])
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f( size, -size, -size)
    glTexCoord2f(1, 1); glVertex3f( size,  size, -size)
    glTexCoord2f(0, 1); glVertex3f(-size,  size, -size)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glPopMatrix()
