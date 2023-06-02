import tarfile
import os.path
from pathlib import Path

targets = [
    "calibre",
    "gitea",
    "gitea-act",
    "drone",
    "n8n",
    "pihole",
    "jellyfin",
]

source = Path("/source")
dest = Path("/destination")


def make_tarfile(output_filename: Path, source_dir: Path):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def main():
    for target in targets:
        print(f"Start {target}")
        make_tarfile(dest / f"{target}.tar.gz", source / target)
        print(f"Finish {target}")


if __name__ == "__main__":
    main()
