import cv2, pygame, numpy
from PIL import Image

capture = cv2.VideoCapture(0)

if capture.isOpened():
    val, frame = capture.read()
else:
    val = False

height = 800
chars = "   `^,.:%;&8$@@BWH##MMMMMMMMMMMM"
width = int((frame.shape[1]/frame.shape[0])*height)
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("monospace", 12)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("window")

def get_ascii(image):
    s = len(chars)/256
    im = image.resize((width, height)).convert("L")
    w,h = int((image.size[0]/4.5)), int((image.size[1]/4.5)*(4/7))
    im = im.resize((w,h))
    t = []
    for row in numpy.array(im):
        a = ""
        for col in row[:-2]:
            a+=chars[int(col*s)]
        t.append(a)
    return t

done = False
while val and not done:
    val, frame = capture.read()
    image = Image.fromarray(frame)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))
    d = get_ascii(image)
    for i in range(len(d)):
        ts = font.render(d[i][::-1], False, (255,255,255))
        screen.blit(ts, (0, i*12))
    pygame.display.flip()
    pygame.time.wait(1)
pygame.quit()
