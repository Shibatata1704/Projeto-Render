# Projeto-Render

Este projeto tem como objetivo analisar anúncios de veículos usados, investigando os principais fatores que influenciam o preço de mercado e o tempo de permanência dos anúncios. O conjunto de dados passou por um processo completo de limpeza, tratamento, enriquecimento e análise exploratória, assegurando consistência, qualidade e confiabilidade para a extração de insights relevantes.

- Tratamento de valores ausentes
    - model_year: valores ausentes foram preenchidos com a mediana do ano do modelo para veículos do mesmo model, preservando coerência temporal.

    - cylinders: valores ausentes foram preenchidos com a moda do número de cilindros por model, garantindo consistência entre veículos equivalentes.

    - odometer: valores ausentes foram preenchidos com a mediana da quilometragem por model_year, reduzindo o impacto de valores extremos.

    - paint_color: valores ausentes foram substituídos pela categoria explícita "unknown".

    - is_4wd: valores ausentes foram interpretados como veículos sem tração 4x4 e preenchidos com 0.


URL do aplicativo no Render: https://projeto-render-q2ji.onrender.com