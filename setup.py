from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Paketname
    version="0.1",
    author="Gloria Kohnle",
    author_email="gloria.r.kohnle@fau.de",
    description="Math Quiz",
    packages=find_packages(),  # Findet alle Pakete automatisch
    install_requires=[  # Optionale Abhängigkeiten
    ],
    python_requires=">=3.9",
    entry_points = {
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz", # Pfad zu math_quiz-Funktion in der math_quiz.py
        ]
    }

)
