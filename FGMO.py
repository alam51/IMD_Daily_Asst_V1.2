import pandas as pd
import re
import matplotlib.pyplot as plt


def fgmo():
    print('*** Make Sure that the .csv file is in correct format***')
    file_path = re.escape(input('File path: '))
    file_name = input('.csv File name without extension: ')
    absolute_file_path = file_path + '\\' + file_name + '.csv'
    day_first = input('Day first?[T/F] : ')
    while True:
        if 'T' in day_first.upper():
            day_first = True
            break
        elif 'F' in day_first.upper():
            day_first = False
            break
        else:
            print("Neither 'T' or 'F'. Enter Again:  ")
    # df = pd.read_csv(absolute_file_path, index_col=None, header=None)
    df = pd.read_csv(absolute_file_path, index_col=0, parse_dates=True, infer_datetime_format=True,
                     low_memory=False, dayfirst=day_first)
    df.dropna(axis=0, thresh=2, inplace=True)

    print(df.to_string())
    fig, ax = plt.subplots()
    gen_unit_name = input('Generation Unit Name: ')
    ax.set_title(gen_unit_name + ' Generation Curve on ' + f'{df.index[0]} to {df.index[-1]}',
                 fontsize=17)
    ax.set_xlabel('Time', fontsize=17)
    ax.set_ylabel('Frequency [Hz]', fontsize=17)
    ax1 = ax.twinx()  # create secondary axis
    ax1.set_ylabel('GEN ACTIVE POWER [MW]')
    df1 = df["Frequency [Hz]"]
    df["Frequency [Hz]"].plot(ax=ax, style='g--', x_compat=True, label='Freq[Hz]')
    df2 = df["GEN ACTIVE POWER [MW]"]
    df2.plot(ax=ax1, style='b-', x_compat=True, label='Gen[MW]')
    leg = ax.legend(loc='lower left', frameon=False)
    leg1 = ax1.legend(loc='lower right', frameon=False)

    plt.grid(True)
    plt.show()
