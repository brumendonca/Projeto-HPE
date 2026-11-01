from jinja2 import Environment, FileSystemLoader

# 1. Dados Estruturados: David Ricardo
dados = {
    "autor": {
        "nome": "David Ricardo",
        "periodo": "1772 – 1823",
        "escola": "Economia Política Clássica (Escola Ricardiana)",
        "resumo": (
            "Economista e corretor da Bolsa de Londres, Ricardo levou a economia clássica ao rigor "
            "do método dedutivo-analítico. Enquanto Adam Smith investigava a causa do enriquecimento "
            "das nações, Ricardo estabeleceu como problema central da economia a distribuição do produto "
            "social entre as três classes: proprietários de terras (renda), capitalistas (lucro) e trabalhadores (salário)."
        ),
    },
    "obras": [
        {
            "titulo_curto": "Ensaio sobre os Lucros",
            "titulo": "Ensaio sobre a Influência do Baixo Preço do Cereal sobre os Lucros do Capital",
            "ano": "1815",
            "visao_geral": (
                "Panfleto econômico decisivo redigido durante o debate parlamentar das Leis dos Cereais (Corn Laws). "
                "Aqui Ricardo constrói o 'modelo do cereal' (corn model), articulando a fertilidade decrescente do solo, "
                "a determinação da renda da terra na margem e a compressão da taxa geral de lucros da economia."
            ),
            "pontos_centrais": [
                {
                    "termo": "Rendimentos Decrescentes na Agricultura",
                    "explicacao": (
                        "Com o crescimento populacional, terras progressivamente menos férteis ou mais distantes "
                        "são postas em cultivo, exigindo mais trabalho por saca de cereal colhida."
                    ),
                },
                {
                    "termo": "Renda Diferencial da Terra",
                    "explicacao": (
                        "A terra intramarginal (mais fértil) gera uma renda fundiária equivalente à diferença entre "
                        "o seu custo de produção e o custo da terra menos fértil em uso (terra marginal, que não paga renda)."
                    ),
                },
                {
                    "termo": "Queda da Taxa de Lucro e Estado Estacionário",
                    "explicacao": (
                        "Cereal mais caro encarece o salário de subsistência. Como o salário real em termos de bens-salário "
                        "é constante, o salário nominal sobe, comprimindo diretamente o lucro dos capitalistas — o que paralisa a acumulação."
                    ),
                },
            ],
            "refutacao": (
                "Ricardo visava refutar frontalmente o protecionismo agrário dos proprietários de terras britânicos e a defesa "
                "feita por Thomas Malthus das Corn Laws. Ricardo defendia o livre comércio agrícola para baratear os alimentos "
                "e restaurar as margens de lucro do capital produtivo."
            ),
        },
        {
            "titulo_curto": "Princípios de Economia",
            "titulo": "Princípios de Economia Política e Tributação",
            "ano": "1817",
            "visao_geral": (
                "A obra magna ricardiana. Nela, o autor formaliza a teoria do valor-trabalho incorporado, analisa o impacto "
                "da mecanização sobre o emprego, detalha a incidência de impostos e formula a célebre teoria das vantagens comparativas."
            ),
            "pontos_centrais": [
                {
                    "termo": "Teoria do Valor-Trabalho Incorporado",
                    "explicacao": (
                        "O valor de troca de mercadorias reproduzíveis decorre da quantidade relativa de trabalho "
                        "necessária para produzi-las (direto e indireto/passado, incorporado em máquinas), corrigindo "
                        "a teoria aditiva de custos de Adam Smith."
                    ),
                },
                {
                    "termo": "Vantagens Comparativas",
                    "explicacao": (
                        "O comércio internacional é vantajoso mesmo se um país for menos eficiente na produção de todos os bens "
                        "(exemplo clássico: tecidos da Inglaterra e vinho de Portugal). O que determina a especialização "
                        "são os custos de oportunidade relativos internos, e não a vantagem absoluta smithiana."
                    ),
                },
                {
                    "termo": "Equivalência Ricardiana",
                    "explicacao": (
                        "A tese de que o financiamento de gastos públicos via endividamento ou via tributos presentes "
                        "possui o mesmo efeito macroeconômico a longo prazo, pois agentes racionais antecipam tributos futuros."
                    ),
                },
                {
                    "termo": "Capítulo 31: Sobre a Maquinaria",
                    "explicacao": (
                        "Revisão corajosa de sua própria postura: Ricardo admite que a introdução rápida de maquinário "
                        "pode destruir o fundo de salários no curto prazo e gerar desemprego tecnológico transitório."
                    ),
                },
            ],
            "refutacao": (
                "Refutou Adam Smith quanto à determinação dos preços por 'soma de componentes' (salário + lucro + renda), "
                "mostrando que a renda da terra não compõe o preço (ela é um resíduo diferencial); refutou as teses malthusianas "
                "de 'superprodução geral' (adotando a Lei de Say); e superou a dependência exclusiva de vantagens absolutas no comércio exterior."
            ),
        },
        {
            "titulo_curto": "Controvérsia do Bulhão",
            "titulo": "O Alto Preço do Bulhão: Uma Prova da Depreciação das Notas Bancárias",
            "ano": "1810",
            "visao_geral": (
                "Ensaio monetário publicado durante as Guerras Napoleônicas, no auge da suspensão de convertibilidade "
                "das notas do Banco da Inglaterra em ouro (1797-1821)."
            ),
            "pontos_centrais": [
                {
                    "termo": "Postura Bulionista (Bullionist)",
                    "explicacao": (
                        "Defesa da teoria quantitativa da moeda: o prêmio do ouro sobre a libra papel e a taxa de câmbio "
                        "depreciada eram sintomas incontestáveis de emissão excessiva de notas de papel sem lastro."
                    ),
                },
                {
                    "termo": "Regra Metálica Automática",
                    "explicacao": (
                        "A circulação de notas deve ser rigorosamente atrelada ao fluxo de reservas metálicas para conter pressões inflacionárias."
                    ),
                },
            ],
            "refutacao": (
                "Refutou a corrente 'anti-bulionista' e os diretores do Banco da Inglaterra, que alegavam que a depreciação "
                "da libra decorria de déficits na balança comercial causados por despesas bélicas e subsídios no continente, "
                "e não de políticas discricionárias de expansão creditícia."
            ),
        },
    ],
}

# 2. Renderização do Template
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.html")
html_gerado = template.render(dados)

# 3. Exportação para index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_gerado)

print("index.html gerado com sucesso para David Ricardo!")