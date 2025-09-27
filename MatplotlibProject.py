import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. Create Sample Dataset
# ==============================

# Years and global population (billions approx.)
years = list(range(1960, 2021, 10))
world_population = [3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 7.8]  # billions

# Latest population of top 10 countries (millions approx.)
top_countries = {
    'China': 1440,
    'India': 1390,
    'USA': 331,
    'Indonesia': 273,
    'Pakistan': 225,
    'Brazil': 213,
    'Nigeria': 211,
    'Bangladesh': 166,
    'Russia': 146,
    'Mexico': 128
}

# Population share by continent (billions approx.)
continents = {
    'Asia': 4.7,
    'Africa': 1.3,
    'Europe': 0.7,
    'North America': 0.6,
    'South America': 0.4,
    'Oceania': 0.04
}

# Sample population vs GDP dataset
pop_gdp_data = {
    'Country': ['China', 'India', 'USA', 'Indonesia', 'Pakistan',
                'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico'],
    'Population': [1440, 1390, 331, 273, 225, 213, 211, 166, 146, 128],  # millions
    'GDP': [16800, 3300, 21400, 1100, 280, 1800, 450, 320, 1500, 1200]   # billions USD
}
df_pop_gdp = pd.DataFrame(pop_gdp_data)

plt.style.use('seaborn-v0_8')

# ==============================
# 2. Visualization (Each Chart Separately)
# ==============================

# --- Line Plot: World population growth ---
plt.figure(figsize=(8, 5))
plt.plot(years, world_population, marker='o', color='red', linewidth=2, label="World Population")
plt.title("World Population Growth (1960–2020)")
plt.xlabel("Year")
plt.ylabel("Population (Billions)")
plt.legend(loc="upper left", fontsize=10, frameon=True)
plt.grid(True)
plt.show()

# --- Bar Chart: Top 10 populated countries ---
plt.figure(figsize=(8, 5))
plt.bar(top_countries.keys(), top_countries.values(), color='green', label="Population 2020")
plt.title("Top 10 Most Populated Countries")
plt.ylabel("Population (Millions)")
plt.xticks(rotation=45)
plt.legend(loc="upper right", fontsize=10, frameon=True)
plt.show()

# --- Pie Chart: Population share by continent ---
plt.figure(figsize=(7, 7))
plt.pie(continents.values(), labels=continents.keys(),
        autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
plt.title("Population Share by Continent")
plt.legend(continents.keys(), loc="lower left", fontsize=9, frameon=True)
plt.show()

# --- NEW Bar Chart: Population by continent ---
plt.figure(figsize=(8, 5))
plt.bar(continents.keys(), continents.values(), color='skyblue', edgecolor='black', label="Population by Continent")
plt.title("Population by Continent")
plt.ylabel("Population (Billions)")
plt.legend(loc="upper right", fontsize=10, frameon=True)
plt.show()

# --- Scatter Plot: Population vs GDP ---
plt.figure(figsize=(8, 6))
plt.scatter(df_pop_gdp["Population"], df_pop_gdp["GDP"],
            s=df_pop_gdp["Population"]/2, c='red', alpha=0.7, edgecolors="k", label="Countries")
for i, row in df_pop_gdp.iterrows():
    plt.text(row["Population"]+10, row["GDP"]+100, row["Country"], fontsize=8)  # shifted for clarity
plt.title("Population vs GDP")
plt.xlabel("Population (Millions)")
plt.ylabel("GDP (Billions USD)")
plt.legend(loc="upper left", fontsize=9, frameon=True)
plt.grid(True)
plt.show()
