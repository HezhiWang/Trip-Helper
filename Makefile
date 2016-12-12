clean-pyc:
    find . -name '*.pyc' -exec rm --force {} +
    find . -name '*.pyo' -exec rm --force {} +
    find . -name '*~' -exec rm --force  {} +

test:
    python3 -m unittest discover

run: 
    python3 gui.py     
