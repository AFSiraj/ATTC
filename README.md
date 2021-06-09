# Repository for Bangkit Capstone Project of ATTC (Advanced Technology for Traditional Cake)
Mentored by Vincent Tatan

An android app using machine learning to identified traditional cake by image that user sent to the server and returning what cake it is and what packaging that cake usually use.

# Tech Stack
- Machine Learning -> Tensorflow
- Android -> Kotlin
- Cloud -> Flask, Docker, Google Cloud Run



# Android Path

This File Project Of Advanced Technology for Traditional Cake

Software :  
Android Studio (Version - 4.1.1)  
Insomnia (Version - 2021.3.0)

### Gradle
For user permission
```bash
implementation 'com.karumi:dexter:6.2.2'
```
For coiling image
```bash
implementation("io.coil-kt:coil:1.1.1")
```
For Internet Connection (API)
```bash
implementation 'com.squareup.retrofit2:retrofit:2.9.0'
implementation 'com.squareup.retrofit2:converter-gson:2.9.0'
```

For UI
```bash
implementation 'androidx.appcompat:appcompat:1.3.0'
implementation 'com.google.android.material:material:1.3.0'
implementation 'androidx.constraintlayout:constraintlayout:2.0.4'
implementation 'com.google.android.material:material:1.3.0-alpha03'
implementation 'com.github.armcha:SpaceNavigationView:1.6.0'
implementation 'androidx.navigation:navigation-fragment-ktx:2.3.5'
implementation 'androidx.navigation:navigation-ui-ktx:2.3.5'
```

### Preview Apps
<img src="https://user-images.githubusercontent.com/29168567/121363635-54ffe800-c961-11eb-8fd6-9a1c71bf27fc.jpeg" width="150" />  <img src="https://user-images.githubusercontent.com/29168567/121363683-5d582300-c961-11eb-9efc-3de4e54c758e.jpeg" width="150" />  <img src="https://user-images.githubusercontent.com/29168567/121363727-65b05e00-c961-11eb-99d7-30e0b0a67c7f.jpeg" width="150" />  <img src="https://user-images.githubusercontent.com/29168567/121363738-6943e500-c961-11eb-8db1-1c75c3ebe274.jpeg" width="150" />  <img src="https://user-images.githubusercontent.com/29168567/121363759-6d700280-c961-11eb-8c79-b9db7a208c40.jpeg" width="150" />  <img src="https://user-images.githubusercontent.com/29168567/121363775-71038980-c961-11eb-860c-fc577f31948d.jpeg" width="150" />


# Cloud Path

## ATTC Model Deployment on Google Cloud Run

deploying machine learning model using Flask framework into Google Cloud Run

Prerequisite (Git Clone)

- main.py (Flask App)
- traditional_cake.h5 (Keras Machine Learning Model)
- Dockerfile
- requirements.txt

---

## To run locally

```bash
python3 main.py
```

The flask server will be served on `port 5000`

## Deployment to Google Cloud Run

```bash
gcloud auth login
```

```bash
gcloud auth configure-docker
```

### Docker Build (make sure Run Docker first)

```bash
docker build -t gcr.io/<PROJECT-ID>/<CONTAINER-NAME>:<TAG> .
```

```bash
docker push gcr.io/<PROJECT-ID>/<CONTAINER-NAME>:<TAG>
```

### Deploy to Cloud Run

```bash
gcloud run deploy --image gcr.io/<PROJECT-ID>/<CONTAINER-NAME> --port 5000
```

### Deploy updates (if any)
1. Run docker build steps again
2. Go to Cloud Run page
3. Select your instance (bangkit-ml-deployment)
4. Click on `EDIT & DEPLOY NEW VERSION`
5. Select the newly pushed container
6. Click on `DEPLOY`

## Usage

Endpoint

```bash
https://bangkit-ml-deployment-mxcyue5puq-et.a.run.app/predict
```

form-data

```
image : image.jpg
```

Return

```bash
{
    "filename": "download.jpg",
    "prediction": "kue_putri_salju",
    "success": true,
}
```

