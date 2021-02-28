import os
import uuid
import shutil
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name="store_track", renderer="../templates/404.mako")
def store_track(request):
    print(request)
    filename = request.POST["mp3"].filename
    track_data = request.POST["mp3"].file

    # we should not use '/tmp' in production and protect against symlink attacks here
    file_location = os.path.join("/tmp", "{}.mp3".format(uuid.uuid4()))

    temp_file_path = file_location + "~"

    track_data.seek(0)
    with open(temp_file_path, "wb") as output_path:
        shutil.copyfileobj(track_data, output_path)

    os.rename(temp_file_path, file_location)

    return Response("OK")
