"""
Yaml handling, file copying
"""
import re
import sys
import tempfile
from ruamel import yaml


def round_trip(output_stream, input_stream, custom_width=None, version=None, indent=None) -> None:
    loaded_yaml = yaml.round_trip_load(input_stream)
    yaml.round_trip_dump(
        loaded_yaml,
        output_stream,
        width=custom_width,
        version=(1, 1) if version else None,
        explicit_start=True,
        indent=indent,
        block_seq_indent=indent,
    )


def format_and_write(file, width, version, ansible) -> None:
    with tempfile.NamedTemporaryFile(mode="w") as temporary_file:
        with open(file, "r") as stream_input:
            round_trip(temporary_file, stream_input, width, version)
        with open(temporary_file.name) as rf, open(file, "w") as stream_out:
            yaml_formatted = rf.read()
            if ansible:
                yaml_formatted = "\n\n- name".join(yaml_formatted.split("\n- name"))
                yaml_formatted = re.sub("[\n]{2,}", "\n\n", yaml_formatted)
            stream_out.write(yaml_formatted)


def format_and_display(file, width, version, ansible) -> None:
    with open(file, "r") as sin:
        round_trip(sys.stdout, sin, width, version)
