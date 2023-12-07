import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class DiskRenderer:
    def __init__(self):
        self.rendering_mode = GL_FILL  # Default to solid rendering mode

    def handle_keypress(self, event):
        if event.key == pygame.K_p:
            self.rendering_mode = GL_POINT  # Switch to point rendering mode
        elif event.key == pygame.K_w:
            self.rendering_mode = GL_LINE  # Switch to wireframe rendering mode
        elif event.key == pygame.K_s:
            self.rendering_mode = GL_FILL  # Switch to solid rendering mode
        glPolygonMode(GL_FRONT_AND_BACK, self.rendering_mode)  # Update the rendering mode

    def load_texture(self):
        textureSurface = pygame.image.load('texture.jpg')
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()

        glEnable(GL_TEXTURE_2D)
        texid = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, texid)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    def draw_disk(self):
        self.quad = gluNewQuadric()
        gluQuadricTexture(self.quad, GL_TRUE)

        slices = 50
        inner_radius = 0.5
        outer_radius = 1.0
        gluDisk(self.quad, inner_radius, outer_radius, slices, 1)

    def show_disk(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        self.quad = gluNewQuadric()
        gluQuadricTexture(self.quad, GL_TRUE)

        self.load_texture()

        pygame.key.set_repeat(1, 10)
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        pygame.event.set_blocked(pygame.KEYDOWN)
        pygame.event.set_allowed(pygame.KEYDOWN)
        pygame.event.set_allowed(pygame.QUIT)
        pygame.event.set_allowed(pygame.VIDEORESIZE)
        pygame.event.set_allowed(pygame.ACTIVEEVENT)
        pygame.event.set_allowed(pygame.USEREVENT)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_keypress(event)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glRotatef(1, 3, 1, 1)
            self.draw_disk()
            pygame.display.flip()
            pygame.time.wait(10)

    def see_disk(self):
        gluPerspective(45, (800/600), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        self.load_texture()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_keypress(event)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glRotatef(1, 3, 1, 1)
            self.draw_disk()

def run_disk():
    disk = DiskRenderer()
    disk.show_disk()