import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Leer CSV con manejo de errores
book = pd.read_csv('books_of_the_decade.csv')
user_reviews = pd.read_csv('user_reviews_dataset.csv')

books = pd.merge(user_reviews, book, left_on='bookIndex', right_on='Index', how='inner')
print(books.head(10))

top_ten_books = book.sort_values(by='Score', ascending=False).head(10)
print(top_ten_books)

top_ten_books_vote = book.sort_values(by='Number of Votes', ascending=False).head(10)
print(top_ten_books_vote)

books['Rating'] = pd.to_numeric(books['Rating'], errors='coerce')
books['Number of Votes'] = pd.to_numeric(books['Number of Votes'], errors='coerce')
# Filling null values in 'Rating' with the median rating
median_rating = books['Rating'].median()
books['Rating'].fillna(median_rating, inplace=True)

# Filling null values in 'Number of Votes' with 0
books['Number of Votes'].fillna(0, inplace=True)
books['Book Name'].value_counts()
book_authors=books['Author'].value_counts()
print(book_authors)

# Authors with more than one books
author_counts = books['Author'].value_counts()

multiple_books_authors = author_counts[author_counts > 1].index
filtered_books = books[books['Author'].isin(multiple_books_authors)]
print(len(multiple_books_authors))

author_stats = (
    books.groupby('Author')
    .agg(
        number_of_books=('Book Name', 'count'),   # Count the number of books per author
        total_score=('Score', 'sum')              # Sum the scores of each author's books
    )
    .reset_index()
)

top_authors = author_stats.sort_values(by='total_score', ascending=False)

print('Best seller authors by total score:')
top_authors[['Author', 'number_of_books', 'total_score']].head(10)
author_stats = (
    books.groupby('Author')
    .agg(
        number_of_books=('Book Name', 'count'),   # Count the number of books per author
        total_score=('Score', 'sum')              # Sum the scores of each author's books
    )
    .reset_index()
)

top_authors = author_stats.sort_values(by='total_score', ascending=False)

print('Best seller authors by total score:')
top_authors[['Author', 'number_of_books', 'total_score']].head(10)

top_auth = top_authors['Author'].head(10)
top_scr= top_authors['total_score'].head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_scr.values, y=top_auth.values , palette='viridis')
plt.title('Top 10 Authors by Total Score')
plt.xlabel('Total_score')
plt.ylabel('Author')
plt.show()

print("Best seller authors by Number of books in the data:")

top_author_by_books = author_stats.sort_values(by='number_of_books', ascending=False)
top_author_by_books

top_author_by_books = books['Author'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_author_by_books.values, y=top_author_by_books.index, palette='viridis')
plt.title('Top 10 Authors by Number of Books')
plt.xlabel('Number of Books')
plt.ylabel('Author')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(books['Rating'], kde=True, color='blue')
plt.title('Distribution of Book Ratings')
plt.xlabel('Rating')
plt.show()


plt.figure(figsize=(8, 6))
sns.heatmap(books[['Rating', 'Number of Votes', 'Score']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

author_counts = books['Author'].value_counts().head(10)

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(author_counts, labels=author_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Ratings')
plt.show()
