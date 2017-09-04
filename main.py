import pandas as pd
import matplotlib.pyplot as plt
from conf.settings import DataFilesConf


def get_file():
    with open(DataFilesConf.FileNames.raw_data) as file:
        file_contents = file.read()
    return file_contents


def format_string(x):
    return x.lower().replace('cajones', '').replace('cajon', '').replace('x', '').replace('$', '')


def split_string(x):
    x = format_string(x)
    string_splitted = list(filter(lambda z: ('(' not in z) and ('' != z), x.split(' ')))
    bathrooms = ' '.join(string_splitted[9:])
    return string_splitted[:9] + [bathrooms]


def to_df(file_contents):
    headers = file_contents.split('\n')[0].replace('M2', '').replace('Precio de Lista', 'Precio')
    headers = headers.replace('á', 'a').replace('ñ', 'ni')
    headers = headers.replace('Balcón Posterior Balcón Frontal Terraza ', '').replace('*', '').split(' ')
    headers = list(filter(lambda x: '' != x, headers))
    return pd.DataFrame(list(map(lambda x: split_string(x), file_contents.split('\n')[2:-1])), columns=headers)


def numeric_df(df):
    df.loc[:, 'Interiores'] = df.Interiores.apply(float).values
    df.loc[:, 'Terrazas'] = df.Terrazas.apply(float).values
    df.loc[:, 'Privativos'] = df.Privativos.apply(float).values
    df.loc[:, 'Precio'] = df.Precio.apply(lambda x: float(x.replace(',', ''))).values
    df.loc[:, 'Estacionamiento'] = df.Estacionamiento.apply(int).values
    df.loc[:, 'Recamaras'] = df.Recamaras.apply(int).values
    return df


def main():
    file_contents = get_file()
    df = to_df(file_contents).query('Precio != "-"')
    df = numeric_df(df)
    df.to_csv(DataFilesConf.FileNames.prices, index=False)

    # Min price and available
    min_index = df.query('Estatus == "disponible"').Precio.argmin()
    df.loc[min_index].to_csv(DataFilesConf.FileNames.min_price)

    # Bar Plot -- Rooms
    df.groupby('Recamaras').Precio.mean().plot(kind='bar', title='Mean price per number of rooms')
    plt.ylabel('$ MXN')
    plt.savefig(DataFilesConf.FileNames.barplot_rooms)
    plt.close()

    # Bar Plot -- Parking Lots
    df.groupby('Estacionamiento').Precio.mean().plot(kind='bar', title='Mean price per number of parking lots')
    plt.ylabel('$ MXN')
    plt.savefig(DataFilesConf.FileNames.barplot_parking)
    plt.close()

    # Scatter Plot -- Price vs interior area
    df.plot.scatter(x='Interiores', y='Precio', title='Price vs interior area (m^2)')
    plt.ylabel('$ MXN')
    plt.savefig(DataFilesConf.FileNames.scatterplot_interiors)
    plt.close()

if __name__ == '__main__':
    main()

