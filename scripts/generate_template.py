import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--project_type", type=str, default="investigation", help="investigation, notebooks, application, spaces")
parser.add_argument("--project_name", type=str, default="test")
args = parser.parse_args()

data_dir = f"{args.project_type}/{args.project_name}"
os.makedirs(data_dir + "/images", exist_ok=True)
os.makedirs(data_dir + "/results", exist_ok=True)

if args.project_type != "spaces":

    commands_line = [
        f"cp basedocs/README.md {data_dir}",
        f"cp basedocs/Docs.md {data_dir}",
    ]

    for cmd in commands_line:
        subprocess.call(cmd, shell=True)
else:
    commands_line = [
        f"cp basedocs/Tutorial.md {data_dir}",
    ]

    for cmd in commands_line:
        subprocess.call(cmd, shell=True)



