import matplotlib.pyplot as plt
import seaborn as sns

class ChartUtils:

    @staticmethod
    def setup_theme():
        sns.set_theme(style="whitegrid")

    @staticmethod
    def create_figure(figsize=(12, 6)):
        plt.figure(figsize=figsize)

    @staticmethod
    def set_labels(title, xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    @staticmethod
    def show():
        plt.tight_layout()
        plt.show()

    @staticmethod
    def line_plot(data,
        x,
        y,
        hue=None,
        title="",
        xlabel="",
        ylabel="",
        figsize=(12,6),
        show=True
    ):

        sns.set_theme(style="whitegrid")

        fig, ax = plt.subplots(figsize=figsize)

        sns.lineplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            marker="o",
            ax = ax
        )  
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        fig.tight_layout()

        if show:
            plt.show()
        else:
            return fig

    @staticmethod
    def hist_plot(
        data,
        x,
        bins=15,
        kde=True,
        hue=None,
        title="",
        xlabel="",
        ylabel="Frequência",
        figsize=(10,6)
        ):

        sns.set_theme(style="whitegrid")

        plt.figure(figsize=figsize)

        sns.histplot(
            data=data,
            x=x,
            bins=bins,
            kde=kde,
            hue=hue
        )

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def compare_hist_subplot(
        data1,
        data2,
        x,
        title1="Grupo 1",
        title2="Grupo 2",
        bins=15,
        kde=True,
        suptitle="",
        xlabel="",
        ylabel="Frequência",
        figsize=(14,5),
        show=True
        ):
        sns.set_theme(style="whitegrid")

        fig, axes = plt.subplots(1, 2, figsize=figsize)
    

        sns.histplot(
            data=data1,
            x=x,
            bins=bins,
            kde=kde,
            ax=axes[0]
        )

        axes[0].set_title(title1)
        axes[0].set_xlabel(xlabel)
        axes[0].set_ylabel(ylabel)

        sns.histplot(
            data=data2,
            x=x,
            bins=bins,
            kde=kde,
            ax=axes[1]
        )

        axes[1].set_title(title2)
        axes[1].set_xlabel(xlabel)
        axes[1].set_ylabel(ylabel)

        plt.suptitle(suptitle)

        fig.tight_layout()

        if show:
            plt.show()
        else:
            return fig

    @staticmethod
    def scatter_plot(
        data,
        x,
        y,
        hue=None,
        size=None,
        sizes=(30, 300),
        alpha=0.7,
        title="",
        xlabel="",
        ylabel="",
        figsize=(12,6),
        log_x=False,
        log_y=False,
        legend=True,
        color=None,
        label_data=None,
        label_col=None,
        label_offset=(5, 5),
        show=True
        ):

        sns.set_theme(style="whitegrid")

      
        fig, axes = plt.subplots(figsize=figsize)

        sns.scatterplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            size=size,
            sizes=sizes,
            alpha=alpha,
            color=color
        )

        if log_x:
            plt.xscale("log")

        if log_y:
            plt.yscale("log")

        # Só adiciona labels se você passar
        if label_data is not None and label_col is not None:
            for _, row in label_data.iterrows():
                plt.annotate(
                    row[label_col],
                    (row[x], row[y]),
                    xytext=label_offset,
                    textcoords="offset points",
                    fontsize=9
                )

        axes.set_title(title)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)

        if legend:
            plt.legend()

        fig.tight_layout()

        if show:
             plt.show()
        else:             
            return fig
        
    @staticmethod
    def outlier_scatter_plot(   
        data,
        outliers,
        x,
        y,
        label_col=None,
        vline=None,
        hline=None,
        title="",
        xlabel="",
        ylabel="",
        figsize=(12,6),
        log_x=False,
        log_y=False,
        show=True
    ):

        sns.set_theme(style="whitegrid")

        # cria figure e axes corretamente
        fig, ax = plt.subplots(figsize=figsize)

        # Todos os países
        sns.scatterplot(
            data=data,
            x=x,
            y=y,
            color="lightgray",
            alpha=0.5,
            ax=ax
        )

        # Outliers
        sns.scatterplot(
            data=outliers,
            x=x,
            y=y,
            color="red",
            s=150,
            label="Outliers",
            ax=ax
        )

        # Linhas de referência
        if vline is not None:
            ax.axvline(
                vline,
                linestyle="--",
                color="blue",
                alpha=0.7,
                label="Limite PIB"
            )

        if hline is not None:
            ax.axhline(
                hline,
                linestyle="--",
                color="green",
                alpha=0.7,
                label="Limite Vida"
            )

        # Escalas log
        if log_x:
            ax.set_xscale("log")

        if log_y:
            ax.set_yscale("log")

        # Labels dos outliers
        if label_col is not None:
            for _, row in outliers.iterrows():
                ax.annotate(
                    row[label_col],
                    (row[x], row[y]),
                    xytext=(5, 5),
                    textcoords="offset points",
                    fontsize=9
                )

        # Títulos e labels
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        ax.legend()

        fig.tight_layout()

        if show:
            plt.show()
        else:
            return fig
    
    @staticmethod
    def bar_plot(
        data,
        x,
        y,
        hue=None,
        title="",
        xlabel="",
        ylabel="",
        figsize=(12,6),
        horizontal=True,
        show_values=True,
        value_format="%.1f",
        legend=True,
        show=True
        ):

        sns.set_theme(style="whitegrid")

       
        fig, ax = plt.subplots(figsize=figsize)

        # Horizontal
        if horizontal:
            ax = sns.barplot(
                data=data,
                x=x,
                y=y,
                hue=hue
            )
        else:
            ax = sns.barplot(
                data=data,
                x=y,
                y=x,
                hue=hue
            )

        # Mostrar valores nas barras
        if show_values:
            for container in ax.containers:
                 ax.bar_label(container, fmt=value_format) # type: ignore


        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        if legend and hue is not None:
            plt.legend()
        elif hue is None:
            legend_obj = ax.get_legend()
            if legend_obj:
                legend_obj.remove()

        plt.tight_layout()

        if show:
            plt.show()
        else:
            return fig


    @staticmethod
    def compare_line_plot(
        data1,
        data2,
        x,
        y,
        label1="Grupo 1",
        label2="Grupo 2",
        title="",
        xlabel="",
        ylabel="",
        figsize=(12,6),
        marker1="o",
        marker2="s",
        linestyle1="-",
        linestyle2="--",
        show=True
        ):

        sns.set_theme(style="whitegrid")
     
        fig, ax = plt.subplots(figsize=figsize)

        # Linha 1
        sns.lineplot(
            data=data1,
            x=x,
            y=y,
            label=label1,
            marker=marker1,
            linestyle=linestyle1,
            linewidth=3,
            ax=ax
        )

        # Linha 2
        sns.lineplot(
            data=data2,
            x=x,
            y=y,
            label=label2,
            marker=marker2,
            linestyle=linestyle2,
            linewidth=3,
            ax=ax
        )

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        ax.legend()

        plt.tight_layout()
    
        if show:
            plt.show()
        else:
            return fig
    
    @staticmethod
    def stack_plot(
        data,
        x=None,
        labels=None,
        title="",
        xlabel="",
        ylabel="",
        figsize=(12,6),
        alpha=0.8,
        legend=True,
        show=True
    ):

        sns.set_theme(style="whitegrid")

        fig, ax = plt.subplots(figsize=figsize)

        ax.stackplot(
            data.index if x is None else x,
            data.T,
            labels=labels if labels is not None else data.columns,
            alpha=alpha
        )

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        if legend:
            ax.legend(loc="upper left")

        fig.tight_layout()

        if show:
            plt.show()
        else:
            return fig
        
    @staticmethod
    def heatmap_plot(
        data,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        title="",
        figsize=(8,6),
        square=True,
        cbar=True,
        show=True
        ):

        sns.set_theme(style="white")

        fig, ax = plt.subplots(figsize=figsize)

        sns.heatmap(
            data,
            annot=annot,
            cmap=cmap,
            fmt=fmt,
            linewidths=linewidths,
            square=square,
            cbar=cbar,
            ax=ax
        )

        ax.set_title(title)

        plt.tight_layout()

        if show:
            plt.show()
        else:
            return fig

    @staticmethod
    def box_plot(
        data,
        x,
        y,
        hue=None,
        title="",
        xlabel="",
        ylabel="",
        figsize=(12,6),
        palette="Set2",
        rotate_xticks=False,
        showmeans=False,
        show=True
    ):

        sns.set_theme(style="whitegrid")

        fig, ax = plt.subplots(figsize=figsize)

        sns.boxplot(
            data=data,
            x=x,
            y=y,
            hue=hue,
            palette=palette,
            showmeans=showmeans,
            ax=ax
        )

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        if rotate_xticks:
            ax.tick_params(axis="x", rotation=45)

        fig.tight_layout()

        if show:
            plt.show()
        else:
            return fig

    @staticmethod
    def schooling_analysis_subplot(
        data,
        figsize=(16,6),
        alpha=0.7,
        show=True
    ):
    
        sns.set_theme(style="whitegrid")

        fig, axes = plt.subplots(1, 2, figsize=figsize)

        # gráfico 1
        sns.scatterplot(
            data=data,
            x="gdpPercap",
            y="lifeExp",
            hue="schooling_years",
            size="pop",
            alpha=alpha,
            ax=axes[0]
        )

        axes[0].set_xscale("log")
        axes[0].set_title("PIB per Capita vs Expectativa de Vida")
        axes[0].set_xlabel("PIB per Capita (escala log)")
        axes[0].set_ylabel("Expectativa de Vida")

        # gráfico 2
        sns.scatterplot(
            data=data,
            x="schooling_years",
            y="lifeExp",
            hue="continent",
            alpha=alpha,
            ax=axes[1]
        )

        axes[1].set_title("Escolaridade vs Expectativa de Vida")
        axes[1].set_xlabel("Anos Esperados de Escolaridade")
        axes[1].set_ylabel("Expectativa de Vida")

        fig.tight_layout()

        if show:
            plt.show()
        else:
            return fig