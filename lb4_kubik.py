import random
import pandas as pd
import matplotlib.pyplot as plt
def kubik(n: int) -> list:
    """

    :param n: Количество подбрасываний
    :return:  Список слкучайных подюрасываний кубика
    """
    data = []
    while len(data) < n:
        data.append(random.randint(1, 6))
    return data

def count_rate(kub_data: list):
    """
    Возвращает частоту выпадания значений кубика,
    согласно полученным данным
    :param kub_data: данные эксперимента
    :return:
    """
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kub_data.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate
def sort_rate(counted_rate: dict):
    """
    Возвращает отсортированную частоту по ключу
    :param counted_rate: Наша неотсортированная частота
    :return:
    """
    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate

def crate_dataframe(sorted_date: dict):
    """
    Создание и преобразование данных в Pandas dataframe
    :param sorted_date: dict
    :return: pd.Dataframe
    """
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
    return df


def probability_solving(dataframe: pd.DataFrame):
    """
    Вычисление вероятности полученных результатов
    :param dataframe:
    :return:
    """
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe
print(probability_solving(crate_dataframe(sort_rate(count_rate(kubik(100))))))
print(probability_solving(crate_dataframe(sort_rate(count_rate(kubik(1000))))))
print(probability_solving(crate_dataframe(sort_rate(count_rate(kubik(10000))))))
print(probability_solving(crate_dataframe(sort_rate(count_rate(kubik(100000))))))
print(probability_solving(crate_dataframe(sort_rate(count_rate(kubik(1000000))))))

proba1=probability_solving(crate_dataframe(sort_rate(count_rate(kubik(100)))))
a = proba1['Вероятность'].plot(kind='bar', legend=True)
a.figure.savefig('Вероятность1.png')
plt.show()
proba2=probability_solving(crate_dataframe(sort_rate(count_rate(kubik(1000)))))
a2 = proba2['Вероятность'].plot(kind='bar', legend=True)
a2.figure.savefig('Вероятность2.png')
plt.show()
proba3=probability_solving(crate_dataframe(sort_rate(count_rate(kubik(10000)))))
a3 = proba3['Вероятность'].plot(kind='bar', legend=True)
a3.figure.savefig('Вероятность3.png')
plt.show()
proba4=probability_solving(crate_dataframe(sort_rate(count_rate(kubik(100000)))))
a4 = proba4['Вероятность'].plot(kind='bar', legend=True)
a4.figure.savefig('Вероятность4.png')
plt.show()
proba5=probability_solving(crate_dataframe(sort_rate(count_rate(kubik(1000000)))))
a5 = proba5['Вероятность'].plot(kind='bar', legend=True)
a5.figure.savefig('Вероятность5.png')
plt.show()