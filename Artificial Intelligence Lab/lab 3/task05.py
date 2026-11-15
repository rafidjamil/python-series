import pandas as pd

titanic = pd.read_csv('titanic.csv')

q1 = (titanic.groupby(['sex', 'pclass'])['survived'].mean().unstack() * 100).round(2)
print("1. Survival rate (%) by sex and pclass:")
print(q1)

titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1
titanic['is_alone'] = titanic['family_size'] == 1
q2 = (titanic.groupby('is_alone')['survived'].mean() * 100).round(2)
print("\n2. Survival rate (%) travelling alone (True) vs with family (False):")
print(q2)

def age_group(age):
    if pd.isna(age): return None
    elif age < 13: return 'Child'
    elif age < 20: return 'Teen'
    elif age < 60: return 'Adult'
    else: return 'Senior'

titanic['age_group'] = titanic['age'].apply(age_group)
q3 = (titanic.groupby('age_group')['survived'].mean()
      .reindex(['Child', 'Teen', 'Adult', 'Senior']) * 100).round(2)
print("\n3. Survival rate (%) by age_group:")
print(q3)

q4 = (titanic.groupby('embarked')['survived'].mean() * 100).round(2)
print("\n4. Survival rate (%) by embarkation port:")
print(q4)
