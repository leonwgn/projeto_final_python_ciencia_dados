@staticmethod
def prepare_schooling_data(
    df_gapminder,
    df_hdi,
    year=2007
):
    # filtrar Gapminder
    df_year = df_gapminder[
        df_gapminder["year"] == year
    ].copy()

    # filtrar indicador
    schooling = df_hdi[
        df_hdi["indicator"] == "Expected Years of Schooling (years)"
    ].copy()

    # filtrar ano
    schooling_year = schooling[
        schooling["year"] == year
    ].copy()

    # selecionar colunas
    schooling_year = schooling_year[
        ["country", "value"]
    ].rename(
        columns={"value": "schooling_years"}
    )

    # merge
    df_extra = df_year.merge(
        schooling_year,
        on="country",
        how="inner"
    )

    return df_extra