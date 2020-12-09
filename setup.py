import os
from setuptools import setup

PACKAGE_NAME = "rrc_example_package"

setup(
    name=PACKAGE_NAME,
    version="2.0.0",
    # Packages to export
    packages=[PACKAGE_NAME],
    data_files=[
        # Include our package.xml file
        (os.path.join("share", PACKAGE_NAME), ["package.xml"]),
    ],
    # This is important as well
    install_requires=["setuptools"],
    zip_safe=True,
    author="Felix Widmaier",
    author_email="felix.widmaier@tue.mpg.de",
    maintainer="Felix Widmaier",
    maintainer_email="felix.widmaier@tue.mpg.de",
    description="Example package for the Real Robot Challenge Submission System.",
    license="BSD 3-clause",
    # Like the CMakeLists add_executable macro, you can add your python
    # scripts here.
    entry_points={
        "console_scripts": [
            "move_up_and_down = rrc_example_package.scripts.move_up_and_down:main",
            "random_motion_with_gym_env = rrc_example_package.scripts.random_motion_with_gym_env:main",
        ],
    },
)
