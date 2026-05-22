import streamlit as st
import pandas as pd
from src.charts import *
from src.utils import prepare_schooling_data

@st.cache_data
def load_data():
    gapminder = pd.read_csv('data/raw/gapminder_full.csv', sep=',', encoding='utf-8')
    hdi = pd.read_csv('data/raw/hdr-data.csv', sep=',', encoding='utf-8')
    
    return gapminder, hdi

def render_home():
    st.title("📊 Análise do Desenvolvimento Humano e Econômico Global")

    st.markdown("""
            ### Pós-Graduação em Inteligência Artificial e Aprendizado de Máquina  
            **Instituição:** PUC Minas  
            **Disciplina:** Python para Ciência de Dados  
            **Professor:** Leandro Figueira Lessa  

            ---

            ### Sobre o Projeto

            Este trabalho foi desenvolvido como parte das atividades da disciplina **Python para Ciência de Dados**, no curso de Pós-Graduação em **Inteligência Artificial e Aprendizado de Máquina da PUC Minas**.

            O projeto tem como objetivo realizar uma análise exploratória de dados (EDA) utilizando o dataset **Gapminder**, uma base amplamente utilizada em estudos de desenvolvimento global por reunir indicadores socioeconômicos e demográficos de diversos países ao longo de várias décadas.

            A análise busca investigar relações entre indicadores como:

            - **Expectativa de vida**
            - **PIB per capita**
            - **População**
            - **Desenvolvimento regional**
            - **Educação e desenvolvimento humano (dados complementares)**

            Por meio de visualizações gráficas e análises estatísticas, este estudo procura identificar padrões históricos, desigualdades regionais e relações entre fatores econômicos, sociais e demográficos que impactam a qualidade de vida das populações ao redor do mundo.

            ---

            ### Dataset Utilizado

            O dataset **Gapminder** reúne informações históricas sobre indicadores essenciais de desenvolvimento humano e econômico, cobrindo mais de **140 países** entre **1952 e 2007**.

            As principais variáveis analisadas incluem:

            - `lifeExp` → Expectativa de vida
            - `gdpPercap` → PIB per capita
            - `pop` → População total
            - `year` → Ano de referência
            - `continent` → Continente
            - `country` → País

            Como seção complementar, foram integrados dados externos da **UNDP (Programa das Nações Unidas para o Desenvolvimento)**, permitindo enriquecer a análise com indicadores relacionados à **educação e desenvolvimento humano**.

            ---
                
            ### Alunos

            **Matrícula:** 1471280  
            **Nome:** Leon Wagner Farias de Souza  
            **Email:** 1471280@sga.pucminas.br  

            **Matrícula:** 1666114  
            **Nome:** Marcos Silva de Castro  
            **Email:** 1666114@sga.pucminas.br  

            **Matrícula:** 1665824  
            **Nome:** Victor Paiva Nevola  
            **Email:** 1665824@sga.pucminas.br  

            **Matrícula:** 1669007  
            **Nome:** Kelvin de Lucca Feltrin  
            **Email:** 1669007@sga.pucminas.br  

            ---

            ### Objetivo da Aplicação

            Esta interface foi desenvolvida em **Streamlit** como uma camada complementar de apresentação dos resultados obtidos no Jupyter Notebook, permitindo navegar de forma interativa entre os diferentes blocos de análise, gráficos e principais insights identificados ao longo do estudo.
            """)
