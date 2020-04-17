import random
import time
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for name in range(num_users):
            self.add_user(name)

        # Make a list of all possible friendships
        friendships_to_add = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                friendships_to_add.append((user, friend))

        # Shuffle the list (Fisher-Yates shuffle)
        for idx in range(len(friendships_to_add)):
            rand_idx = random.randint(0, len(friendships_to_add) - 1)
            friendships_to_add[idx], friendships_to_add[rand_idx] = friendships_to_add[rand_idx], friendships_to_add[idx]

        # Create friendships
        pairs_needed = num_users * avg_friendships // 2
        for user, friend in friendships_to_add[:pairs_needed]:
            self.add_friendship(user, friend)

    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for name in range(num_users):
            self.add_user(name)

        # Create friendships
        friendships_added = 0
        pairs_needed = num_users * avg_friendships // 2
        while friendships_added < pairs_needed:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if user_id != friend_id and friend_id not in self.friendships[user_id]:
                self.add_friendship(user_id, friend_id)
                friendships_added += 1

            # find random friend_id out of remaining available id's
            # print(self.friendships[user_id])
            # friendships_added += 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        path = [user_id]
        queue = Queue()
        queue.enqueue(path)
        while queue.size() > 0:
            current_path = queue.dequeue()
            if current_path[-1] not in visited:
                visited[current_path[-1]] = current_path

            for friend in self.friendships[current_path[-1]]:
                if friend not in visited:
                    queue.enqueue(current_path + [friend])
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    # Question #2
    sg.populate_graph(1000, 5)
    connections = sg.get_all_social_paths(1)

    degree_of_separation_sum = 0
    for key in connections:
        degree_of_separation_sum += len(connections[key])
    degree_of_separation_avg = degree_of_separation_sum / len(connections)
    print(f"Avg. degree of separation between user and network = {degree_of_separation_avg}")

    # Stretch Goal #2
    start = time.time()
    sg.populate_graph(1000, 20)
    end = time.time()
    
    print(f"O(n^2) time elapsed: {end - start}")

    start = time.time()
    sg.populate_graph_linear(1000, 20)
    end = time.time()
    linear = end - start
    print(f"  O(n) time elapsed: {linear}")

