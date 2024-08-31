import json
import os

def ler_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return json.load(file)

def calcular_metricas(faturamento_diario):
    faturamentos_validos = [f['faturamento'] for f in faturamento_diario if f['faturamento'] > 0]

    if not faturamentos_validos:
        raise ValueError("Não há dados de faturamento válido para cálculo.")

    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)


    media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)

    dias_acima_media = sum(1 for f in faturamento_diario if f['faturamento'] > media_faturamento)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

def main():
    caminho_arquivo = os.path.join('calcpercentual', '3', 'faturamento.json') 
    try:
        dados = ler_dados_json(caminho_arquivo)
        faturamento_diario = dados.get('faturamento_diario', [])

        metricas = calcular_metricas(faturamento_diario)
        
        print(f"Menor valor de faturamento: {metricas['menor_faturamento']}")
        print(f"Maior valor de faturamento: {metricas['maior_faturamento']}")
        print(f"Número de dias com faturamento acima da média: {metricas['dias_acima_media']}")
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")

if __name__ == "__main__":
    main()
