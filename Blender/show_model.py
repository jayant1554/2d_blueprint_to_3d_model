import bpy
import os
import sys

if __name__ == "__main__":
    argv = sys.argv

    input_path = argv[5]
    bpy.ops.wm.open_mainfile(filepath=input_path)

    format = argv[6]
    output_path = argv[
        7
    ]  # strict argc==5 -> len=6 will be used as argument see Reformat_blender_to_obj.py

    # Must exit with 0 to avoid error!
    exit(0)
