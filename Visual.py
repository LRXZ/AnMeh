import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from Quaternion import *
import Change_matrix


def visual(data, Matrix):
    video_flags = OPENGL | DOUBLEBUF
    pygame.init()
    screen = pygame.display.set_mode((800, 610), video_flags)
    pygame.display.set_caption("AnMeh Rocket")
    resizewin(800, 610)
    init()
    frames = 0
    ticks = pygame.time.get_ticks()
    data1 = data
    while 1:
        event = pygame.event.poll()
        [roll, pitch, yaw] = data
        draw(roll, pitch, yaw, Matrix)
        pygame.display.flip()
        frames += 1
        if (event.type == pygame.QUIT) or (data == data1):
            break


def resizewin(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0 * width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init():
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def draw(nx, ny, nz, Matrix):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0.0, -7.0)
    drawText((-2.6, 1.8, 2), "AnMeh Rocket", 18)
    drawText((-2.6, -2.2, 2), "пока в доработке, закрывать GUI", 16)
    drawText((-2.6, -2, 2), "quaternion = " + quat_to_string(Euler_to_Quaternion(nx, ny, nz)), 14)
    roll = nx
    pitch = ny
    yaw = nz
    roll = roll * m.pi / 180
    pitch = pitch * m.pi / 180
    yaw = yaw * m.pi / 180
    drawText((-2.6, -1.8, 2),
             "Крен: %f, Тангаж: %f, Рысканье: %f" % (roll * 180 / m.pi, pitch * 180 / m.pi, yaw * 180 / m.pi), 16)
    Vectors_static()
    R1 = Change_matrix.change_matrix(roll, pitch, yaw)
    R1 = Matrix * R1
    x1 = R1 * np.array([[1], [0], [0]])
    x1 = x1 / np.linalg.norm(x1)
    y1 = R1 * np.array([[0], [1], [0]])
    y1 = y1 / np.linalg.norm(y1)
    z1 = R1 * np.array([[0], [0], [1]])
    z1 = z1 / np.linalg.norm(z1)

    glRotatef(roll * 180 / m.pi, x1[0], y1[0], z1[0])  # крен
    glRotatef(pitch * 180 / m.pi, x1[1], y1[1], z1[1])  # тангаж
    glRotatef(yaw * 180 / m.pi, x1[2], y1[2], z1[2])  # рысканье
    Rocket()
    Vectors()


def Vectors_static():
    glBegin(GL_LINES)

    glColor3f(1, 0.5, 0)  # ох
    glVertex3f(5, 0, 0)
    glVertex3f(0, 0, 0)

    glColor3f(0, 1, 0.5)  # оу
    glVertex3f(0, 5, 0)
    glVertex3f(0, 0, 0)

    glColor3f(0.5, 0, 1)  # оz
    glVertex3f(0, 0, 5)
    glVertex3f(0, 0, 0)

    glEnd()


def Vectors():
    glBegin(GL_LINES)

    glColor3f(1, 0, 0)  # красный ох
    glVertex3f(5, 0, 0)
    glVertex3f(0, 0, 0)

    glColor3f(0, 1, 0)  # зеленый оу
    glVertex3f(0, 5, 0)
    glVertex3f(0, 0, 0)

    glColor3f(0, 0, 1)  # синий оz
    glVertex3f(0, 0, 5)
    glVertex3f(0, 0, 0)

    glEnd()


