"""Обработка показаний датчика температуры (учебный пример для ЛР-4 по СУВ)."""


def moving_average(values, window=3):
    """Скользящее среднее для сглаживания шумных измерений."""
    return [sum(values[i - window + 1:i + 1]) / window for i in range(window - 1, len(values))]


if __name__ == "__main__":
    readings = [21.4, 21.9, 22.6, 21.8, 23.1, 22.7]
    print("Показания:", readings)
    print("Сглаженные:", [round(v, 2) for v in moving_average(readings)])
