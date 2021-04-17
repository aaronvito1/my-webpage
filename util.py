from jinja2 import Template
import glob 
import os

# list of files that only contains html extensions 
all_content_html_files = glob.glob("./content/*.html")
# print(all_content_html_files)
pages = [] 

def generate_list(list):
	for file in list:
		file_path = file
		# print(file_path)÷
		file_name = os.path.basename(file_path)
		# print(file_name)
		name_only, extension = os.path.splitext(file_name)
		# print(name_only)

		new_list = pages.append({
			"filename": file_path,
			"title": name_only,
			"output": 'docs/'+file_name,
			"output_filename": './'+file_name,
		})
	return new_list

generate_list(all_content_html_files)

def main():
	for page in pages:
		# def read_in_file(filename):
		# 	filename_content = open(filename).read()
		# 	print(filename_content) 
		# 	return filename_content
		def apply_template(content):
			content_html = open(content).read()
			# read in combined top/bottom template 
			# print(content_html)
			template_html = open("./templates/base.html").read()
			template = Template(template_html)
			finished_page =  template.render(
				pages= pages,
				title= page["title"],
				output= page["output"],
				content= content_html,
				output_filename= page["output_filename"]
				)
			open(page["output"], "w+").write(finished_page)
			results = page["output"]
			# # print(results)
			return results

		# print('------------------------------')
		# print(page["title"])
		# print(page["filename"])
		# print(page["output"])
		content = page["filename"]
		# print(content)
		resulting_html_for_doc = apply_template(content)

main()

# print(pages)