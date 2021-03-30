# Top template of the webpage
top_html_file = open('./templates/top.html').read()

# Bottom template of webpage
bottom_html_file = open('./templates/bottom.html').read()

# Use contents dir to add the middle parts to complete the code
# Currently Home 
middle_html_file = open('./content/Home.html').read()

print('HTML files combined')

combined_html_files = top_html_file + middle_html_file + bottom_html_file
print(combined_html_files)

open('Home.html', 'w+').write(combined_html_files)


# About 
# Use contents dir to add the middle parts to complete the code
middle_html_file = open('./content/about.html').read()

print('HTML files combined')

combined_html_files = top_html_file + middle_html_file + bottom_html_file
print(combined_html_files)

open('about.html', 'w+').write(combined_html_files)

# Portfolio
# Use contents dir to add the middle parts to complete the code
middle_html_file = open('./content/portfolio.html').read()

print('HTML files combined')

combined_html_files = top_html_file + middle_html_file + bottom_html_file
print(combined_html_files)

open('portfolio.html', 'w+').write(combined_html_files)

# Blog
# Use contents dir to add the middle parts to complete the code
middle_html_file = open('./content/blog.html').read()

print('HTML files combined')

combined_html_files = top_html_file + middle_html_file + bottom_html_file
print(combined_html_files)

open('blog.html', 'w+').write(combined_html_files)

# Contact
# Use contents dir to add the middle parts to complete the code
middle_html_file = open('./content/contact.html').read()

print('HTML files combined')

combined_html_files = top_html_file + middle_html_file + bottom_html_file
print(combined_html_files)

open('contact.html', 'w+').write(combined_html_files)