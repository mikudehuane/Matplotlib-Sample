# Matplotlib-Sample
Using matplotlib.pyplot to plot experimental results.  

Key functions include:\
  &nbsp; &nbsp; Draw subfigures within the plot;\
  &nbsp; &nbsp; Customize the legends;\
  &nbsp; &nbsp; Customize the fonts;\
  &nbsp; &nbsp; Customizing the axises.
  
The suggested font is TrueType.\
  &nbsp; &nbsp; To set this font, please open anaconda/envs/<env>/lib/site-packages/matplotlib/mpl-data/matplotlibrc.\
  &nbsp; &nbsp; Then add or release the comment "pdf.fontType: 42".\
  &nbsp; &nbsp; Remember to output pdf files rather than eps files in the programs, or errors will be introduced.

Many matplotlib APIs are hard to find, e.g. changing the font, using latex, adding annotation, mix fonts, adding subfigures, etc.
Since the strict requirements on submissions to conferences in computer science, we actually need these features, but they are not well-documented.
Therefore, I write a sample to record these APIs to avoid searching for them again when we need them.
