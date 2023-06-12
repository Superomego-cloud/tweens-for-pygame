import numpy as np
import time, pygame, typing

screen = pygame.display.set_mode([500,100])


class proto:
    def __init__(self, **kwargs):
        self.hitbox = pygame.Rect(kwargs["location"], kwargs["size"])
        self.currentTween = None
        
class tween:
    def __init__(self, easingStyle:typing.Callable, d:int, t:int, obj:proto, dirList:list, reverse:bool=False):
        
        self.obj = obj
        if not self.obj.currentTween:
            self.obj.currentTween = self
        else:
            print("Error: can't have two tweens associated to one object")
            return
        
        self.tempData = [d, t, dirList]
        self.speedX, self.speedY = [(d/t)*dirList[0], (d/t)*dirList[1]]
        self.easingFunction = easingStyle
        self.frame = 0
        self.defaultPos = obj.hitbox
        self.temp = [0,0]
        self.reverse = reverse
    
    def update(self):
        
        if self.frame > FPS*self.tempData[1]:
            if self.reverse:
                print("starting")
                self.obj.currentTween = None
                newTween = tween(self.easingFunction, -self.tempData[0], self.tempData[1], self.obj, self.tempData[2])
                tweenlist.append(self.obj.currentTween)
            tweenlist.remove(self)
            del self
        
        self.obj.hitbox = self.defaultPos.copy()
        self.temp[0] = self.speedX*self.easingFunction(self.frame/FPS, self.tempData[1])
        self.temp[1] = self.speedY*self.easingFunction(self.frame/FPS, self.tempData[1])
        self.frame += 1
        self.obj.hitbox.move_ip(ErrorCheck(self.temp[0]), ErrorCheck(self.temp[1]))


def ErrorCheck(x):
    if abs(np.round(x)-x)<0.01:
        return np.round(x)
    else:
        return x
        
def Linear(x, s):
    return x

def xpo(x, s):
    return np.power(s+1, 1/s)**x - 1

def Expo(x, s):
    return xpo(xpo(x,s), s)

def Quadratic(x, s):
    return np.sqrt(s*x)

FPS = 450
running = True
rect1 = proto(location=[0,0], size=[100,100])
rect2 = proto(location=[0,0], size=[100,100])
rect3 = proto(location=[0,0], size=[100,100])
tweenlist = [tween(Quadratic, 400, 5, rect1, [1,0]), tween(Expo, 400, 5, rect2, [1,0]), tween(Linear, 400, 5, rect3, [1,0], True)]
clock = pygame.time.Clock()      
i = 0

pygame.draw.rect(screen, [255,0,0], rect1.hitbox)
pygame.draw.rect(screen, [0,255,0], rect2.hitbox)
pygame.draw.rect(screen, [0,0,255], rect3.hitbox)
pygame.display.update()

while running:
    
    clock.tick(FPS)
    i += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    screen.fill([0,0,0])
    
    if len(tweenlist)>0 and i>1000:
        for twn in tweenlist:
            try:
                twn.update()
            except:
                pass
            
    pygame.draw.rect(screen, [255,0,0], rect1.hitbox)
    pygame.draw.rect(screen, [0,255,0], rect2.hitbox)
    pygame.draw.rect(screen, [0,0,255], rect3.hitbox)
    pygame.display.update()

pygame.quit()