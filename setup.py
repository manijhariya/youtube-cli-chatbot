from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="yt_chatbot",
    version="0.0.1",
    author="Manish Kumar",
    author_email="mannjhariya@gmail.com",
    license="MIT License",
    description="Build a CLI powered chatbot for YouTube that allows users to find videos, ask questions about the video and its content, and summarize the video.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/yt_chatbot",
    py_modules=["yt_chatbot", "app"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        yt_chatbot=src.main:main
    """,
)
