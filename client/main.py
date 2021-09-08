import core

def main():
    print("client main")
    map = core.map.Map(20, 5)
    print(map.get_map())
    map.set_point(0,0,"@")
    print(map.get_map())