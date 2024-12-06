# Repository for Text Emotion Detector Application
## employing the Watson NLP library
Change to project directory
```
cd final_project
```

Install the following dependencies inside your environment:
```
python3.11 -m pip install flask==2.2.2
python3.11 -m pip install pylint
python3.11 -m pip install requests
```

To run unit testing
```
python3.11 test_emotion_detection.py
```

to run static code anylysis
```
pylint server.py
```

To run server/application -- deployed on localhost:5000
```
python3.11 server.py
```
