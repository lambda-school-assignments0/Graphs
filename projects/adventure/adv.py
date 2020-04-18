from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = []

# Travel through all nodes with DFT and save output path
dfs_visited = set()
dfs_visited.add(player.current_room.id)
dfs_path = []
stack = Stack()
stack.push((player.current_room, ""))

while stack.size() > 0:
    current_room, direction = stack.pop()
    dfs_path.append((current_room.id, direction))

    for room_exit in current_room.get_exits():
        if current_room.get_room_in_direction(room_exit).id not in dfs_visited:
            dfs_visited.add(current_room.get_room_in_direction(room_exit).id)
            stack.push((current_room.get_room_in_direction(room_exit), room_exit))

# Iterate through `dfs_path` to add steps to `traversal_path`
for room_id, direction in dfs_path:
    # Skip first room because player is already there
    if direction != "":
        # If the direction results in the player moving into a room with an `id`
        # that matches `room_id`, move player and add direction to `traversal_path`
        if player.current_room.get_room_in_direction(direction) and player.current_room.get_room_in_direction(direction).id == room_id:
            player.travel(direction)
            traversal_path.append(direction)
        # If the direction results in the player moving into a room with an `id`
        # that does not match `room_id`, use BFS to find the shortest path between
        # the two nodes and move player accordingly and add steps to `traversal_path`
        else:
            bfs_path = [(player.current_room, "")]
            bfs_visited = set()
            bfs_visited.add(player.current_room.id)
            queue = Queue()
            queue.enqueue(bfs_path)

            while queue.size() > 0:
                current_path = queue.dequeue()

                if current_path[-1][0].id == room_id:
                    retrace = current_path

                for room_exit in current_path[-1][0].get_exits():
                    if current_path[-1][0].get_room_in_direction(room_exit).id not in bfs_visited:
                        bfs_visited.add(current_path[-1][0].get_room_in_direction(room_exit).id)
                        queue.enqueue(current_path + [(current_path[-1][0].get_room_in_direction(room_exit), room_exit)])

            for _, bfs_direction in retrace:
                if bfs_direction != "":
                    player.travel(bfs_direction)
                    traversal_path.append(bfs_direction)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")