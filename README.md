# Introduction To Exploratory Data Analysis in Python
Exploratory data analysis using Python, Pandas and data from the Stanford Open Policing Project.

![Meme](https://i.imgflip.com/2xhjll.jpg)

## What are we going to cover?

## What dataset are we using?
We'll be using the Maryland subset of the [Stanford Open Policing Project](https://openpolicing.stanford.edu) dataset, made available under the Open Data Commons Attribution License.

## How do I download the dataset and the associated jupyter notebooks?
There are three equally valid ways to get the data:

- If you're comfortable with git, you can click the green button above and clone the repository:
```
git clone https://github.com/ilyagerner/pandas_policing_tutorial.git
```
- If you're comfortable with ZIP files, you can click the green button above and download the repository as a ZIP archive.
- If you want to download the files individually, right click on these links and select "Save As": traffic_stops_md.csv, workshop.ipynb.

## What Python packages do I need to have installed?
![xkcd comic](https://imgs.xkcd.com/comics/python_environment.png "The Python environmental protection agency wants to seal it in a cement chamber, with pictorial messages to future civilizations warning them about the danger of using sudo to install random Python packages.")

([XCKD 1987](https://xkcd.com/1987/). CC License.)

We'll be using the following:
- Python 3.7.3 (but we're unlikely to use any of the newest features, so older versions should work fine)
- pandas
- numpy
- matplotlib
- seaborn

A good way to avoid the unpleasant scenario outlined in the XKCD comic is to rely on the Anaconda distribution for your data science libraries. This is less vital for Mac and Linux users, but important for Windows users thanks to the various C and FORTRAN dependencies in the Python data stack.

### Instructions for Installing Anaconda
1. Download the appropriate version of [Anaconda](https://www.anaconda.com/distribution/#download-section)
2. Follow the instructions on that page to run the installer
3. Test out the jupyter notebook: open a Terminal window (on Mac or Linux), navigate to the directory where you have downloaded the dataset/workshop notebook and type:
`
jupyter notebook
`
3. On Windows, start the Anaconda launcher, which you can find in C:\Anaconda or, in the Start menu. Start the jupyter notebook by typing `jupyter notebook`. A new browser window should open.

## Who led the workshop and is there a way to contact him??
Ilya Gerner can be found on twitter as [@igerner](https://twitter.com/igerner) and via email at ilyagerner@gmail.com.
