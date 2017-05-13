class BaseScene:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.z_index = 1

    def activate(self):
        pass

    def close(self):
        pass

    def context_lost(self):
        pass

    def context_state_lost(self):
        pass

    def deactivate(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def expose(self):
        pass

    def hide(self):
        pass

    def key_press(self, key, modifier):
        pass

    def mouse_motion(self, x, y, dx, dy):
        pass

    def mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def mouse_enter(self, x, y):
        pass

    def mouse_leave(self, x, y):
        pass

    def mouse_press(self, x, y, btn, modifier):
        pass

    def mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass

    def mouse_release(self, x, y, button, modifiers):
        pass

    def move(self, x, y):
        pass

    def resize(self, width, height):
        pass

    def show(self):
        pass

    def save(self):
        pass


class BlockingScene(BaseScene):
    def activate(self):
        return False

    def close(self):
        return False

    def context_lost(self):
        return False

    def context_state_lost(self):
        return False

    def deactivate(self):
        return False

    def update(self):
        return False

    def draw(self):
        return False

    def expose(self):
        return False

    def hide(self):
        return False

    def key_press(self, key, modifier):
        return False

    def mouse_motion(self, x, y, dx, dy):
        return False

    def mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        return False

    def mouse_enter(self, x, y):
        return False

    def mouse_leave(self, x, y):
        return False

    def mouse_press(self, x, y, btn, modifier):
        return False

    def mouse_scroll(self, x, y, scroll_x, scroll_y):
        return False

    def mouse_release(self, x, y, button, modifiers):
        return False

    def move(self, x, y):
        return False

    def resize(self, width, height):
        return False

    def show(self):
        return False

    def save(self):
        return False