def Rocket():
    glBegin(GL_QUADS)

    glColor3f(0.7, 0.3, 0.2)
    glVertex3f(-2.5, 0.5, 0.5)  # A
    glVertex3f(2.5, 0.5, 0.5)  # A1
    glVertex3f(2.5, -0.5, 0.5)  # B1
    glVertex3f(-2.5, -0.5, 0.5)  # B

    glColor3f(0.2, 0.7, 0.5)
    glVertex3f(-2.5, 0.5, 0.5)  # A
    glVertex3f(2.5, 0.5, 0.5)  # A1
    glVertex3f(2.5, 0.5, -0.5)  # C1
    glVertex3f(-2.5, 0.5, -0.5)  # C

    glColor3f(0.2, 0.3, 0.7)
    glVertex3f(-2.5, 0.5, -0.5)  # C
    glVertex3f(2.5, 0.5, -0.5)  # C1
    glVertex3f(2.5, -0.5, -0.5)  # D1
    glVertex3f(-2.5, -0.5, -0.5)  # D

    glColor3f(0.5, 0.7, 0.2)
    glVertex3f(-2.5, -0.5, 0.5)  # B
    glVertex3f(2.5, -0.5, 0.5)  # B1
    glVertex3f(2.5, -0.5, -0.5)  # D1
    glVertex3f(-2.5, -0.5, -0.5)  # D

    glColor3f(0.6, 0.15, 0.15)  # типа оранжевое сопло
    glVertex3f(-2.5, 0.5, 0.5)  # A
    glVertex3f(-2.5, -0.5, 0.5)  # B
    glVertex3f(-2.5, -0.5, -0.5)  # D
    glVertex3f(-2.5, 0.5, -0.5)  # C

    glColor3f(0.6, 0.6, 0.3)
    glVertex3f(2.5, 0.5, 0.5)  # A1
    glVertex3f(3.5, 0, 0)  # F
    glVertex3f(2.5, -0.5, 0.5)  # B1
    glVertex3f(2.5, 0.5, 0.5)  # A1

    glColor3f(0.2, 0.65, 0.65)
    glVertex3f(2.5, 0.5, -0.5)  # C1
    glVertex3f(3.5, 0, 0)  # F
    glVertex3f(2.5, 0.5, 0.5)  # A1
    glVertex3f(2.5, 0.5, -0.5)  # C1

    glColor3f(0.3, 0.6, 0.6)
    glVertex3f(2.5, 0.5, -0.5)  # C1
    glVertex3f(3.5, 0, 0)  # F
    glVertex3f(2.5, -0.5, -0.5)  # D1
    glVertex3f(2.5, 0.5, -0.5)  # C1

    glColor3f(0.65, 0.65, 0.2)
    glVertex3f(2.5, -0.5, -0.5)  # D1
    glVertex3f(3.5, 0, 0)  # F
    glVertex3f(2.5, -0.5, 0.5)  # B1
    glVertex3f(2.5, -0.5, -0.5)  # D1

    glColor3f(0.8, 0.2, 0.9)
    glVertex3f(0, 0.5, 0)  # O1
    glVertex3f(-2.5, 1, 0)  # C5
    glVertex3f(-2.5, 0.5, 0.05)  # C3
    glVertex3f(0, 0.5, 0)  # O1

    glColor3f(0.8, 0.2, 0.9)
    glVertex3f(0, 0.5, 0)  # O1
    glVertex3f(-2.5, 1, 0)  # C5
    glVertex3f(-2.5, 0.5, -0.05)  # C4
    glVertex3f(0, 0.5, 0)  # O1

    glColor3f(0.8, 0.2, 0.9)
    glVertex3f(-2.5, 0.5, 0.05)  # C3
    glVertex3f(-2.5, 1, 0)  # C5
    glVertex3f(-2.5, 0.5, -0.05)  # C4
    glVertex3f(-2.5, 0.5, 0.05)  # C3

    glColor3f(0.8, 0.2, 0.9)
    glVertex3f(0, -0.5, 0)  # O1
    glVertex3f(-2.5, -1, 0)  # C5
    glVertex3f(-2.5, -0.5, 0.05)  # C3
    glVertex3f(0, -0.5, 0)  # O1

    glColor3f(0.8, 0.2, 0.9)
    glVertex3f(0, -0.5, 0)  # O1
    glVertex3f(-2.5, -1, 0)  # C5
    glVertex3f(-2.5, -0.5, -0.05)  # C4
    glVertex3f(0, -0.5, 0)  # O1

    glColor3f(0.8, 0.2, 0.9)
    glVertex3f(-2.5, -0.5, 0.05)  # C3
    glVertex3f(-2.5, -1, 0)  # C5
    glVertex3f(-2.5, -0.5, -0.05)  # C4
    glVertex3f(-2.5, -0.5, 0.05)  # C3

    glEnd()


def drawText(position, textString, size):
    font = pygame.font.SysFont("Courier", size, True)
    textSurface = font.render(textString, True, (255, 255, 255, 255), (0, 0, 0, 255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glRasterPos3d(*position)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
