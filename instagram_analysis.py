import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Impressions':,
    'From Home':,
    'From Explore':,
    'Likes':,
    'Comments':,
    'Post_Type': ['Photo', 'Reel', 'Photo', 'Reel', 'Carousel', 'Reel', 'Carousel']
}
df = pd.DataFrame(data)

plt.figure(figsize=(6, 4))
sns.barplot(x='Post_Type', y='Impressions', data=df, errorbar=None, palette='magma')
plt.title('Instagram Reach by Post Type')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.barplot(x='Post_Type', y='Likes', data=df, errorbar=None, palette='Blues_d')
plt.title('Likes by Post Type')
plt.subplot(1, 2, 2)
sns.barplot(x='Post_Type', y='Comments', data=df, errorbar=None, palette='Oranges_d')
plt.title('Comments by Post Type')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Impressions', y='Likes', hue='Post_Type', data=df, s=200)
plt.title('Relationship between Impressions and Likes')
plt.grid(True)
plt.tight_layout()
plt.show()
