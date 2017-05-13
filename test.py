import engine
import pyglet
from os.path import join

NAME = "gamename"

default_config = (
    engine.configloader.ConfigArgument("height", int, 480, "Window Height"),
    engine.configloader.ConfigArgument("width", int, 640, "Window Width"),
    engine.configloader.ConfigArgument("resizable", engine.configloader.boolean, True, "Resizable Window"),
    engine.configloader.ConfigArgument("fullscreen", engine.configloader.boolean, False, "Fullscreen window"),
    engine.configloader.ConfigArgument("log_level", str, "INFO", "Console Log Level"),
)

config = engine.configloader.JsonSave(engine.game.AssetManager.ensure_directory(join(engine.game.AssetManager.DIR_CONFIG, NAME+".json"), True), default_config)

game = engine.game.Engine(config.load_config().get_config())

class MyScene(engine.scene.BaseScene):
    def __init__(self):
        super().__init__("testscene")
        ball_image = pyglet.image.load(join(engine.game.AssetManager.DIR_IMAGE ,'ball.png'))
        self.bpc = engine.configloader.EncodedSave(engine.game.AssetManager.ensure_directory(join(engine.game.AssetManager.DIR_SAVE, "testsave.b64"), True),
                                              (engine.configloader.ConfigArgument("x", int, 50), engine.configloader.ConfigArgument("y", int, 50)))
        self.bpc.load_config()
        bpcv = self.bpc.get_config()
        self.ball = pyglet.sprite.Sprite(ball_image, x=bpcv.x, y=bpcv.y)

    def draw(self):
        self.ball.draw()

    def save(self):
        print("SAVE")
        self.bpc["x"] = self.ball.x
        self.bpc["y"] = self.ball.y
        self.bpc.save_config()

    def update(self):
        if 65362 in self._keys: # up
            self.ball.y += 1
        if 65364 in self._keys: # down
            self.ball.y -= 1
        if 65363 in self._keys: # right
            self.ball.x += 1
        if 65361 in self._keys: # left
            self.ball.x -= 1

game.scene_manager.add_scene(MyScene())

game.present()