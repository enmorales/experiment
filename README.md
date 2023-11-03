## Configuración

```
python -m venv env
source env/Scripts/activate
```

## Crear Imágenes

```
chmod +x build_images.sh
./build_images.sh
```

## Levantar Microservicios

``` 
 docker compose -f docker-compose.yml up
```