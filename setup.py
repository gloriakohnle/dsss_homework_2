from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Paketname
    version="0.1",
    author="Gloria Kohnle",
    author_email="gloria.r.kohnle@fau.de",
    description="Math Quiz",
    packages=find_packages(),  # Findet alle Pakete automatisch
    install_requires=[  # Optionale Abhängigkeiten
        # Liste hier Abhängigkeiten auf, die beim Installieren mitgeladen werden sollen
    ],
)
