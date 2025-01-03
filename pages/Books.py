import mysql.connector
import streamlit as st
import pandas as pd

# Display the title in Streamlit
st.title('To Explorer the BookScape')

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",         # Hostname of the MySQL server
    user="root",              # Your MySQL username
    port=3306,
    password="Dinesh2802",    # Your MySQL password
    database="books_explorer"  # Name of the database
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

cursor.execute('USE books_explorer')

# Fetch the Check Availability of eBooks vs Physical Books
cursor.execute('''
    SELECT
    is_ebook,
    COUNT(*) AS book_count
    FROM books
    GROUP BY is_ebook;
''')
# Fetch the results for show availability of eBooks vs Physical Books
table1 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_1 = pd.DataFrame(table1, columns=["is_ebook", "book_count"])

# Fetch Find the Publisher with the Most Books Published
cursor.execute('''
    SELECT publisher, COUNT(*) AS book_count
    FROM books
    GROUP BY publisher
    ORDER BY book_count DESC
    LIMIT 10;
''')
# Fetch the results for Publisher with the Most Books Published
table2 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_2 = pd.DataFrame(table2, columns=["publisher", "book_count"])

# Fetch Identify the Publisher with the Highest Average Rating
cursor.execute('''
    SELECT publisher, AVG(average_rating) AS avg_rating
    FROM books
    GROUP BY publisher
    ORDER BY avg_rating DESC
    LIMIT 1;
''')
# Fetch the results for Publisher with the Highest Average Rating
table3 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_3 = pd.DataFrame(table3, columns=["publisher", "avg_rating"])

# Fetch Get the Top 5 Most Expensive Books by Retail Price
cursor.execute('''
    SELECT title, retail_price_amount, retail_price_currency
    FROM books
    ORDER BY retail_price_amount DESC
    LIMIT 5;
''')
# Fetch the results for Top 5 Most Expensive Books
table4 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_4 = pd.DataFrame(table4, columns=["title", "retail_price_amount", "retail_price_currency"])

# Fetch Find Books Published After 2010 with at Least 500 Pages
cursor.execute('''
    SELECT title, published_date, page_count
    FROM books
    WHERE published_date > '2010-01-01' AND page_count >= 500;
''')
# Fetch the results for Books Published After 2010 with at Least 500 Pages
table5 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_5 = pd.DataFrame(table5, columns=["title", "published_date", "page_count"])

# Fetch List Books with Discounts Greater than 20%
cursor.execute('''
    SELECT title, list_price_amount, retail_price_amount
    FROM books
    WHERE (list_price_amount - retail_price_amount) / list_price_amount > 0.2;
''')
# Fetch the results for Books with Discounts Greater than 20%
table6 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_6 = pd.DataFrame(table6, columns=["title", "list_price_amount", "retail_price_amount"])

# Fetch Find the Average Page Count for eBooks vs Physical Books
cursor.execute('''
    SELECT is_ebook, AVG(page_count) AS avg_page_count
    FROM books
    GROUP BY is_ebook;
''')
# Fetch the results for Average Page Count for eBooks vs Physical Books
table7 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_7 = pd.DataFrame(table7, columns=["is_ebook", "avg_page_count"])

# Fetch Find the Top 3 Authors with the Most Books
cursor.execute('''
    SELECT authors, COUNT(*) AS book_count
    FROM books
    GROUP BY authors
    ORDER BY book_count DESC
    LIMIT 3;
''')
# Fetch the results for Top 3 Authors with the Most Books
table8 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_8 = pd.DataFrame(table8, columns=["authors", "book_count"])

# Fetch List Publishers with More than 10 Books
cursor.execute('''
    SELECT publisher, COUNT(*) AS book_count
    FROM books
    GROUP BY publisher
    HAVING COUNT(*) > 10;
''')
# Fetch the results for Publishers with More than 10 Books
table9 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_9 = pd.DataFrame(table9, columns=["publisher", "book_count"])

# Fetch Find the Average Page Count for Each Category
cursor.execute('''
    SELECT categories, AVG(page_count) AS avg_page_count
    FROM books
    GROUP BY categories;
''')
# Fetch the results for Average Page Count for Each Category
table10 = cursor.fetchall()

# Convert the results to pandas DataFrame
answer_10 = pd.DataFrame(table10, columns=["categories", "avg_page_count"])

# 11. Retrieve Books with More than 3 Authors
cursor.execute('''
    SELECT title, authors
    FROM books
    WHERE LENGTH(authors) - LENGTH(REPLACE(authors, ',', '')) + 1 > 3;
''')
table11 = cursor.fetchall()
answer_11 = pd.DataFrame(table11, columns=["title", "authors"])

