from aiohttp import web

# Define routes
BotzPW = web.RouteTableDef()

@BotzPW.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("hello world")

# Create the web server
async def web_server():
    web_app = web.Application(client_max_size=30 * 1024 * 1024)  # 30 MB size limit
    web_app.add_routes(BotzPW)  # Add routes to the app
    return web_app
