pgcopd = md[(md.department_name == 'Prince George\'s County Police Department') | (md.department_name == 'PGCOPD')]
pgcopd.subject_race.value_counts(normalize=True)