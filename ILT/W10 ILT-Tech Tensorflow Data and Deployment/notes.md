### Is it Enough to have Model Running on the Jupyter Notebook?
Not enough, because we cannot serve it to web services.

## Lifecycle of ML Project
- Project Planning
Decide problem, Define goals and requirm, dan Allocate Resources

- Data Collection and Labelling
Kredibilitas data di industri sangat penting. Kita perlu memahami data sebelum masukin ke ML model

- Model Training and Debugging
Dapetin baseline model secepatnya. Lalu baru kita debug dan update processnya.
Debug ML itu beda. ML itu perlu ngedebug datanya, mastiin data yang kita punya itu high quality.
Audit check, untuk melihat model yang dibuat sesuai dengan industry standar.

- Deployment and Monitoring
Software into production. Kita naruh model ke production.
Kita buat software untuk mastiin model nya berjalan dan membuat prediksi.

## ML Objectives vs Business Objectives
Bisnis, itu dia cuma care sama cost, investment, regulasasia, ROI, dll.

Bagaimana mempertemukan ML objective dan Bisnis objective?
### Challenges of Model Deployment
- ML itu sensitif terhadap data yang datang. Datanya harus terstandarisasi. 
- The performance ML models will `degrades` overtime, due to changes in real data. Retraining ya
- Locality, ML model only works from spesific demographic.

## Model Deployment Options
- Centralized model in Server
- Distribute model on User Device

Tensorflow provide tools TFJS, TFLite, TFServing, tentu ada consideration before deploying speerti complexity, computing power, dsbg.

## Tensorflow JS
We can run in client model or server js.
Open-source, can deploy in Client's broswer or Node.js server.
- Run existing model
- Retrain existing model
- Develop ML with Javascript

## General Steps n Tensorflow JS
- Build Model  : Disini juga testing
- Save Model : Bisa .h5 format
- Convert : Convert ke JSON format
- Deploy 

## Converting Models into JSON Format
Kita make .h5, ada di Screenshot caranya.

## What Can Tensorflow.JS Do?
<https://teachablemachine.withgoogle.com/train>

## Beberapa article MLOps
> https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
> https://ml-ops.org/content/mlops-principles

## Tensorflow Lite
Run TensorFlow Models on Device
- Optimized on device ML
- Multiple platform support
Bisa di run di Android and IOS,
- Diverse language support
Dia support Java, C++, Kotlin
- Hardware acceleration and Model Optimization
Semisal di embedded system, ada hardware acceleration, bisa manfaatin itu.

## Challenges of on-Device model
- Handle Diverse Devices
- We do not have access to the actual data
- Need  to balance between : power effeciency, inference latency, model accuracy and complexity

Step untuk deploy TFLite nya itu sama kyk sebelumnya.
Tapi Convert nya bisa di convert ke TFLite model.

## TensorFlow Serving
Serving sistem, untuk nge-serve ML model. Dia ni flexible dan high-performance, for production.

TF ini mudah di extend, support banget sama TF Model. Ada beberapa hal tapi yang perlu di atur.

Model nya bakal running di central location, 
servernya yang execute requestprediksi dari kita. 
- Easy to manage model version, hardware resources
- Can have multiple serving processes. Misal request nya ada puluhan ribu, kan gamungkin di 1 server. Bisa ada beberapa server gitu. Untuk ngatur kemana? Itu pake load balancing. 

Untuk deploy model, kita make Docker Image (disarankan).

## What is Container/Docker
Standard unit of software, that packages code dengan semua depedencies nya.
Bagusnya? 
- Portable : Di bundle, bisa running di multiple platform. Selama env itu support Docker
- Lightewight : Karena dia host OS nya di host, ukurannya kecil.
- Isolation : Container punya own network. Bakal di isolasi. Punya resourcenya sendiri. 
Enable to deploy multiple app, in a single OS. Kita gaperlu musingin tentang OS, hanya fokus ke APP saja.


TF Serving expect input dalam JSON Format

## Serve ML model on GCP
Provides multiple ways for deploying inference in the Cloud
Kita bisa make Cloud Run.

## Data Pipelines
Memindahkan data, ke data yg lain gitu. Biasanya dipake ke warehouse gitu.
Basically automated process of ETL. Extract Transform Load.

- Extract : System will gather raw data, from DB and etc. Then the system starts reading, and through the transform process.
- Transform : Set of function are applied to the extracted data, to a single standard data format. Di normalisasi dan standardisasi gitu. Ada filtering, cleaning, sorting, dsbg.  
- Load : Clean datanya di transfer ke final destination/target system. Bisa ke warehouse, atau sistem machine learning.

Tensorflow provide tools for ETL
## Tensorflow Datasets
TFDS is a tool to build the ETL process with a conssitent API.
Dia ada koleksi public dataset yang bisa dipakai untuk latihan. 

ELT : alternative form. Data will store original data. Kalo ETL kan transform dulu baru di load. Kebalikannya, di load dulu, baru di transform. Mempercepat proses loading. 

## Federated Learning
Allows each client to independently train its own model using its own data right on the device.

Tiap klien bisa ngetrain modelnya, dengan data mereka sendiri. 
- Low Latency, Less Power Consumption, Ensuring Privacy

Your client can personalize the model. Belajar behavior dari usernya gitu. 

## Tensorflow Federated
Provide computation on Decentralized Data.
- FL API (L for Learning)
- FC API (C for Core)

Collaboration between data engineers, data analysts and data scientists: <https://medium.com/dailymotion/collaboration-between-data-engineers-data-analysts-and-data-scientists-97c00ab1211f>
<https://www.freecodecamp.org/news/scalable-data-analytics-pipeline/>

## Federated
<https://www.tensorflow.org/federated/get_started>


## MLOps
Intro to MLOps: ML Technical Debt: 
<https://towardsdatascience.com/intro-to-mlops-ml-technical-debt-9d3d6107cd95>

Intro to ML Ops: Tensorflow Extended (TFX): 
<https://towardsdatascience.com/intro-to-ml-ops-tensorflow-extended-tfx-39b6ab1c7dd7>

The TFX User Guide: 
<https://www.tensorflow.org/tfx/guide>

