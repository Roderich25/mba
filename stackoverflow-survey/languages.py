import csv
from collections import Counter

with open('survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    total = 0
    language_counter = Counter()
    for line in csv_reader:
        language_counter.update(line['LanguageWorkedWith'].split(';'))
        total += 1
        print(line['DevType'].split(';'))

for language, value in language_counter.most_common(5):
    language_pct = round(value / total * 100, 2)
    print(f'{language}; {language_pct}%')
