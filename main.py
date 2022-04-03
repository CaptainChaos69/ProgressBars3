from direct.showbase.ShowBase import *
from panda3d.core import loadPrcFileData
from direct.gui.DirectGui import *
from direct.task import *

confVars = """
window-title Progress Bars
"""

loadPrcFileData("",confVars)

class Bars(ShowBase):
    def __init__(self):
        super().__init__()

        global v1, v2, v3, r1, r2, r3

        self.bar1 = DirectWaitBar(text=str(v1)+" / "+str(r1), range=r1, value=v1, pos=(0, .4, .4), scale=1)

        self.bar2 = DirectWaitBar(text=str(v2)+" / "+str(r2), range=r2, value=v2, pos=(0, .4, .1), scale=1)

        self.bar3 = DirectWaitBar(text=str(v3)+" / "+str(r3), range=r3, value=v3, pos=(0, .4, -.2), scale=1)

        self.taskMgr.add(self.update1, "update1", priority=1)



    def update1(self, task1):
        global v1, v2, v3, r1, r2, r3

        self.bar1 = DirectWaitBar(text=str(v1)+" / "+str(r1), range=r1, value=v1, pos=(0, .4, .4), scale=1)

        if v1 < r1:
            v1 += 1
            return Task.cont
        elif v2 < r2:
            self.taskMgr.add(self.update2, "update2", priority=2, appendTask=True)


    def update2(self, task2):
        global v1, v2, v3, r1, r2, r3
        self.bar2 = DirectWaitBar(text=str(v2)+" / "+str(r2), range=r2, value=v2, pos=(0, .4, .1), scale=1)

        if v2 < r2:
            v2 += 1
            return Task.cont
        elif v3 < r3:
            self.taskMgr.add(self.update3, "update2", priority=3, appendTask=True)

    def update3(self, task3):
        global v1, v2, v3, r1, r2, r3
        self.bar3 = DirectWaitBar(text=str(v3)+" / "+str(r3), range=r3, value=v3, pos=(0, .4, -.2), scale=1)

        if v3 < r3:
            v3 += 1
            return Task.cont

def endApp():
    game.finalizeExit()


b = DirectButton(text=("Stop Animation"),
                 scale=.05, command=endApp, pos=(0,0,-0.8))

barInfo = [0,1000,200,400,450,550]
global v1, v2, v3, r1, r2, r3
v1 = barInfo[0]
r1 = barInfo[1]
v2 = barInfo[2]
r2 = barInfo[3]
v3 = barInfo[4]
r3 = barInfo[5]


game = Bars()
game.run()
