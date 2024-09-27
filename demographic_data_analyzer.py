import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv('adult.data.csv')

    #Quantos de cada raça estão representados neste conjunto de dados? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # Qual a média de idade dos homens?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Qual é a porcentagem de pessoas que têm um diploma de Bacharel?
    percentage_bachelors = round((df['education'].value_counts(normalize=True)['Bachelors'] * 100), 1)

    # Qual porcentagem de pessoas com educação avançada (Bacharel, Mestrado ou Doutorado) ganham mais de 50K?
    # Qual porcentagem de pessoas sem educação avançada ganham mais de 50K?

    # Com e sem educação superior
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # porcentagem com salário >50K
    higher_education_rich = higher_education_rich = round((df[higher_education]['salary'].value_counts(normalize=True)['>50K'] * 100), 1)
    lower_education_rich = round((df[lower_education]['salary'].value_counts(normalize=True)['>50K'] * 100), 1)

    # Qual o número mínimo de horas que uma pessoa trabalha por semana?
    min_work_hours = df['hours-per-week'].min()

    # Qual porcentagem das pessoas que trabalham o número mínimo de horas por semana têm salário >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100)

    # Qual país tem a maior porcentagem de pessoas que ganham >50K?
    country_earning = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    highest_earning_country = country_earning[">50K"].idxmax()
    highest_earning_country_percentage = (country_earning[">50K"].max() * 100).round(1)

    # Identifique a ocupação mais popular para aqueles que ganham >50K na Índia.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
