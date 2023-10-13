import argparse
from pathlib import Path
from packaging.version import parse as parse_version
from sh import wget, tar, python, find
from shutil import copytree, rmtree

parser = argparse.ArgumentParser()
parser.add_argument("version")


if __name__ == "__main__":
    args = parser.parse_args()

    base = Path(__file__ + "/../" + args.version).resolve()
    if base.is_dir():
        rmtree(base)
    base.mkdir(exist_ok=True)

    multipy = parse_version(args.version) < parse_version("3.3")

    if multipy:
        py2 = base / "py2"
        py3 = base / "py3"
        py2.mkdir()
        unpack = py2
    else:
        unpack = base

    url = f"https://github.com/OSGeo/gdal/archive/v{args.version}.tar.gz"

    if parse_version(args.version) < parse_version("3.5"):

        tar(
            wget(url, "-O", "-"),
            "xz", "--strip-components=4", "-C", str(unpack),
            f"gdal-{args.version}/gdal/swig/python")
    else:

        tar(
            wget(url, "-O", "-"),
            "xz", "--strip-components=3", "-C", str(unpack),
            f"gdal-{args.version}/swig/python")

    
    for d in ("samples", "scripts", "gdal-utils"):
        if (unpack / d).is_dir():
            rmtree(unpack / d)
    find(str(unpack), "-maxdepth", "1", "-type", "f", "-delete")

    if multipy:
        copytree(unpack / "extensions", base / "extensions")
        rmtree(unpack / "extensions")
        copytree(unpack, py3)
        python(
            "-m", "lib2to3", "-w", "-n",
            "-f", "import", "-f", "next",
            "-f", "renames", "-f", "unicode",
            "-f", "ws_comma", "-f", "xrange",
            str(py3))

    (base / 'GDAL_VERSION').write_text(args.version)
    for s in ("setup.py", "MANIFEST.in", "README.md"):
        (base / s).symlink_to("../" + s)
