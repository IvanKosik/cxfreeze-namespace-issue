from cx_Freeze import setup


build_exe_options = {
    "excludes": [
        "regularpack.configs", "regularpack.models",
        "namespacepack.firstchildpack.configs", "namespacepack.firstchildpack.models",
        "namespacepack.secondchildpack.configs", "namespacepack.secondchildpack.models",
    ],
    "packages": ["regularpack", "namespacepack.firstchildpack", "namespacepack.secondchildpack"],
}


setup(
    name="Test",
    version="0.1",
    options={"build_exe": build_exe_options},
    executables=[
        {"target_name": "regularpack", "script": "regularpack/main.py"},
        {"target_name": "firstchildpack", "script": "namespacepack/firstchildpack/main.py"},
        {"target_name": "secondchildpack", "script": "namespacepack/secondchildpack/main.py"},
    ],
)
