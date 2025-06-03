import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from skybox import draw_skybox, load_skybox
from camera import Camera
from cube import draw_cube
from utils import load_texture

def setup():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [2, 5, 5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 800 / 600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    setup()
    camera = Camera([0, 1.5, 15])  # Start camera at height 1.5
    texture = load_texture("textures/crate.jpg")
    skybox = load_skybox("textures/skybox")

    velocity_y = 0
    on_ground = True

    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60)
        fps = int(clock.get_fps())
        pygame.display.set_caption(f"3D Engine - FPS: {fps}")

        dx, dy = pygame.mouse.get_rel()
        camera.mouse_move(dx, dy)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == VIDEORESIZE:
                width, height = event.size
                glViewport(0, 0, width, height)
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                gluPerspective(60, width / height, 0.1, 100.0)
                glMatrixMode(GL_MODELVIEW)


        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return
        if keys[K_w]: camera.move('FORWARD')
        if keys[K_s]: camera.move('BACKWARD')
        if keys[K_a]: camera.move('LEFT')
        if keys[K_d]: camera.move('RIGHT')
        if keys[K_SPACE] and on_ground:
            velocity_y = 0.25
            on_ground = False

        # Apply gravity
        velocity_y -= 0.01
        camera.position[1] += velocity_y
        if camera.position[1] < 1.5:
            camera.position[1] = 1.5
            velocity_y = 0
            on_ground = True

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        camera.apply()

        draw_skybox(skybox)

        for x in range(-3, 4, 3):
            for y in range(-3, 4, 3):
                for z in range(-3, 4, 3):
                    glPushMatrix()
                    glTranslatef(x, y, z)
                    glRotatef(pygame.time.get_ticks() * 0.05, 1, 1, 0)
                    draw_cube(texture_id=texture)
                    glPopMatrix()

        pygame.display.flip()

if __name__ == "__main__":
    main()
