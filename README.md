# StandStack
Una Api-Rest que permite exponer productos y realizar ordenes.

## Para correr el proyecto, ejecute:
+ Clone el proyecto
    ```bash
    git clone https://github.com/Julian-Bio0404/StandStack.git
    ```
+ En la raíz del proyecto, instale las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
    
+ Levantar el servidor:
    ```bash
    py manage.py runserver
    ```

## Documentacion de la API:
Desde un cliente como Postman, puede:
1. Listar los Stands disponibles, metodo = GET
    ```bash
    http://localhost:8000/stands/
    ```

2. Ir al detalle de un Stand, metodo = GET:
    ```bash
    http://localhost:8000/stands/1/
    ```

3. Listar los productos de un stand, metodo = GET:
    ```bash
    http://localhost:8000/stands/1/products/
    ```

4. Ir al detalle de un producto, metodo = GET:
    ```bash
    http://localhost:8000/stands/1/products/1/
    ```

5. Listar las opciones disponibles de un producto, metodo = GET:
    ```bash
    http://localhost:8000/stands/1/products/1/options/
    ```
    
6. Ordenar un producto, metodo = POST
    ```bash
    http://localhost:8000/stands/1/products/1/order/
    ```

    request-body:
    ```bash
        {
            "option": "M"
        }
    ```