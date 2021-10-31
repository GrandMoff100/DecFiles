from setuptools import setup


setup(
    name="DecFiles",
    version="0.0.0",
    install_requires=["flask", "requests"],
    packages=["decfiles"],
    package_data={
        "decfiles/templates": ["*.html"]
    }
)