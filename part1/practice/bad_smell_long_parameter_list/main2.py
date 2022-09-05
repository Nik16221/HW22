class Unit:
    def __init__(self, field, state, speed, x, y):
        self.field = field
        self.state = state
        self.speed = speed
        self.x = x
        self.y = y

    def move(self, direction):

        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(x=self.x, y=self.y + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=self.x, y=self.y - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=self.x - speed, y=self.y, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(x=self.x + speed, y=self.y, unit=self)

    def _get_speed(self):
        if self.state == "fly":
            return self.speed * 1.2
        elif self.state == "crawl":
            return self.speed * 0.5
