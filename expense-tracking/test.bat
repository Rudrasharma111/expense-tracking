@echo off
docker-compose run --rm app pytest %*
exit /b

#"./test.bat test"