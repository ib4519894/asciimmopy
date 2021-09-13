from aiohttp import web
import jsonpickle
import core, server

def main():
    map = core.Map(10, 10, "#")
    
    routes = web.RouteTableDef()
    
    @routes.get("/")
    async def get_sync(request):
        data = {"map":jsonpickle.encode(map)}
        return web.json_response(data)
    
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=9999)