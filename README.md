# cicd-lab1
**Простий FastAPI проект на Python, який реалізує CRUD операції**  
Щоб запеустити Docker контейнер потрібно:  
1. Створити зібрати контейнер:  
   ```docker build -t fastapi-lab1 .```  
2. Запустити контейнер:  
   ```docker run -d -p 8000:8000 --name lab1-app fastapi-lab1```
    
Щоб запустити тести треба виконати:  
```docker exec -it lab1-app python -m pytest```  
