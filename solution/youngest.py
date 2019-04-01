print(md['subject_age'].min())
#It's a 10-year-old boy, cited for driving without a license.
md[(md['subject_age']) == md['subject_age'].min()]