# 12. Books with Ratings Count Greater Than the Average
cursor.execute('''
    SELECT title, ratings_count
    FROM books
    WHERE ratings_count > (SELECT AVG(ratings_count) FROM books);
''')
table12 = cursor.fetchall()
answer_12 = pd.DataFrame(table12, columns=["title", "ratings_count"])

# 13. Books with the Same Author Published in the Same Year
cursor.execute('''
    SELECT a.title, a.authors, a.published_date
    FROM books a
    JOIN books b ON a.authors = b.authors
    WHERE YEAR(a.published_date) = YEAR(b.published_date) AND a.id != b.id;
''')
table13 = cursor.fetchall()
answer_13 = pd.DataFrame(table13, columns=["title", "authors", "published_date"])

# 14. Books with a Specific Keyword in the Title
keyword = "Python"  # Example keyword, replace as needed
cursor.execute(f'''
    SELECT title, authors
    FROM books
    WHERE title LIKE '%Python%';
''')
table14 = cursor.fetchall()
answer_14 = pd.DataFrame(table14, columns=["title", "authors"])

# 15. Year with the Highest Average Book Price
cursor.execute('''
    SELECT YEAR(published_date) AS year, AVG(retail_price_amount) AS avg_price
    FROM books
    GROUP BY year
    ORDER BY avg_price DESC
    LIMIT 1;
''')
table15 = cursor.fetchall()
answer_15 = pd.DataFrame(table15, columns=["year", "avg_price"])

# 16. Count Authors Who Published 3 Consecutive Years
cursor.execute('''
    SELECT authors, COUNT(DISTINCT (published_date)) AS year_count
    FROM books
    GROUP BY authors
    HAVING year_count = 3;
''')
table16 = cursor.fetchall()
answer_16 = pd.DataFrame(table16, columns=["authors", "year_count"])

# 17. Authors Who Published Books in the Same Year But Under Different Publishers
cursor.execute('''
    SELECT authors, YEAR(published_date) AS year, COUNT(DISTINCT publisher) AS publisher_count
    FROM books
    GROUP BY authors, YEAR(published_date)
    HAVING publisher_count > 1;
''')
table17 = cursor.fetchall()
answer_17 = pd.DataFrame(table17, columns=["authors", "year", "publisher_count"])

# 18. Average Retail Price of eBooks and Physical Books
cursor.execute('''
    SELECT 
        AVG(CASE WHEN is_ebook = 1 THEN retail_price_amount ELSE NULL END) AS avg_ebook_price,
        AVG(CASE WHEN is_ebook = 0 THEN retail_price_amount ELSE NULL END) AS avg_physical_price
    FROM books;
''')
table18 = cursor.fetchall()
answer_18 = pd.DataFrame(table18, columns=["avg_ebook_price", "avg_physical_price"])

# 19. Books More Than Two Standard Deviations Away from the Average Rating
cursor.execute('''
    SELECT title, average_rating, ratings_count
    FROM books
    WHERE ABS(average_rating - (SELECT AVG(average_rating) FROM books)) > 2 * (SELECT STDDEV(average_rating) FROM books);
''')
table19 = cursor.fetchall()
answer_19 = pd.DataFrame(table19, columns=["title", "average_rating", "ratingsCount"])

# 20. Publisher with the Highest Average Rating for Publishers with More Than 10 Books
cursor.execute('''
    SELECT publisher, AVG(average_rating) AS avg_rating, COUNT(*) AS book_count
    FROM books
    GROUP BY publisher
    HAVING COUNT(*) > 10
    ORDER BY avg_rating DESC
    LIMIT 1;
''')
table20 = cursor.fetchall()
answer_20 = pd.DataFrame(table20, columns=["publisher", "avg_rating", "book_count"])


# Button to trigger query execution for different options
selected_option = st.multiselect('Select any Question', 
                                ['1.Check Availability of eBooks vs Physical Books',
                                 '2.Find the Publisher with the Most Books Published',
                                 '3.Identify the Publisher with the Highest Average Rating',
                                 '4.Get the Top 5 Most Expensive Books by Retail Price',
                                 '5.Find Books Published After 2010 with at Least 500 Pages',
                                 '6.List Books with Discounts Greater than 20%',
                                 '7.Find the Average Page Count for eBooks vs Physical Books',
                                 '8.Find the Top 3 Authors with the Most Books',
                                 '9.List Publishers with More than 10 Books',
                                 '10.Find the Average Page Count for Each Category',
                                 '11.Retrieve Books with More than 3 Authors',
                                 '12.Books with Ratings Count Greater Than the Average',
                                 '13.Books with the Same Author Published in the Same Year',
                                 '14.Books with a Specific Keyword in the Title',
                                 '15.Year with the Highest Average Book Price',
                                 '16.Count Authors Who Published 3 Consecutive Years',
                                 '17.Authors Who Published Books in the Same Year But Under Different Publishers',
                                 '18.Average Retail Price of eBooks and Physical Books',
                                 '19.Books More Than Two Standard Deviations Away from the Average Rating',
                                 '20.Publisher with the Highest Average Rating for Publishers with More Than 10 Books'
                                 ])

