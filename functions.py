
import logging
import logging.config
from pathlib import Path

# Configuro el logging
config_path = Path(__file__).parent / 'log_config_file.conf'
logging.config.fileConfig(fname=config_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def cantidades(data: str) -> int:
    # La funcion toma un objeto archivo y devuelve un 1 en caso de
    # ejecutarse correctamente Calcula la cantidad de renglones y la
    #  cantidad de palabras por cada renglon

    linea = 0
    palabras = 0
    df = data.read()
    # Separo el string por filas o saltos de lineas
    lineas = df.split('\n')
    logger.info(f"Cantidad de Renglones: {len(lineas)}")

    # Cuento la cantidad de palabras por cada linea
    for line in lineas:
        linea += 1
        palabras = len(line.split())
        logger.info(f"Renglon: {linea} Cantidad de palabras: {palabras}")
    return 1
