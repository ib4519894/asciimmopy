import os, jsonpickle
import core, client

class Player(core.entity.Entity):
    def __init__(self, name, start_x, start_y, map):
        super().__init__(name, start_x, start_y, "@", map, False)
    
    def action(self):
        valid = False
        while not valid:
            user_input = input("> ")
            if user_input in "wasdh?help":
                valid = True
            else:
                print("Invalid Input, try again or view help (?/h/help)")
        
        if user_input in "?h" or user_input == "help":
            print("""
            Options:
                help (?/h/help) - view help
                up (w) - move player up
                down (s) - move player down
                left (a) - move player left
                right (d) - move player right
            """)
        elif user_input == "w":
            self._map.set_point(self.get_x_pos(), self.get_y_pos(), self._map._default)
            self.set_y_pos(self.get_y_pos() - 1)
            self._map.set_point(self.get_x_pos(), self.get_y_pos(), "@")
        elif user_input == "s":
            self._map.set_point(self.get_x_pos(), self.get_y_pos(), self._map._default)
            self.set_y_pos(self.get_y_pos() + 1)
            self._map.set_point(self.get_x_pos(), self.get_y_pos(), "@")
        elif user_input == "a":
            self._map.set_point(self.get_x_pos(), self.get_y_pos(), self._map._default)
            self.set_x_pos(self.get_x_pos() - 1)
            self._map.set_point(self.get_x_pos(), self.get_y_pos(), "@")
        elif user_input == "d":
            self._map.set_point(self.get_x_pos(), self.get_y_pos(), self._map._default)
            self.set_x_pos(self.get_x_pos() + 1)
            self._map.set_point(self.get_x_pos(), self.get_y_pos(), "@")

async def main():
    print("client main")
    server = "https://9999-green-tarsier-beurmlis.ws-us15.gitpod.io/"
    map = core.Map(20, 5)
    player = Player("player", 2, 2, map)
    map.actors.append(player)
    map.set_point(player.get_x_pos(), player.get_y_pos(), player._char)
    os.system('cls' if os.name=='nt' else 'clear')

    async def iteration():
        print(map.get_map())
        map.turn()
        os.system('cls' if os.name=='nt' else 'clear')
    
    while True:
        await iteration()
        print(await client.sync(server, jsonpickle.encode(map.get_map)))
        try:
            server_map = jsonpickle.decode(await client.sync(server, {"map":map.get_map()}))
        except Exception as e:
            print(f"Error, cannot connect to server:     {e}")