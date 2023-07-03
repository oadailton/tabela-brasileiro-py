"""As bibliotecas para conectar ao site, separar a tabela e retirar informações irrelevantes"""
import re
import requests
import pandas as pd

def tabelabrasileiro(tipo, tempodeespera, time=0, info=None):
    """Aqui que o jogo começa."""
    try:
        url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a"
        response = requests.get(url, timeout=tempodeespera)
        cbf = response.text
    except requests.exceptions.RequestException as err:
        raise ValueError("Erro de conexão") from err
    tabela = pd.read_html(str(cbf))[0]
    brasileiro = tabela
    if tipo == 0:
        return repr(tabela)
    if tipo == 1:
        if time < 0 or time >= len(brasileiro):
            raise ValueError("Erro: não encontramos nenhum time nessa posição.")
        if info is not None:
            try:
                return brasileiro.iloc[time][info]
            except KeyError as err:
                aviso = "Não existe esse objeto na tabela, consulte a documentação!"
                raise ValueError(aviso) from err
        return brasileiro.iloc[time]
    if tipo == 2:
        if time < 0 or time >= len(brasileiro):
            raise ValueError("Erro: não encontramos nenhum time nessa posição.")
        return re.sub(r'[\dº]', "", brasileiro.iloc[time][0]).strip()
    raise ValueError("Você especificou um TIPO que não existe, experimente tentar 0; 1 ou 2.")
