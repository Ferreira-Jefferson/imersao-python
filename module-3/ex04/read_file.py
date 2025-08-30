import sys

def read_file(file_name: str) -> None:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IsADirectoryError:
        print("Erro: O argumento enviado é um diretório.")
    except Exception as err:
        print(f"Erro inesperado: {type(err).__name__}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        read_file(file_name)
        