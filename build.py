print('Python SSG (Static Site Generator code for HW 3)')
# listing out file names in dicts

pages = [
	{
		'filename': './content/index.html',
		'output': 'docs/index.html',
		'title': 'Home',
	},
	{
		'filename': './content/about.html',
		'output': 'docs/about.html',
		'title': 'About Me',
	},
	{
		'filename': './content/portfolio.html',
		'output': 'docs/portfolio.html',
		'title': 'Portfolio',
	},
	{
		'filename': './content/blog.html',
		'output': 'docs/blog.html',
		'title': 'Blog',
	},
	{
		'filename': './content/contact.html',
		'output': 'docs/contact.html',
		'title': 'Contact',
	},
]

# for page in pages:
# 	page_title = page['title']
# 	# used print statements to assure for loop works
# 	# print(page_title )
# 	# print(page['filename'])
# 	# print(page['output'])

# 	# defined variables outside of for loop to use as arguments for functions
# 	filename = page['filename']
# 	# print(filename)
# 	doc_output= page['output']
# 	# print(doc_output)
# 	# return filename


# this will read the contents of every page listed
# def read_in_file(filename):
# 		filename_content = open(filename).read()
# 		print(filename_content) 
# 		return filename_content

# # page_content = read_in_file(filename)

# print('------------------------------')

# # applies the base template to each of the page content 
# def apply_template(content):
# 		# read in combined top/bottom template 
# 		template = open('./templates/base.html').read()
# 	    # this assigns a finsihed page and replaces content with page_content
# 		finished_page = template.replace('{{content}}', read_in_file(page['filename']))
# 		open(page['output'], 'w+').write(finished_page)
# 		results = page['output']
# 		# print(results)
# 		# return results

print('------------------------------')

def main():
	for page in pages:
		def read_in_file(filename):
			filename_content = open(filename).read()
			print(filename_content) 
			return filename_content
			
		def apply_template(content):
					# read in combined top/bottom template 
					template = open('./templates/base.html').read()
				    # this assigns a finsihed page and replaces content with page_content
					finished_page = template.replace('{{content}}', read_in_file(page['filename']))
					open(page['output'], 'w+').write(finished_page)
					results = page['output']

		print(page['filename'])
		print('------------------------------')
		content = read_in_file(page['filename'])
		resulting_html_for_doc = apply_template(content)
		# print(resulting_html_for_doc



		# applies the base template to each of the page content 
	

	# original SSG code from previous assignment (part 2.1)
	# Top template of the webpage
	# top_html_file = open('./templates/top.html').read()
	# Bottom template of webpage
	# bottom_html_file = open('./templates/bottom.html').read()
	# Use contents dir to add the middle parts to complete the code

	# Home 
	# middle_html_file = open('./content/index.html').read()
	# combined_html_files = top_html_file + middle_html_file + bottom_html_file
	# print(combined_html_files)
	# open('index.html', 'w+').write(combined_html_files)

	# About 
	# Use contents dir to add the middle parts to complete the code
	# middle_html_file = open('./content/about.html').read()
	# combined_html_files = top_html_file + middle_html_file + bottom_html_file
	# print(combined_html_files)
	# open('about.html', 'w+').write(combined_html_files)

	# Portfolio
	# Use contents dir to add the middle parts to complete the code
	# middle_html_file = open('./content/portfolio.html').read()
	# combined_html_files = top_html_file + middle_html_file + bottom_html_file
	# print(combined_html_files)
	# open('portfolio.html', 'w+').write(combined_html_files)

	# Blog
	# Use contents dir to add the middle parts to complete the code
	# middle_html_file = open('./content/blog.html').read()
	# combined_html_files = top_html_file + middle_html_file + bottom_html_file
	# print(combined_html_files)
	# open('blog.html', 'w+').write(combined_html_files)

	# Contact
	# Use contents dir to add the middle parts to complete the code
	# middle_html_file = open('./content/contact.html').read()
	# combined_html_files = top_html_file + middle_html_file + bottom_html_file
	# print(combined_html_files)
	# open('contact.html', 'w+').write(combined_html_files)



	# String replacement templating


	# Read in the content of the index HTML page
	# index_content = open("content/index.html").read()
	# #se the string replace
	# finished_index_page = template.replace("{{content}}", index_content)
	# open("docs/index.html", "w+").write(finished_index_page)


	# Read in the content of the about HTML page
	# about_content = open("content/about.html").read()
	# Use the string replace
	# finished_about_page = template.replace("{{content}}", about_content)
	# open("docs/about.html", "w+").write(finished_about_page)


	# Read in the content of the portfolio HTML page
	# portfolio_content = open("content/portfolio.html").read()
	# Use the string replace
	# finished_portfolio_page = template.replace("{{content}}", index_content)
	# open("docs/portfolio.html", "w+").write(finished_portfolio_page)


	# Read in the content of the blog HTML page
	# blog_content = open("content/blog.html").read()
	# Use the string replace
	# finished_blog_page = template.replace("{{content}}", blog_content)
	# open("docs/blog.html", "w+").write(finished_blog_page)


	# Read in the content of the contact HTML page
	# contact_content = open("content/contact.html").read()
	# Use the string replace
	# finished_contact_page = template.replace("{{content}}", contact_content)
	# open("docs/contact.html", "w+").write(finished_contact_page)
main()