def render_dashboard(df_gapminder, df_hdi):
    st.title("Dashboard de Análises")

    tabs = st.tabs([
        "Bloco 1",
        "Bloco 2",
        "Bloco 3",
        "Bloco 4",
        "Bloco 5",
        "Bloco 6",
        "Seção Extra"
    ])

    with tabs[0]:
        st.header("Desenvolvimento Humano Global")
        st.markdown("""
                    ## 1.1 Média da expectativa de vida ao longo dos anos
                        Observa-se crescimento contínuo da expectativa de vida mundial entre 1952 e 2007, indicando avanços significativos nas condições de saúde, saneamento, 
                        alimentação e acesso à medicina ao longo das décadas.
                    """)
        # Calcular média da expectativa de vida por ano
        media_vida = df_gapminder.groupby("year", as_index=False)["lifeExp"].mean()
        # Exibir resultado
        fig_media_vida =ChartUtils.line_plot(
            data=media_vida,
            x="year",
            y="lifeExp",
            title="Média da Expectativa de Vida Mundial ao Longo dos Anos",
            xlabel="Ano",
            ylabel="Expectativa de Vida Média",
            show=False
        )
        st.pyplot(fig_media_vida)

        st.markdown("""
                    ## 1.2 Histograma 1952 vs 2007
                        A distribuição da expectativa de vida desloca-se significativamente para valores mais elevados em 2007 quando comparada a 1952, evidenciando melhora global 
                        das condições de vida e saúde da população mundial.
                    """)
        # Filtrar os anos
        df_1952 = df_gapminder[df_gapminder["year"] == 1952]
        df_2007 = df_gapminder[df_gapminder["year"] == 2007]

        fig_histograma = ChartUtils.compare_hist_subplot(
            data1=df_1952,
            data2=df_2007,
            x="lifeExp",
            title1="1952",
            title2="2007",
            suptitle="Distribuição da Expectativa de Vida Global",
            xlabel="Expectativa de Vida",
            show=False
        )

        st.pyplot(fig_histograma)
        
        st.markdown("""
                    ## 1.3 Países acima de 80 anos
                        Os países com expectativa de vida superior a 80 anos em 2007 concentram-se majoritariamente em regiões economicamente desenvolvidas, especialmente Europa, 
                        Oceania e partes da Ásia. 
                    """)
        df_80 = df_gapminder[df_gapminder["year"] == 2007]
        df_80 = df_80[df_80["lifeExp"] > 80]

        # Ordenar valores
        df_80 = df_80.sort_values(
            by="lifeExp",
            ascending=True
        )

        fig_80 = ChartUtils.bar_plot(
            data=df_80,
            x="lifeExp",
            y="country",
            hue="continent",
            title="Países com Expectativa de Vida acima de 80 anos",
            xlabel="Expectativa de Vida",
            ylabel="País",
            value_format="%.1f",
            show=False
        )
        st.pyplot(fig_80)

    with tabs[1]:
        st.header("Economia e Desenvolvimento")
        st.markdown("""
                    ## 2.1 - PIB vs Expectativa de Vida
                        Observa-se uma correlação positiva entre PIB per capita e expectativa de vida em 2007. Países com maior riqueza média tendem a apresentar melhores indicadores de longevidade, provavelmente devido ao maior acesso à saúde, 
                        alimentação, saneamento e infraestrutura. Entretanto, percebe-se que após determinado nível econômico, o aumento do PIB gera ganhos menores na expectativa de vida.

                        A escala logarítmica foi aplicada ao PIB per capita devido à grande disparidade econômica entre os países, permitindo melhor distribuição visual dos dados e facilitando a análise da 
                        correlação com a expectativa de vida.
                    """)
        df_2007 = df_gapminder[df_gapminder["year"] == 2007]

        fig_pipexp = ChartUtils.scatter_plot(
            data=df_2007,
            x="gdpPercap",
            y="lifeExp",
            hue="continent",
            size="pop",
            log_x=True,
            title="PIB per Capita vs Expectativa de Vida (2007)",
            xlabel="PIB per Capita (escala log)",
            ylabel="Expectativa de Vida",
            show=False
        )
        st.pyplot(fig_pipexp)

        st.markdown("""
                    ## 2.2 - Evolução do PIB por continente
                        Observa-se crescimento do PIB per capita médio em todos os continentes ao longo do período analisado. Europa e Oceania mantêm os maiores níveis econômicos médios durante praticamente toda 
                        a série histórica. Ásia e Américas apresentam trajetórias de crescimento relativamente semelhantes nas últimas décadas, enquanto a África demonstra evolução mais lenta, evidenciando 
                        persistência de desigualdades econômicas globais.
                    """)
        pib_continente = (
                df_gapminder.groupby(["year", "continent"])["gdpPercap"]
                .mean()
                .reset_index()
            )

        fig_pib_continente = ChartUtils.line_plot(
                data=pib_continente,
                x="year",
                y="gdpPercap",
                hue="continent",
                title="Evolução do PIB per Capita Médio por Continente",
                xlabel="Ano",
                ylabel="PIB per Capita Médio",
                show=False
            )
        st.pyplot(fig_pib_continente)

        st.markdown("""
                    ## 2.3 - Outliers
                        Os países identificados como outliers apresentam níveis relativamente elevados de PIB per capita, mas expectativa de vida abaixo do padrão observado para economias de
                        renda semelhante. Muitos desses países possuem economias dependentes de recursos naturais, especialmente petróleo e mineração, além de apresentarem elevada desigualdade social, 
                        concentração de renda ou desafios estruturais em saúde pública. Esses resultados evidenciam que crescimento econômico isoladamente não garante melhoria proporcional na qualidade de vida da população.
                    
                    #### Muitos desses países compartilham características como:
                        Desigualdade social elevada
                        Dependência de petróleo/gás/mineração
                        Concentração de renda
                        Desenvolvimento econômico pouco distribuído
                        Problemas estruturais em saúde pública
                        Histórico político instável ou desenvolvimento tardio
                    """)
        df_2007 = df_gapminder[df_gapminder["year"] == 2007]
        # Limites
        pib_alto = df_2007["gdpPercap"].median()
        vida_baixa = df_2007["lifeExp"].median()

        # Outliers
        outliers = df_2007[
            (df_2007["gdpPercap"] > pib_alto) &
            (df_2007["lifeExp"] < vida_baixa)
        ]

        fig_outliers = ChartUtils.outlier_scatter_plot(
            data=df_2007,
            outliers=outliers,
            x="gdpPercap",
            y="lifeExp",
            label_col="country",
            vline=pib_alto,
            hline=vida_baixa,
            log_x=True,
            title="Outliers: Alto PIB e Baixa Expectativa de Vida",
            xlabel="PIB per Capita (escala log)",
            ylabel="Expectativa de Vida",
            show=False
        )
        st.pyplot(fig_outliers)

    with tabs[2]:
        st.header("População e Distribuição")
        st.markdown("""
                    ## 3.1 - Top 10 países mais populoso
                        Observa-se forte concentração da população mundial em poucos países, especialmente na Ásia. China e Índia lideram amplamente o ranking populacional em 2007, refletindo o elevado peso demográfico do 
                        continente asiático na população global. Países como Estados Unidos, Indonésia e Brasil também apresentam grande relevância populacional.
                    """)
        df_top_10_paises_2007 = df_gapminder[df_gapminder["year"] == 2007]
        df_top_10_paises_2007 = (
            df_top_10_paises_2007.assign(pop_milhoes=df_top_10_paises_2007["pop"] / 1_000_000)
            .sort_values(by="pop", ascending=False)
            .head(10)
        )
        fig_top10 = ChartUtils.bar_plot(
            data=df_top_10_paises_2007,
            x="pop_milhoes",
            y="country",
            hue="continent",
            title="Top 10 Países Mais Populosos em 2007",
            xlabel="População (milhões)",
            ylabel="País",
            value_format="%.1f",
            show=False
        )
        st.pyplot(fig_top10)

        st.markdown("""
                    ## 3.2 - Evolução da Ásia vs Europa
                        Observa-se crescimento populacional expressivo da Ásia ao longo das décadas, contrastando com a relativa estabilidade populacional da Europa. Esse comportamento reflete diferenças em taxas de 
                        natalidade, urbanização, desenvolvimento econômico e transição demográfica entre os continentes.
                    """)
        pop_continente = (
        df_gapminder.groupby(["year", "continent"])["pop"]
        .sum()
        .reset_index()
        )

        asia_europa = pop_continente[
            pop_continente["continent"].isin(["Asia", "Europe"])
        ]

        asia_europa["pop_bilhoes"] = (
            asia_europa["pop"] / 1_000_000_000
        )

        fig_asia_europa = ChartUtils.line_plot(
            data=asia_europa,
            x="year",
            y="pop_bilhoes",
            hue="continent",
            title="Crescimento Populacional: Ásia vs Europa",
            xlabel="Ano",
            ylabel="População (bilhões)",
            show=False
        )
        st.pyplot(fig_asia_europa)

        st.markdown("""
                    ## 3.3 - Área empilhada — População mundial por continente
                        A visualização evidencia a forte concentração populacional mundial na Ásia ao longo de todo o período analisado. Também é possível observar o crescimento progressivo da participação africana na população global, 
                        enquanto a Europa apresenta crescimento relativamente estável. O gráfico destaca importantes transformações demográficas globais ao longo das décadas.
                    """)
        pop_continente = (
        df_gapminder.groupby(["year", "continent"])["pop"]
        .sum()
        .reset_index()
        )
        pivot_pop = pop_continente.pivot(
            index="year",
            columns="continent",
            values="pop"
        )
        pivot_pop = pivot_pop / 1_000_000_000

        fig_pop_mundial = ChartUtils.stack_plot(
            data=pivot_pop,
            x=pivot_pop.index,
            title="População Mundial por Continente ao Longo do Tempo",
            xlabel="Ano",
            ylabel="População (bilhões)",
            show=False
        )
        st.pyplot(fig_pop_mundial)

    with tabs[3]:
        st.header("Comparações Regionais")
        
        st.markdown("""
                    ## 4.1 - Boxplot por continente
                        Observa-se significativa desigualdade regional na expectativa de vida em 2007. África apresenta a menor mediana e maior variabilidade relativa, enquanto Europa e Oceania concentram os maiores 
                        valores de longevidade. Os resultados evidenciam diferenças históricas e socioeconômicas entre os continentes em relação ao acesso à saúde, saneamento e qualidade de vida. 
                    """)
        df_2007 = df_gapminder[df_gapminder["year"] == 2007]

        fig_box = ChartUtils.box_plot(
            data=df_2007,
            x="continent",
            y="lifeExp",
            title="Distribuição da Expectativa de Vida por Continente (2007)",
            xlabel="Continente",
            ylabel="Expectativa de Vida",
            showmeans=True,
            show=False
        )

        st.pyplot(fig_box)

        st.markdown("""
                    ## 4.2 - Brasil vs América do Sul
                       Observa-se crescimento contínuo da expectativa de vida no Brasil ao longo do período analisado, acompanhando a tendência geral da América do Sul. O país apresenta trajetória 
                        próxima da média regional, refletindo melhorias graduais em saúde pública, saneamento e condições socioeconômicas nas últimas décadas.
                    """)
        brasil = df_gapminder[df_gapminder["country"] == "Brazil"]
        paises_america_sul = [
            "Argentina",
            "Bolivia",
            "Brazil",
            "Chile",
            "Colombia",
            "Ecuador",
            "Paraguay",
            "Peru",
            "Uruguay",
            "Venezuela"
        ]

        america_sul = df_gapminder[
            df_gapminder["country"].isin(paises_america_sul)
        ]

        media_america_sul = (
            america_sul.groupby("year")["lifeExp"]
            .mean()
            .reset_index()
        )

        fig_brasil_america_sul = ChartUtils.compare_line_plot(
            data1=brasil,
            data2=media_america_sul,
            x="year",
            y="lifeExp",
            label1="Brasil",
            label2="Média América do Sul",
            title="Brasil vs Média da América do Sul: Expectativa de Vida",
            xlabel="Ano",
            ylabel="Expectativa de Vida",
            marker1="o",
            marker2="s",
            linestyle1="-",
            linestyle2="--",
            show=False
        )

        st.pyplot(fig_brasil_america_sul)

    with tabs[4]:
        st.header("Relações Estatísticas")
        st.markdown("""
                    ## 5.1 - População vs PIB per capita
                       Observa-se que países mais populosos não são necessariamente os mais ricos em termos de PIB per capita. A visualização evidencia grande dispersão entre população e riqueza média, indicando que fatores econômicos, 
                        históricos e estruturais influenciam o desenvolvimento econômico além do tamanho populacional.
                    """)
        df_2007 = df_gapminder[df_gapminder["year"] == 2007]
        df_2007["pop_milhoes"] = df_2007["pop"] / 1_000_000

        destaques = df_2007[
            df_2007["country"].isin(
                ["China", "India", "United States", "Brazil"]
            )
        ]

        fig_po_capita = ChartUtils.scatter_plot(
            data=df_2007,
            x="pop_milhoes",
            y="gdpPercap",
            hue="continent",
            size="lifeExp",
            log_x=True,
            log_y=True,
            title="População vs PIB per Capita (2007)",
            xlabel="População (milhões)",
            ylabel="PIB per Capita",
            label_data=destaques,
            label_col="country",
            show=False
        )
        st.pyplot(fig_po_capita)

        st.markdown("""
                    ## 5.2 - Heatmap de correlação
                       O heatmap evidencia correlação positiva entre PIB per capita e expectativa de vida, indicando que países economicamente mais desenvolvidos tendem a apresentar melhores indicadores de longevidade. Por outro 
                       lado, a população apresenta correlação fraca com as demais variáveis, sugerindo que o tamanho populacional, isoladamente, não determina riqueza média nem qualidade de vida.
                    """)
        corr = df_gapminder[["pop", "gdpPercap", "lifeExp"]].corr()

        fig_corr = ChartUtils.heatmap_plot(
            data=corr,
            title="Heatmap de Correlação",
            show=False
        )
        st.pyplot(fig_corr)

    with tabs[5]:
        st.header("Evolução Histórica")
        st.markdown("""
                    ## 6.1 - Maior aumento percentual de expectativa de vida
                       Alguns países apresentaram crescimento expressivo da expectativa de vida entre 1952 e 2007, refletindo avanços em saúde pública, vacinação, saneamento básico e desenvolvimento socioeconômico. Em muitos casos,
                       os maiores aumentos ocorreram em países que inicialmente possuíam indicadores muito baixos, permitindo ganhos relativos mais significativos ao longo das décadas.
                    """)
        
        life_1952 = df_gapminder[df_gapminder["year"] == 1952][
            ["country", "lifeExp"]
        ]

        life_2007 = df_gapminder[df_gapminder["year"] == 2007][
            ["country", "lifeExp"]
        ]

        life_1952 = life_1952.rename(
            columns={"lifeExp": "lifeExp_1952"}
        )

        life_2007 = life_2007.rename(
            columns={"lifeExp": "lifeExp_2007"}
        )

        crescimento = pd.merge(
            life_1952,
            life_2007,
            on="country"
        )

        crescimento["crescimento_percentual"] = (
            (
                crescimento["lifeExp_2007"] -
                crescimento["lifeExp_1952"]
            )
            / crescimento["lifeExp_1952"]
        ) * 100

        top_crescimento = crescimento.sort_values(
            by="crescimento_percentual",
            ascending=False
        )

        # top_crescimento.head(10)
        # Top 10
        top_10 = top_crescimento.head(10)

        # Ordenar para gráfico
        top_10 = top_10.sort_values(
            by="crescimento_percentual"
        )

        fig_crescimento = ChartUtils.bar_plot(
            data=top_10,
            x="crescimento_percentual",
            y="country",
            title="Maior Crescimento da Expectativa de Vida (1952–2007)",
            xlabel="Crescimento Percentual (%)",
            ylabel="País",
            value_format="%.1f%%",
            legend=False,
            show=False
        )
        st.pyplot(fig_crescimento)
    with tabs[6]:
        st.header("Seção Extra: Educação, Renda e Qualidade de Vida")
        st.markdown("""
                    Como complemento às análises anteriores, foi incorporado ao estudo o indicador *Expected Years of Schooling* (anos esperados de escolaridade), extraído da base de dados da UNDP para o ano de 2007. A inclusão desse indicador permite 
                    adicionar uma nova dimensão à análise, investigando como a educação se relaciona com variáveis já presentes na base Gapminder, como renda per capita e expectativa de vida. Dessa forma, torna-se possível observar não apenas aspectos 
                    econômicos e de saúde, mas também o papel da educação como fator associado ao desenvolvimento humano.

                    A análise mostra que países com maior expectativa de escolaridade tendem a concentrar-se em níveis mais elevados de expectativa de vida, indicando uma forte associação entre educação e qualidade de vida. No gráfico econômico, também 
                    é possível observar que países mais ricos frequentemente apresentam melhores indicadores educacionais, embora existam diferenças regionais que mostram que renda, isoladamente, não explica todo o desenvolvimento humano.
                    """)
        
        df_extra = prepare_schooling_data(
            df_gapminder,
            df_hdi,
            year=2007
        )
        fig_extra = ChartUtils.schooling_analysis_subplot(data=df_extra, show=False)
        st.pyplot(fig_extra)

