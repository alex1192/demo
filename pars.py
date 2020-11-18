from bs4 import BeautifulSoup
import lxml, requests,time 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS

def plot_cloud(x):
	plt.figure(figsize = (40,30))
	plt.imshow(x)
	plt.savefig('gg.png')
	plt.show()
	plt.axis('off')
	plt.close('num')
def pars_google():
	url = requests.get('https://news.google.com/search?q=Russia&hl=en-US&gl=US&ceid=US%3Aen')
	result = url.content
	soup = BeautifulSoup(result, 'lxml')
	news = soup.find_all('div', jslog='93789')
	z =''
	for i in news:
		z+= i.find('h3').find('a').text
	wordcloud = WordCloud(width = 4000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(z)
	plot_cloud(wordcloud)
pars_google()
