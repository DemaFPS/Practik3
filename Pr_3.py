import matplotlib.pyplot as plt
import numpy as np

# мои данные
tablets_compact = [
    {
        "model": "iPad Pro 12.9",
        "screen_size_in": 12.9,
        "resolution_px": "2732x2048",
        "ram_gb": 16,
        "storage_gb": 256,
        "battery_mah": 10758,
        "weight_g": 682,
        "stylus_support": True,
        "price_rub": 119990,
    },
    {
        "model": "Samsung Galaxy Tab S9 Ultra",
        "screen_size_in": 14.6,
        "resolution_px": "2960x1848",
        "ram_gb": 12,
        "storage_gb": 256,
        "battery_mah": 11200,
        "weight_g": 732,
        "stylus_support": True,
        "price_rub": 99990,
    },
    {
        "model": "Microsoft Surface Pro 9",
        "screen_size_in": 13.0,
        "resolution_px": "2880x1920",
        "ram_gb": 16,
        "storage_gb": 512,
        "battery_mah": 5070,
        "weight_g": 891,
        "stylus_support": True,
        "price_rub": 129990,
    },
    {
        "model": "Xiaomi Pad 6",
        "screen_size_in": 11.0,
        "resolution_px": "2880x1800",
        "ram_gb": 8,
        "storage_gb": 256,
        "battery_mah": 8840,
        "weight_g": 490,
        "stylus_support": False,
        "price_rub": 39990,
    },
]

models = [tablet["model"] for tablet in tablets_compact]
name_char = [
    "ОЗУ (ГБ)",
    "Память (ГБ)",
    "Батарея (мАч)",
    "Диагональ (дюйм)",
    "Обратный вес (1/г)",
    "Обратная цена (1/руб)",
    "Поддержка стилуса"
]

char = []
for tablet in tablets_compact:
    char.append([
        tablet["ram_gb"],
        tablet["storage_gb"],
        tablet["battery_mah"],
        tablet["screen_size_in"],
        1 / tablet["weight_g"],
        1 / tablet["price_rub"],
        1 if tablet["stylus_support"] else 0
    ])

def get_normal(char):
    normal = []
    for item in char:
        normal.append([a / b for a, b in zip(item, char[0])])
    return normal

def get_quality(normal):
    result = []
    for item in normal:
        result.append(round(sum(item) / len(item), 2))
    return result

def create_bar(name, values):
    plt.bar(name, values)
    plt.xlabel("Модель")
    plt.ylabel("Kту")
    plt.title("Интегральный показатель качества планшетов")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def create_radial(models, name, values):
    for item in values:
        item += item[:1]

    angles = np.linspace(0, 2 * np.pi, len(name), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))

    for i in range(len(values)):
        ax.plot(angles, values[i], "o-", linewidth=2, label=models[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(name, fontsize=10)
    ax.set_ylim(0, 2)

    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение относительных характеристик планшетов", pad=20)
    plt.show()


normalized = get_normal(char)
quality = get_quality(normalized)

create_bar(models, quality)
create_radial(models, name_char, normalized)