def render_conclusion():
    st.title("Conclusão")
    st.markdown("""
                # 📚 Conclusão

                A análise realizada a partir do dataset **Gapminder** permitiu observar, de forma histórica e comparativa, importantes transformações nos indicadores de desenvolvimento humano e econômico ao redor do mundo entre **1952 e 2007**.

                De maneira geral, os dados mostram um **avanço consistente na expectativa de vida global ao longo das décadas**, refletindo melhorias em fatores como saúde pública, medicina, saneamento e condições gerais de vida. O aumento do número de países com níveis elevados de longevidade em 2007 reforça esse movimento de progresso global, embora os ganhos não tenham ocorrido de forma homogênea entre as diferentes regiões.

                Sob a perspectiva econômica, a análise evidenciou uma **relação positiva entre PIB per capita e expectativa de vida**, indicando que países mais ricos tendem, em média, a apresentar melhores indicadores de saúde e qualidade de vida. No entanto, a presença de outliers mostrou que **crescimento econômico isolado não é suficiente para explicar desenvolvimento humano**, revelando situações em que renda elevada não se traduz necessariamente em maior longevidade.

                As análises populacionais também mostraram importantes transformações demográficas globais. Observou-se a forte concentração populacional na **Ásia**, além do crescimento progressivo da participação africana na população mundial, enquanto regiões como a Europa apresentaram comportamento mais estável ao longo do período. Esses padrões reforçam a importância de considerar fatores demográficos na análise de desenvolvimento global.

                Do ponto de vista regional, os gráficos comparativos destacaram desigualdades significativas entre continentes. Regiões como **Europa e Oceania** concentraram melhores indicadores de expectativa de vida e menor dispersão, enquanto a **África apresentou maior variabilidade e menores medianas**, evidenciando persistência de desigualdades estruturais no desenvolvimento humano.

                A seção complementar, com a integração de dados da **UNDP**, trouxe uma dimensão adicional à análise ao incorporar o indicador de **anos esperados de escolaridade**. Os resultados sugerem uma forte associação entre **educação, renda e expectativa de vida**, reforçando a ideia de que o desenvolvimento humano é multifatorial e depende não apenas de crescimento econômico, mas também de investimentos em capital humano e oportunidades sociais.

                Em síntese, os dados analisados mostram que o desenvolvimento humano global avançou de forma significativa no período estudado, mas também evidenciam que **riqueza, saúde, educação e demografia estão profundamente interligados**, e que o progresso não ocorre de maneira uniforme entre países e regiões. A análise reforça que o desenvolvimento sustentável depende de uma combinação equilibrada de fatores econômicos, sociais e estruturais, e não apenas do aumento de renda.
                """)

def main():
    # Carregando os data frames
    df_gapminder, df_hdi = load_data()

    # Configurações da página
    st.set_page_config(
        page_title="Gapminder Dashboard",
        page_icon="📊",
        layout="wide"
    )
    # Barra lateral
    st.sidebar.title("📊 Gapminder Dashboard")
    menu = st.sidebar.radio(
        "Navegação",
        [
            "Apresentação",
            "Dashboard",
            "Conclusão"
        ]
    )
    # Renderizando as páginas
    if menu == "Apresentação":
        render_home()
    elif menu == "Dashboard":
        render_dashboard(df_gapminder, df_hdi)
    elif menu == "Conclusão":
        render_conclusion()

if __name__ == "__main__":
    main()