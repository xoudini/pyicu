import os
import pathlib
import typing as t


def _get_build_dir() -> pathlib.Path:
    return pathlib.Path(os.environ["_BUILD_DIR"])


def get_sources(root: str) -> t.Sequence[str]:
    pyicu = pathlib.Path(root).joinpath("pyicu").absolute()
    return list(map(str, pyicu.glob("**/*.cpp")))


def get_include_dirs(root: str) -> t.Sequence[str]:
    path = _get_build_dir().joinpath("include").absolute()

    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")

    return [str(path)]


def get_library_dirs(root: str) -> t.Sequence[str]:
    path = _get_build_dir().joinpath("lib").absolute()

    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")

    return [str(path)]


def get_libraries(root: str) -> t.Sequence[str]:
    # NOTE: manylinux
    return [
        "icudata",
        "icui18n",
        "icuuc",
    ]
    # TODO: fix for other platforms?
    return [
        "libicudata",
        "libicui18n",
        "libicuuc",
    ]


def get_extra_compile_args(root: str) -> t.Sequence[str]:
    VERSION = os.environ["PYICU_VERSION"]
    ICU_MAX_MAJOR_VERSION = os.environ["ICU_MAX_MAJOR_VERSION"]
    return [
        "-std=c++17",
        # TODO: pass to define_macros instead
        f'-DPYICU_VER="{VERSION}"',
        f'-DPYICU_ICU_MAX_VER="{ICU_MAX_MAJOR_VERSION}"',
    ]
