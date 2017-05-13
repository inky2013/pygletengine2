import pyglet
import engine.text
import os
from os.path import join as path_join


class _SceneManager:
    def __init__(self):
        self._scenes = []

    def clear(self):
        self._scenes = []

    def __iter__(self):
        for item in self._scenes:
            yield item

    def __setitem__(self, name, value):
        value.name = name
        self._scenes.append(value)
        self._scenes.sort(key=lambda x: x.z_index, reverse=False)

    def __delitem__(self, key):
        for item in self._scenes:
            if item.name == key:
                del item

    def __getitem__(self, key):
        for i in self._scenes:
            if i.name == key:
                return i
        return None

    def add_scene(self, scene):
        self.__setitem__(scene.name, scene)


class AssetManager:
    DIR_BASE = "assets/"
    DIR_IMAGE = path_join(DIR_BASE, "images")
    DIR_FONT = path_join(DIR_BASE, "fonts")
    DIR_SOUND = path_join(DIR_BASE, "sound")
    DIR_TEXT = path_join(DIR_BASE, "text")
    DIR_SAVE = path_join("saves")
    DIR_CONFIG = "config"

    @staticmethod
    def ensure_directory(d, split=False):
        nd = d
        if split:
            nd = os.path.dirname(nd)
        try:
            os.makedirs(nd)
        except FileExistsError:
            pass
        return d


class Engine:
    _instance = None

    def __init__(self, config, logger=None):
        logger = engine.text.generate_logger(__name__, config.log_level)
        self.scene_manager = _SceneManager()
        self.config = config
        self._window = pyglet.window.Window(fullscreen=config.fullscreen, resizable=config.resizable, height=config.height, width=config.width)
        Engine._instance = self


    @staticmethod
    def get_engine():
        return Engine._instance

    def save_game(self):
        for scene in self.scene_manager:
            scene.save()

    def present(self):

        @self._window.event
        def on_activate():
            for scene in self.scene_manager:

                if scene.activate() is False:
                    return

        @self._window.event
        def on_close():
            for scene in self.scene_manager:

                if scene.close() is False:
                    return

        @self._window.event
        def on_context_lost():
            for scene in self.scene_manager:

                if scene.context_lost() is False:
                    return

        @self._window.event
        def on_context_state_lost():
            for scene in self.scene_manager:

                if scene.context_state_lost() is False:
                    return

        @self._window.event
        def on_deactivate():
            for scene in self.scene_manager:

                if scene.deactivate() is False:
                    return

        @self._window.event
        def on_draw(*args):
            for scene in self.scene_manager:

                if scene.draw() is False:
                    return

        @self._window.event
        def on_expose():
            for scene in self.scene_manager:

                if scene.expose() is False:
                    return

        @self._window.event
        def on_hide():
            for scene in self.scene_manager:

                if scene.hide() is False:
                    return

        @self._window.event
        def on_key_press(symbol, modifiers):
            for scene in self.scene_manager:

                if scene.key_press(symbol, modifiers) is False:
                    return
            if symbol == pyglet.window.key.ESCAPE:
                return pyglet.event.EVENT_HANDLED

        @self._window.event
        def on_key_release(*args):
            for scene in self.scene_manager:

                if scene.key_release(*args) is False:
                    return

        @self._window.event
        def on_mouse_drag(*args):
            for scene in self.scene_manager:

                if scene.mouse_drag(*args) is False:
                    return

        @self._window.event
        def on_mouse_enter(*args):
            for scene in self.scene_manager:

                if scene.mouse_enter(*args) is False:
                    return

        @self._window.event
        def on_mouse_leave(*args):
            for scene in self.scene_manager:

                if scene.mouse_leave(*args) is False:
                    return

        @self._window.event
        def on_mouse_motion(*args):
            for scene in self.scene_manager:

                if scene.mouse_motion(*args) is False:
                    return

        @self._window.event
        def on_mouse_press(*args):
            for scene in self.scene_manager:

                if scene.mouse_press(*args) is False:
                    return

        @self._window.event
        def on_mouse_scroll(*args):
            for scene in self.scene_manager:

                if scene.mouse_scroll(*args) is False:
                    return

        @self._window.event
        def on_mouse_release(*args):
            for scene in self.scene_manager:

                if scene.mouse_release(*args) is False:
                    return

        @self._window.event
        def on_move(*args):
            for scene in self.scene_manager:

                if scene.move(*args) is False:
                    return

        @self._window.event
        def on_resize(x, y):
            if x < 2:
                self._window.width = 2
            if y < 2:
                self._window.height = 2
            self.size = [x, y]
            for scene in self.scene_manager:

                if scene.resize(x, y) is False:
                    return
        @self._window.event
        def on_show():
            for scene in self.scene_manager:

                if scene.show() is False:
                    return

        def update(*args):
            for scene in self.scene_manager:

                if scene.update() is False:
                    return

        pyglet.clock.schedule_interval(update, 1 / float(60))
        pyglet.clock.schedule_interval(on_draw, 1 / float(60))
        pyglet.app.run()


