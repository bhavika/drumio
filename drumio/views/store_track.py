import os
import uuid
import shutil
from pyramid.response import Response
from pyramid.view import view_config
from drumio.lib.ssplit import split_track


@view_config(route_name="store_track", renderer="../templates/process.mako")
def store_track(request):
    filename = request.POST["track"].filename
    track_data = request.POST["track"].file

    # we should not use '/tmp' in production and protect against symlink attacks here
    file_location = os.path.join("/tmp", "{}.track".format(uuid.uuid4()))

    temp_file_path = file_location + "~"

    track_data.seek(0)
    with open(temp_file_path, "wb") as output_path:
        shutil.copyfileobj(track_data, output_path)

    os.rename(temp_file_path, file_location)
    destination_dir = split_track(track_input=file_location, stem_count=4)

    stems = shutil.make_archive(destination_dir, "zip", destination_dir)

    return Response(f"OK {stems}")
