Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... R_EATING = "I don't like eating anything because I'm a bot obviously!"
... R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
... 
... 
... def unknown():
...     response = ["Could you please re-phrase that? ",
...                 "...",
...                 "Sounds about right.",
...                 "What does that mean?"][
...         random.randrange(4)]
