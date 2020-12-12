# Matplotlib-Sample
Using matplotlib.pyplot to plot experimental results.  

# Key Functions
- Draw subfigures within the plot;
- Customize the legends;
- Customize the fonts;
- Customizing the axises.

# Font
The suggested font is TrueType.
1. To set this font, please open anaconda/envs/<env>/lib/site-packages/matplotlib/mpl-data/matplotlibrc.
2. Then add or release the comment "pdf.fontType: 42".
3. Remember to output pdf files rather than eps files in the programs, or errors will be introduced.

# Motivation
Many matplotlib APIs are hard to find, e.g. changing the font, using latex, adding annotation, mixing fonts, adding subfigures, etc.
Since the strict requirements on submissions to conferences in computer science, we actually need these features, but they are not well-documented.
Therefore, I write a sample to record these APIs to avoid searching for them again when we need them.
