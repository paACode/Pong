import permanentbrush

DEFAULT_SCREEN_WIDTH_PX = 1000
DEFAULT_SCREEN_HEIGHT_PX = 600

DEFAULT_COURT_WIDTH = DEFAULT_SCREEN_WIDTH_PX - 50
DEFAULT_COURT_HEIGHT = DEFAULT_SCREEN_HEIGHT_PX - 50
DEFAULT_BACKGROUND_COLOR = "Black"


class Court:

    def __init__(self):

        self.screen_width_px = DEFAULT_SCREEN_WIDTH_PX
        self.screen_height_px = DEFAULT_SCREEN_HEIGHT_PX

        self.width_px = DEFAULT_COURT_WIDTH
        self.height_px = DEFAULT_COURT_HEIGHT

        self.sideline_top = self.create_sideline("top")
        self.sideline_bottom = self.create_sideline("bottom")
        self.sideline_left = self.create_sideline("left")
        self.sideline_right = self.create_sideline("right")
        self.net = self.create_net()

    def create_sideline(self, sideline_type):
        brush = permanentbrush.PermanentBrush()
        brush.set_brush_size(5)
        if sideline_type == "top":
            sideline = brush.draw_line((-self.width_px / 2, self.height_px / 2),
                                       (self.width_px / 2, self.height_px / 2))
        elif sideline_type == "bottom":
            sideline = brush.draw_line((-self.width_px / 2, -self.height_px / 2),
                                       (self.width_px / 2, -self.height_px / 2))
        elif sideline_type == "left":
            sideline = brush.draw_line((-self.width_px / 2, -self.height_px / 2),
                                       (-self.width_px / 2, self.height_px / 2))
        elif sideline_type == "right":
            sideline = brush.draw_line((self.width_px / 2, -self.height_px / 2),
                                       (self.width_px / 2, self.height_px / 2))
        return sideline

    def create_net(self):
        brush = permanentbrush.PermanentBrush()
        brush.set_brush_size(5)
        net = brush.draw_line((0, self.height_px / 2), (0, -self.height_px / 2))
        return net
