from aiohttp import web
import jsonpickle
import core, server

def main():
    map = core.Map(10, 10, "#")
    
    routes = web.RouteTableDef()

    @routes.post("/")
    async def receive_sync(request):
        data = (await request.post())["map"]
        print(data)
    
    @routes.get("/")
    async def respond_sync(request):
        data = {"map":jsonpickle.encode(map)}
        return web.json_response(data)
    
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=9999)