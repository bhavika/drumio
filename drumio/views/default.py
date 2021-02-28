from pyramid.view import view_config


@view_config(route_name="process", renderer="../templates/process.mako")
def process_song_view(request):
    return {"ui": "process"}
