# This is a sample Python script.
from nltk.probability import FreqDist
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.tokenize import wordpunct_tokenize


def w_cloud(data):
    # Use a breakpoint in the code line below to debug your script.
    mostcommon = FreqDist(data).most_common(100)
    wordcloud = WordCloud(width=1600, height=800, background_color='white').generate(str(mostcommon))
    fig = plt.figure(figsize=(30, 10), facecolor='white')
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.title('Top 100 Most Common Words', fontsize=100)
    plt.tight_layout(pad=0)
    plt.show() # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    with open('/home/ahsan/Desktop/Think T/Rough') as f:
        contents = f.read()
    data = wordpunct_tokenize(contents)
    w_cloud(data)

#ref link: https://towardsdatascience.com/preprocessing-text-data-using-python-576206753c28