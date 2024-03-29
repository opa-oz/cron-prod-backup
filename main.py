import tarfile
import os.path
import time
import requests
from pathlib import Path

targets = [
    "calibre",
    "gitea",
    "jellyfin",
    "kuma",
]

source = Path("/source")
dest = Path("/destination")


def make_tarfile(output_filename: Path, source_dir: Path):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def main():
    for target in targets:
        start = time.time()
        print(f"Start {target}")
        make_tarfile(dest / f"{target}.tar.gz", source / target)
        print(f"Finish {target}: {time.time() - start}")

        ping_url = os.environ.get("PING_URL")

        if ping_url is not None:
            try:
                requests.get(ping_url)
            except:
                pass


if __name__ == "__main__":
    main()
