# Docker
Run docker image and connect with DB

# Docker
cd web-connect
docker build -t web-connect .
docker run --rm --name web -p 8080:8080 web-connect
