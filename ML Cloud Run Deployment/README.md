# ATTC Model Deployment on Google Cloud Run

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
