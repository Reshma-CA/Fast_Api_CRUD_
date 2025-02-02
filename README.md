# CSV data to Database Uploader project

This project is a simple fast api CRUD project

Technologies Used:

Backend: python, Fast API.




##  1,  Create a virtual environment



```bash
python -m venv venv


```



##  2, Activate the virtual environment



```bash
venv\Scripts\activate


```

##  3, Install project dependencies



```bash
pip install fastapi uvicorn



```
##  4,Write a Simple FastAPI App



```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


```
##  5,  Run the FastAPI Server



```bash
uvicorn main:app --reload


```


##  6, Access the API
Once the server is running, open:

#### POST API

```http
API: http://127.0.0.1:8000/
Interactive Docs (Swagger UI): http://127.0.0.1:8000/docs
Redoc UI: http://127.0.0.1:8000/redoc
```

## Project API screen shots
![Image](https://github.com/user-attachments/assets/ef653264-c2cd-4000-90e8-cae392566bbe)




