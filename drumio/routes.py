def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("process", "/")
    config.add_route("store_track", "/store_track")
