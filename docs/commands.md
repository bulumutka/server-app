# Some commands

Starts docker image in background on sertain ports.
```
docker run -d --publish 5000:5000 app
```

Lists storages images.
```
docker images
```

Pull docker image using Docker hub.
```
docker pull mishasdk/app
```

Builds docker image.
```
docker build --tag app app/
```

Lists running images.
```
docker ps
```
