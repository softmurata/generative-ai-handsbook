import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--project_type", type=str, default="investigation", help="investigation, notebooks, application")
parser.add_argument("--project_name", type=str, default="test")
args = parser.parse_args()

subprocess.call(f"rm -rf {args.project_type}/{args.project_name}", shell=True)
