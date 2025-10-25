## create a new folder
mkdir fastapi-starter
cd fastapi-starter

## create a new virtual environment
python3 -m venv venv
source venv/bin/activate

## install dependencies
pip install fastapi uvicorn -- this is a server which runs ur weba app


🧩 Step 2: Create a Simple FastAPI App

fastapi-starter/
│
├── app/
│   ├── main.py            # entry point
│   ├── routers/
│   │   └── items.py       # modular API routes
│   ├── models/
│   │   └── item_model.py  # Pydantic models
│   └── services/
│       └── item_service.py # business logic
│
├── requirements.txt
└── README.md

## saves ur dependencies in requirements.txt just like maven
 pip freeze > requirements.txt


to run the application -- uvicorn is ur servver
uvicorn main:app --reload

## for documentation refer this 
http://127.0.0.1:8000/docs