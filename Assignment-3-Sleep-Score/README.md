# Sleep Score Analysis

A Python-based data analysis project that calculates a Sleep Score for individuals using sleep, stress, physical activity, and sleep disorder information.

The project also provides a rule-based wellbeing interpretation based on the calculated Sleep Score and Stress Level.

## Objective

The main objectives of this project are:

- Analyze a sleep health and lifestyle dataset.
- Calculate a Sleep Score between 0 and 100.
- Categorize individuals based on their Sleep Score.
- Analyze the relationship between sleep and stress.
- Provide a sleep-related wellbeing interpretation.
- Generate a processed dataset containing the calculated results.

## Dataset

The project uses the Sleep Health and Lifestyle Dataset.

The dataset contains 374 records and 13 original attributes, including:

- Gender
- Age
- Occupation
- Sleep Duration
- Quality of Sleep
- Physical Activity Level
- Stress Level
- BMI Category
- Blood Pressure
- Heart Rate
- Daily Steps
- Sleep Disorder

## Sleep Score

The Sleep Score is calculated on a scale of 0–100 using the following weighted factors:

| Factor | Weight |
|---|---:|
| Sleep Duration | 30% |
| Quality of Sleep | 30% |
| Stress Level | 20% |
| Physical Activity | 10% |
| Sleep Disorder | 10% |

Lower stress contributes to a higher score, while the presence of a sleep disorder reduces the score.

### Sleep Score Categories

| Score | Category |
|---|---|
| 80–100 | Excellent |
| 65–79 | Good |
| 50–64 | Fair |
| Below 50 | Poor |

## Wellbeing Interpretation

The project combines Sleep Score and Stress Level to provide a general wellbeing interpretation.

The possible interpretations are:

- Positive Wellbeing
- Generally Positive
- Moderate Concern
- Higher Concern

This interpretation is intended for general sleep and wellbeing analysis. It is not a medical or psychological diagnosis.

## Results

The analysis produced the following Sleep Score distribution:

| Category | Number of People |
|---|---:|
| Excellent | 182 |
| Good | 84 |
| Fair | 103 |
| Poor | 5 |

The wellbeing interpretation distribution was:

| Interpretation | Number of People |
|---|---:|
| Positive Wellbeing | 118 |
| Generally Positive | 90 |
| Moderate Concern | 96 |
| Higher Concern | 70 |

## Observations

- Individuals in the Excellent Sleep Category had an average sleep duration of 7.72 hours.
- Individuals in the Poor Sleep Category had an average sleep duration of 5.86 hours.
- Average Quality of Sleep was 8.37 for the Excellent category and 4.00 for the Poor category.
- Positive Wellbeing had the lowest average stress level at 3.40.
- Higher Concern had the highest average stress level at 8.00.
- Individuals without a recorded sleep disorder had an average Sleep Score of 82.68.
- Individuals with Insomnia had an average Sleep Score of 68.49.
- Individuals with Sleep Apnea had an average Sleep Score of 72.72.

These results show a relationship between sleep-related factors, stress level, and the calculated wellbeing interpretation.

Technologies Used
- Python
- Pandas
- Git
- GitHub

How to Run
1. Clone the repository
git clone <repository-url>

2. Navigate to the project
cd Sleep-score-analysis

3. Install dependencies
pip install -r requirements.txt

4. Run the analysis
python src/sleep_analysis.py

The processed results will be saved to:
outputs/sleep_score_results.csv