from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import *
from random import *
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        aaa = randint(-3000,3000)
        bbb = randint(-3000,3000)
        

        
        self.scene = self.loader.loadModel("models/environment")
        
        self.scene.reparentTo(self.render)
       
        self.scene.setScale(1, 1, 1)#此处的1相当于setPos的1250
        self.scene.setPos(-8, 42, 0)
        #界限
        self.scene3 = self.loader.loadModel("models/environment")
        
        self.scene3.reparentTo(self.render)
       
        self.scene3.setScale(1, 1, 1)#此处的1相当于setPos的1250
        self.scene3.setPos(-8, 42,1250)
        #界限
        self.scen = loader.loadModel("models/environment")
        self.scen.reparentTo(self.render)
        self.scen.setScale(1,1,1)
        self.scen.setPos(-1257,42,1)
        #self.scene.detach_node()#可运行代码
        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")#视觉调整

       #中噢噢噢噢噢噢噢噢哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)


        
        self.pandaActor.loop("walk")

        
        posInterval1 = self.pandaActor.posInterval(15,
                                                   Point3(5, -11, 0),
                                                   startPos=Point3(5, 11, 0))
        posInterval2 = self.pandaActor.posInterval(15,
                                                   Point3(5, 11, 0),
                                                   startPos=Point3(5, -11, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))

       
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()
        #aaaaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzzzzzz大大啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        self.pandaActoraa = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActoraa.setScale(0.005, 0.005, 0.005)
        self.pandaActoraa.reparentTo(self.render)
        self.pandaActoraa.loop("walk")
        aa = self.pandaActoraa.posInterval(15,
                                        Point3(0.2, -10, 0),
                                        startPos=Point3(0.2, 10, 0))
        bb = self.pandaActoraa.posInterval(15,
                                        Point3(0.2, 10, 0),
                                        startPos=Point3(0.2, -10, 0))
        cc = self.pandaActoraa.hprInterval(3,
                                        Point3(180, 0, 0),
                                        startHpr=Point3(0, 0, 0))
        dd = self.pandaActoraa.hprInterval(3,
                                        Point3(0, 0, 0),
                                        startHpr=Point3(180, 0, 0))
        self.pandadaaa = Sequence(aa,cc,bb,dd,name="pandadaaa")
        self.pandadaaa.loop()
        #界限小哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦哦
        self.pandaActorab = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActorab.setScale(0.3, 0.3, 0.3)
        self.pandaActorab.reparentTo(self.render)
        self.pandaActorab.loop("walk")

        a = self.pandaActorab.posInterval(15,
                                        Point3(-5, -10, 0),
                                        startPos=Point3(-5, 10, 0))
        b = self.pandaActorab.posInterval(15,
                                        Point3(-5, 10, 0),
                                        startPos=Point3(-5, -10, 0))
        
        c = self.pandaActorab.hprInterval(2,
                                        Point3(180, 0, 0),
                                        startHpr=Point3(0, 0, 0))
        d = self.pandaActorab.hprInterval(2,
                                        Point3(0, 0, 0),
                                        startHpr=Point3(180, 0, 0))
        self.pandad = Sequence(a,c,b,d,name="pandad")
        self.pandad.loop()
        #界限
       

        #self.pandaActorab.detach_node()#删除小熊猫
        #self.pandaActor.detach_node()#删除中熊猫
        #self.pandaActoraa.detach_node()#删除大熊猫
    """def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 20 * sin(angleRadians))
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont#视觉函数"""


app = MyApp()
app.run()
