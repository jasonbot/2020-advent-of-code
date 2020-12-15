directions = ('E', 'S', 'W', 'N')

direction_vectors = {
    'E': (1, 0),
    'W': (-1, 0),
    'N': (0, 1),
    'S': (0, -1),
}

instructions = [(lambda x: (x[0], int(x[1:])))(row.strip()) for row in open('day12.input')]


class Ship:
    def __init__(self, waypointy=False):
        self.direction = 'E'
        self.angle = 0
        self.east = 0
        self.north = 0
        self.actual_east = 0
        self.actual_north = 0
        self.waypointy = waypointy
        if self.waypointy:
            self.east, self.north = 10, 1
    def __repr__(self):
        if self.waypointy:
            return f"<East: {self.actual_east} North: {self.actual_north} Heading: {self.direction} MD: {abs(self.actual_east) + abs(self.actual_north)}>"
        else:
            return f"<East: {self.east} North: {self.north} Heading: {self.direction} MD: {abs(self.east) + abs(self.north)}>"
    def do_instruction(self, instruction, units):
        if instruction == 'F':
            if not self.waypointy:
                instruction = self.direction
        # Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
        # Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
        elif instruction in ('R', 'L'):
            if self.waypointy:
                print("WAYPT ROT", instruction, units, self.north, self.east)
                while units > 0:
                    if instruction == 'R':
                        self.east, self.north = (-self.north, self.east)
                    elif instruction == 'L':
                        self.east, self.north = (-self.north, -self.east)
                    units -= 90
                print("      ->MOVED", self.north, self.east)
                return
            else:
                direction = self.direction
                idx = directions.index(self.direction)
                if instruction == 'R':
                    idx += (units // 90)
                elif instruction == 'L':
                    idx -= (units // 90)
                self.direction = directions[idx % len(directions)]
                return

        # Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:
        # Action N means to move the waypoint north by the given value.
        # Action S means to move the waypoint south by the given value.
        # Action E means to move the waypoint east by the given value.
        # Action W means to move the waypoint west by the given value.
        if instruction in direction_vectors:
            vector = direction_vectors[instruction]
            self.east += (vector[0] * units)
            self.north += (vector[1] * units)
        elif instruction == 'F':
            self.actual_east += (self.east * units)
            self.actual_north += (self.north * units)
            # print("GO TO", self.actual_east,'+', self.east, self.actual_north,'+',self.north)
        else:
            raise ValueError(instruction)


my_boat = Ship()
my_weirder_boat = Ship(waypointy=True)

for instruction in instructions:
    my_boat.do_instruction(*instruction)
    my_weirder_boat.do_instruction(*instruction)

print(my_boat)
print(my_weirder_boat)