if '1.Check Availability of eBooks vs Physical Books' in selected_option and st.button('Execute'):
    st.subheader('Show Availability of eBooks vs Physical Books')
    st.dataframe(answer_1)

elif '2.Find the Publisher with the Most Books Published' in selected_option and st.button('Execute'):
    st.subheader('Top 10 Publisher with the Most Books Published')
    st.dataframe(answer_2)

elif '3.Identify the Publisher with the Highest Average Rating' in selected_option and st.button('Execute'):
    st.subheader('Publisher with the Highest Average Rating')
    st.dataframe(answer_3)

elif '4.Get the Top 5 Most Expensive Books by Retail Price' in selected_option and st.button('Execute'):
    st.subheader('Top 5 Most Expensive Books')
    st.dataframe(answer_4)

elif '5.Find Books Published After 2010 with at Least 500 Pages' in selected_option and st.button('Execute'):
    st.subheader('Books Published After 2010 with at Least 500 Pages')
    st.dataframe(answer_5)

elif '6.List Books with Discounts Greater than 20%' in selected_option and st.button('Execute'):
    st.subheader('Books with Discounts Greater than 20%')
    st.dataframe(answer_6)

elif '7.Find the Average Page Count for eBooks vs Physical Books' in selected_option and st.button('Execute'):
    st.subheader('Average Page Count for eBooks vs Physical Books')
    st.dataframe(answer_7)

elif '8.Find the Top 3 Authors with the Most Books' in selected_option and st.button('Execute'):
    st.subheader('Top 3 Authors with the Most Books')
    st.dataframe(answer_8)

elif '9.List Publishers with More than 10 Books' in selected_option and st.button('Execute'):
    st.subheader('Publishers with More than 10 Books')
    st.dataframe(answer_9)

elif '10.Find the Average Page Count for Each Category' in selected_option and st.button('Execute'):
    st.subheader('Average Page Count for Each Category')
    st.dataframe(answer_10)

elif '11.Retrieve Books with More than 3 Authors' in selected_option and st.button('Execute'):
    st.subheader('Books with More Than 3 Authors')
    st.dataframe(answer_11)

elif '12.Books with Ratings Count Greater Than the Average' in selected_option and st.button('Execute'):
    st.subheader('Books with Ratings Count Greater Than the Average')
    st.dataframe(answer_12)

elif '13.Books with the Same Author Published in the Same Year' in selected_option and st.button('Execute'):
    st.subheader('Books with Same Author Published in the Same Year')
    st.dataframe(answer_13)

elif '14.Books with a Specific Keyword in the Title' in selected_option and st.button('Execute'):
    st.subheader('Books with Keyword in the Title')
    st.dataframe(answer_14)

elif '15.Year with the Highest Average Book Price' in selected_option and st.button('Execute'):
    st.subheader('Year with the Highest Average Book Price')
    st.dataframe(answer_15)

elif '16.Count Authors Who Published 3 Consecutive Years' in selected_option and st.button('Execute'):
    st.subheader('Authors Who Published in 3 Consecutive Years')
    st.dataframe(answer_16)

elif '17.Authors Who Published Books in the Same Year But Under Different Publishers' in selected_option and st.button('Execute'):
    st.subheader('Authors Who Published in the Same Year under Different Publishers')
    st.dataframe(answer_17)

elif '18.Average Retail Price of eBooks and Physical Books' in selected_option and st.button('Execute'):
    st.subheader('Average Retail Price of eBooks and Physical Books')
    st.dataframe(answer_18)

elif '19.Books More Than Two Standard Deviations Away from the Average Rating' in selected_option and st.button('Execute'):
    st.subheader('Books with Ratings More Than Two Standard Deviations from Average')
    st.dataframe(answer_19)

elif '20.Publisher with the Highest Average Rating for Publishers with More Than 10 Books' in selected_option and st.button('Execute'):
    st.subheader('Publisher with Highest Average Rating')
    st.dataframe(answer_20)


# Close the database connection
cursor.close()
conn.close()
