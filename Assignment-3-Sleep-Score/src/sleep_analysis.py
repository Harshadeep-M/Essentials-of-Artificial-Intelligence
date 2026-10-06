import pandas as pd
df = pd.read_csv("data/Sleep_health_and_lifestyle_dataset.csv")

#Sleep score calculation

def duration_score(hours):
    if 7 <= hours <= 9:
        return 100
    elif hours < 7:
        return max(0, (hours / 7) * 100)
    else:
        return max(0, 100 - ((hours - 9) * 20))

df["Duration Score"] = df["Sleep Duration"].apply(duration_score)
df["Quality Score"] = (df["Quality of Sleep"] / 9) * 100
df["Stress Score"] = (
    (df["Stress Level"].max() - df["Stress Level"]) /
    (df["Stress Level"].max() - df["Stress Level"].min())
) * 100

df["Activity Score"] = (
    df["Physical Activity Level"] /
    df["Physical Activity Level"].max()
) * 100

df["Disorder Score"] = df["Sleep Disorder"].map({
    "Sleep Apnea": 30,
    "Insomnia": 50
}).fillna(100)


# Final Sleep Score
df["Sleep Score"] = (
    0.30 * df["Duration Score"] +
    0.30 * df["Quality Score"] +
    0.20 * df["Stress Score"] +
    0.10 * df["Activity Score"] +
    0.10 * df["Disorder Score"]
).round(2)

#Sleep Score Category
def classify_sleep_score(score):
    if score >= 80:
        return "Excellent"
    elif score >= 65:
        return "Good"
    elif score >= 50:
        return "Fair"
    else:
        return "Poor"


df["Sleep Category"] = df["Sleep Score"].apply(
    classify_sleep_score
)

# Wellbeing Interpretation

def interpret_wellbeing(row):
    score = row["Sleep Score"]
    stress = row["Stress Level"]

    if score >= 80 and stress <= 4:
        return "Positive Wellbeing"
    elif score >= 65 and stress <= 5:
        return "Generally Positive"
    elif score < 50 or stress >= 8:
        return "Higher Concern"
    else:
        return "Moderate Concern"

df["Wellbeing Interpretation"] = df.apply(
    interpret_wellbeing,
    axis=1
)
df.to_csv(
    "outputs/sleep_score_results.csv",
    index=False
)

print("Sleep Score Analysis Completed!")
print(f"Total records analyzed: {len(df)}")
print("\nSleep Category Distribution:")
print(df["Sleep Category"].value_counts())
print("\nWellbeing Distribution:")
print(df["Wellbeing Interpretation"].value_counts())
print("\nAverage Sleep Score by Sleep Disorder:")
print(
    df.groupby(
        "Sleep Disorder",
        dropna=False
    )["Sleep Score"].mean().round(2)
)                  
print("\nResults saved to:")
print("outputs/sleep_score_results.csv")