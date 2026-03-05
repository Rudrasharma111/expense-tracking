@echo off
docker-compose run --rm app python app/main.py %*
exit /b

#"./start.bat ingest"
#"./start.bat analyze"
#"./start.bat analyze --month january"