
import logging
import logging.config
from pathlib import Path
import functions


def main():
    # Ejecuta la lectura de un archivo cuento.txt 
    # al mismo se le contaran las lineas y la cantidad
    # de palabras en cada linea haciendo uso del modulo
    # funciones con la funcion cantidades
    config_path = Path(__file__).parent / 'log_config_file.conf'

    logging.config.fileConfig(fname=config_path,
                              disable_existing_loggers=False)

    print(__name__)
    logger = logging.getLogger(__name__)
    logger.info("...Leyendo el archivo...")
    try:
        with open('cuento.txt') as file:
            functions.cantidades(file)
        logger.info("...Archivo procesado...")

    except Exception as e:
        logger.error("No se pudo abrir el archivo")
        print(e)


if __name__ == '__main__':
    main()
