# polemica_scrapper
Tool para parsear la spreadsheet de Polémica en /var a Markdown.

## Requerimientos

- Python 3.7
- oauth2client
- gspread
- Credenciales con permisos para acceder a la spreadsheet.
- Archivo de credenciales bajado de la dashboard de Google, formato json.

## Setup

La mejor forma de usarlo es mediante un virtualenv:

~~~
$ virtualenv -p python3.7 ~/venv/
$ source ~/venv/bin/activate
$ pip install -r requirements.txt
~~~

## Uso

~~~
$ ./polemica_scrapper.py --help
usage: polemica_scrapper.py [-h] [-l level] [-a auth] [-s sheet]
                            [-w worksheet] -r range [-d destination]

Scrapper de Polémica sheets a markdown v0.1

optional arguments:
  -h, --help            show this help message and exit
  -l level, --log-level level
                        El log level. Puede ser cualquiera de los niveles
                        estándares de Python: CRITICAL, ERROR, WARNING, INFO,
                        DEBUG.
  -a auth, --auth auth  Path opcional al json de credenciales para gsheets.
                        Default: /home/usuario/credentials_polemica.json.
  -s sheet, --sheet sheet
                        La sheet principal para sacar la información. Default:
                        Noticias Polémica.
  -w worksheet, --worksheet worksheet
                        La worksheet ("tab") a procesar. Default: S04E02.
  -r range, --range range
                        El range de celdas con las noticias, en formato
                        ColumnaFila:ColumnaFila (p/ej: A1:C23).
  -d destination, --destination destination
                        Si se especifica, path a un file en donde escribir el
                        markdown resultante. Si no, se escribe a stdout.
~~~

El script tiene varios valores en default, que pueden cambiarse. El único que es obligatorio de especificar es el rango, con -r/--range.

## Autores

* [Juan Manuel Santos (godlike)](https://github.com/godlike64)

