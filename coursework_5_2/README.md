# SkyPro.Python course
## Course work №5. Skymarket

### Implementation

1. Backend: django restframework
2. Database: postgresql 
3. Backend-server: gunicorn
4. Web-server: nginx (from docker image)
5. Frontend: react (was provided)

frontend available at: localhost:3000  
backend at: localhost:8000

### How to launch project locally using docker for every service

Project is set to start all necessary docker containers and populate database from single command.  
Just perform the following command: `docker-compose up --build -d`

06.12.2022