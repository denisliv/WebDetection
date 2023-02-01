<a href="https://github.com/denisliv"><img src="https://img.shields.io/static/v1?logo=github&label=maintainer&message=denisliv&color=ff3300" alt="Last Commit"/></a> 
<a href="https://github.com/denisliv/WebDetection/graphs/commit-activity"><img src="https://img.shields.io/github/last-commit/denisliv/WebDetection.svg?colorB=ff8000&style=flat" alt="Last Commit"/> </a>
<img src="https://img.shields.io/github/repo-size/denisliv/WebDetection.svg?colorB=CC66FF&style=flat" alt="Size"/>

# Yolov8 object detection model deployment using flask
This repo contains example app for exposing the [YOLOv8](https://github.com/ultralytics/ultralytics) object detection model via a [flask](https://flask.palletsprojects.com/en/2.2.x/).
## WebDetection
Simple app consisting of a form where you can upload an image, and see the inference result of the model in the browser.

<p align="center">
<img src="docs/app_form.jpg" width="450">
</p>

<p align="center">
<img src="docs/app_result.jpg" width="450">
</p>

Processed images are saved in the `static/results` directory with the original filename.

## Installation
### Clone repository and install requirements

```
git clone git@github.com:denisliv/WebDetection.git
cd WebDetection
pip install -r requirements.txt
```

## Usage
### Start the application

```$ python3 server.py --port 5000```

then visit [http://localhost:5000/](http://localhost:5000/) in your browser:

## Contacts:

[![LinkedIn](https://img.shields.io/static/v1.svg?label=connect&message=@denisliv&color=success&logo=linkedin&style=flat&logoColor=white&colorA=blue)](https://www.linkedin.com/in/denis-iv/)
