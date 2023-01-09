# Face recognition using opencv
Real-time face recognition project with OpenCV and Python

## What to add in next versions
* add gopro as camera
* write docker image or python script to run on rasberry PI
* modificate `names related to id's: example ==> Sergey: id=1,  etc`... 
for example - enter name and this will be ID
* work with OS py lib - create and delete `dataset/` and `trainer/` directory
* ~~add delay in record for dataset~~

## face record dataset
Capture multiple faces from multiple users to be stored on a DataBase (dataset directory)

Take 20 screenshots and exited. Every screenshot will be taken every 2 seconds.

- Faces will be stored on a directory: `dataset/` (if it does not exist, need to create one)
- Each face will have a unique numeric integer ID as 1, 2, 3, etc
- Use `SPACE` key to take screenshoot and `Q` key to exited

## face id training
Training faces from `dataset/` dir and make .yml file with training model:
- Each face will have a unique numeric integer ID as 1, 2, 3 and etc
- Model will be saved on `trainer/` directory. (if it does not exist, need to create one)
- If need to using PIL, install pillow library with `pip install pillow`

# face record dataset
Real Time Face Recogition
- Each face stored on `dataset/` dir, should have a unique numeric integer ID as 1, 2, 3, etc
- trained faces model should be on `trainer/` dir
- use `ESC` key to exit