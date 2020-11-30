#!/usr/bin/env python3

import argparse
import logging
from pathlib import Path
import gspread
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS = Path.home()/'credentials_polemica.json'
SHEET_NAME='Noticias Polémica'
WKS_NAME='S04E02'

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

def loglevel_validator(v):
    """Validate selected log level. Return v.upper() or raise an error."""
    if v.upper() not in ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']:
        raise argparse.ArgumentTypeError('Log level must be a valid Python ' +
                                         'log level. See -h for details.')
    else:
        return v.upper()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=f'Scrapper de Polémica sheets a markdown v0.1')
    parser.add_argument('-l', '--log-level',
                        metavar='level',
                        type=loglevel_validator,
                        default='INFO',
                        help='El log level. Puede ser cualquiera de los' +
                        ' niveles estándares de Python: CRITICAL, ERROR, ' +
                        'WARNING, INFO, DEBUG.')
    parser.add_argument('-a', '--auth',
                        metavar='auth',
                        default=CREDENTIALS,
                        help=f'Path opcional al json de credenciales para ' +
                        f'gsheets. Default: {CREDENTIALS}.')
    parser.add_argument('-s', '--sheet',
                        metavar='sheet',
                        default=SHEET_NAME,
                        help=f'La sheet principal para sacar la información. ' +
                        f'Default: {SHEET_NAME}.')
    parser.add_argument('-w', '--worksheet',
                        metavar='worksheet',
                        default=WKS_NAME,
                        help=f'La worksheet ("tab") a procesar. Default: ' +
                        f'{WKS_NAME}.')
    parser.add_argument('-r', '--range',
                        metavar='range',
                        required=True,
                        help='El range de celdas con las noticias, en formato' +
                        ' ColumnaFila:ColumnaFila (p/ej: A1:C23).')
    parser.add_argument('-d', '--destination',
                        metavar='destination',
                        help='Si se especifica, path a un file en donde ' +
                        'escribir el markdown resultante. Si no, se escribe ' +
                        'a stdout.')
    args = parser.parse_args()
    if args.log_level == 'DEBUG':
        extra_log_fields = '- %(filename)s:%(lineno)s '
    else:
        extra_log_fields = ''
    logformat = f'%(asctime)s - %(name)s - %(levelname)s {extra_log_fields}- %(message)s'
    logging.basicConfig(level=args.log_level, format=logformat)
    logger = logging.getLogger('polemica_scrapper')
    credentials_path = args.auth
    sheet_name = args.sheet
    wks_name = args.worksheet
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    gc = gspread.authorize(credentials)
    try:
        sh = gc.open(sheet_name)
    except gspread.exceptions.SpreadsheetNotFound:
        logging.error(f'No existe el documento {sheet_name}.')
    try:
        wks = sh.worksheet(wks_name)
    except gspread.exceptions.WorksheetNotFound:
        logging.error(f'No existe la hoja {wks_name}.')
    cells = wks.batch_get([args.range])
    content = ""
    for row in cells[0]:
        print(row)
        url = row[4].strip().split(' ')[0]
        if row[0] == '1':
            try:
                title = row[5]
            except IndexError:
                title = ''
                logging.warning(f'La noticia de {row[1]} {url}  no tiene ' +
                                'título.')
            try:
                description = row[6]
            except IndexError:
                description = ''
                logging.warning(f'La noticia de {row[1]} {url} no tiene ' +
                                'descripción.')
            content += f'### [- {title} ]({url}) \n {description}\n\n'
    if args.destination:
        with open(args.destination, 'w') as file_:
            file_.write(content)
    else:
        print(content)
