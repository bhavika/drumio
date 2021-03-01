from spleeter.separator import Separator
import os

OUTPUT_DIR = "processed"


def split_track(track_input, stem_count):
    fname = os.path.basename(track_input)

    track_stems_output = os.path.join("/tmp", OUTPUT_DIR, fname)

    if stem_count in [2, 4, 5]:
        separator = Separator(f"spleeter:{stem_count}stems")

    separator.separate_to_file(
        audio_descriptor=track_input, destination=track_stems_output, synchronous=True
    )

    return track_stems_output
