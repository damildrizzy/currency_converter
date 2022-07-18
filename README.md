# Currencies converter REST service

### Features

* supports 170 forex currencies
* source data is fetched via [https://exchangerate.host](https://exchangerate.host)
* authentication

## Getting Started
### Prerequisites
* [Docker](https://docker.com)

### Installation
1. Clone the repo
   ```shell script
   git clone https://github.com/damildrizzy/currency_converter.git
   ```
2. Go to the project directory
   ```shell script
   cd currency-converter
   ```
3. Run the service
   ```shell script
   docker-compose up --build
   ```
4. The application should be running at http://127.0.0.1:8000/  
   
## Documentation
### OpenAPI schema

Go to `/openapi.json` to get the current OpenAPI JSON schema.
Or view already generated [openapi.json](openapi.json) in the repository.

### Interactive API documentation (provided by Swagger UI)

Go to `/docs` to see the automatic interactive API documentation.

### ReDoc

Go to `/redoc` to see the ReDoc documentation.



## Todo (If I had more time)
1. Write Tests
2. Decouple sqlalchemy orm from User model
3. Implement rate-limiting on historical data endpoint




