from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({
        "status": "success",
        "message": "Welcome to the @RDX_PVT_LTD Rename Bot service.",
        "developer": "@RDX_PVT_LTD"
    })


async def web_server():
    web_app = web.Application(client_max_size=30000000) # 30MB limit
    web_app.add_routes(routes)
    return web_app



## Fixed by @VoidZero_Dev ##
# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
## Fixed by @VoidZero_Dev ##
