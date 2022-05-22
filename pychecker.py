import os
import sys



'''
PyChecker

Protect your Python code from any malware, viruses or unwanted functionality.
See what's up.

Cybersecurity is a team sport. 
Don't wait. Contribute.


ZPXD, Łukasz Pintal.
'''



class PyChecker():
	
	# Paths.
	landing_main_folder = 'file_landing'
	pychecker_default = '/home/{}'

	landing_folder = 'landing'
	ok_folder = 'ok'
	not_now_folder = 'not_now'
	not_yet_folder = 'not_yet'
	hall_of_fame_folder = 'hall_of_fame'

	# Lists.
	black_list_keywords = [] 

	# Commands:
	git_clone = 'git clone {} {}'
	
	def __init__(self, file_landing=None):	
		if file_landing:
			self.file_landing = file_landing
		else:
			self.file_landing = self.file_landing_default.format(os.getlogin()) + '/' + self.landing_main_folder


	# Paths, folders, prequisites, setup.
	
	def setup_paths(self):
		'''
		.
		'''
		self.landing_folder_path = self.file_landing + '/' + self.landing_folder
		self.ok_folder_path = self.file_landing + '/' + self.ok_folder
		self.not_now_folder_path = self.file_landing + '/' + self.not_now_folder
		self.not_yet_folder_path = self.file_landing + '/' + self.not_yet_folder
		self.hall_of_fame_folder_path = self.file_landing + '/' + self.hall_of_fame_folder

	def setup_folders(self):
		'''
		.
		'''
		if not os.path.exists(self.file_landing):
			os.mkdir(self.file_landing)
		if not os.path.exists(self.landing_folder_path):
			os.mkdir(self.landing_folder_path)
		if not os.path.exists(self.ok_folder_path):
			os.mkdir(self.ok_folder_path)
		if not os.path.exists(self.not_now_folder_path):
			os.mkdir(self.not_now_folder_path)
		if not os.path.exists(self.not_yet_folder_path):
			os.mkdir(self.not_yet_folder_path)
		if not os.path.exists(self.hall_of_fame_folder_path):
			os.mkdir(self.hall_of_fame_folder_path)


	def setup_prequisites(self):
		'''
		.
		'''
		pass


	def setup(self):
		'''
		.
		'''
		self.setup_paths()
		self.setup_folders()
		self.setup_prequisites()


	# Open files to check.

	def check_folder(self, folder_path):
		'''
		.
		'''
		return None

	def check_files(self, files=[]):
		'''
		.
		'''
		pass
		
	def check_file(self, file_path):
		'''
		.
		'''
		with open(file_path, 'w+') as wtf:
			file_lines = wtf.readlines()
		return file_lines


	# Files operations.

	def self.list_all_folder_files(self, what):
		'''
		.
		'''s
		pass

	def is_folder(self, what):
		'''
		.
		'''
		result = None
		return result

	def move_to(self, what, where):
		'''
		.
		'''
		if is_folder(what):
			command = 'cp -r {} {}'.format(what, where)
		else:
			command = 'cp {} {}'.format(what, where)
		os.system(command)




	# Git:

	def get_git_repo(self, repo, credentials=None):
		'''
		.
		'''
		what = repo
		where = self.file_landing
		if not credentials:
			command = git_clone.format(what, where)
		else:
			# TBD.
			command = git_clone.format(what, where)
		os.system(command)

	def git_is_folder(self):
		'''
		.
		'''
		pass

	def git_file_by_url(self):
		'''
		.
		'''
		pass

	def git_folder_by_url(self):
		'''
		.
		'''
		pass


	# Internet.

	def get_internet_file(self,):
		'''
		.
		'''
		pass



	# Anything downloaded.

	def file_landing(self):
		'''
		.
		'''
		pass

	def create_test_environment(self):
		'''
		.
		'''
		pass



	# Checks - Python.

	def black_list_keywords(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def any_downloads(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def any_uploads(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def any_connections(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def any_file(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def any_software_use(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def any_hardware_use(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def any_system_interactions(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def any_processes(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def check_libraries(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def check_libraries_source_code(self):
		'''
		.
		'''
		result = None
		foundings = []
		founding = {
			'what' : '',
			'type' : '',
			'line' : '',
			'path' : '',
			'file' : '',
		}
		return result, foundings

	def check_py_file(self, file_path):
		'''
		.
		'''
		f = {}

		f['result'] = None
		f['results'] = []

		result, foundings = self.black_list_keywords(file_path)
		f['keywords'] = foundings
		f['results'].append(result)

		result, foundings = self.any_downloads(file_path)
		f['downloads'] = foundings
		f['results'].append(result)

		result, foundings = self.any_uploads(file_path)
		f['uploads'] = foundings
		f['results'].append(result)

		result, foundings = self.any_connections(file_path)
		f['connections'] = foundings
		f['results'].append(result)

		result, foundings = self.any_file(file_path)
		f['software'] = foundings
		f['results'].append(result)

		result, foundings = self.any_software_use(file_path)
		f['hardware'] = foundings
		f['results'].append(result)

		result, foundings = self.any_hardware_use(file_path)
		f['system'] = foundings
		f['results'].append(result)

		result, foundings = self.any_system_interactions(file_path)
		f['system'] = foundings
		f['results'].append(result)

		result, foundings = self.any_processes(file_path)
		f['processes'] = foundings
		f['results'].append(result)

		result, foundings = self.check_libraries(file_path)
		f['libraries'] = foundings
		f['results'].append(result)

		#result, foundings = self.check_libraries_source_code(file_path)
		#f[''] = foundings

		f['result'] = any(f['results'])

		return f['result'], f


	def check_bash_file(self):
		'''
		.
		'''
		pass

	def check_config_file(self):
		'''
		.
		'''
		pass

	def check_data_file(self):
		'''
		.
		'''
		pass

	def check_text_file(self):
		'''
		.
		'''
		pass

	def check_other_file(self):
		'''
		.
		'''
		pass


	# File type decider.
	def what_is_this_file():
		pass




	# Check.

	def check_listed(self, what, check_options):
		'''
		.
		'''
		check_list = open(what).readlines()
		self.check_it(check_list)

	def check_it(self, what=None, check_options):
		'''
		Performs all checks on given path.
		'''

		# What. List files to check.
		if not what:
			what = self.landing_folder_path
		if isinstance(what, list):
			files = []
			for link in what:
				files.append(self.list_all_folder_files(what))
		else:
			if is_folder(what):
				files = self.list_all_folder_files(what)
			else:
				files = [what]

		# Result informations structure.
		check_results = {}
		check_results['result'] = None
		check_results['results'] = [] # {}
		check_results['files'] = []

		for file in files:
			# What file is this? Check it.
			file_type = what_is_this_file(file)
			if file_type == 'python':
				result, foundings = self.check_py_file()
			elif file_type == 'bash':
				result, foundings = self.check_bash_file()
			elif file_type == 'config':
				result, foundings = self.check_config_file()
			elif file_type == 'data':
				result, foundings = self.check_data_file()
			elif file_type == 'text':
				result, foundings = self.check_text_file()
			elif file_type == 'other':
				result, foundings = self.check_other_file()

			file_check = {}
			file_check['path'] = file
			file_check['result'] = result
			file_check['type'] = file_type
			file_check['foundings'] = foundings

			results['results'].append(result)
			results['files'].append(file_check)

		check_results['result'] = all(check_results['results'])

		# Result
		self.result(check_results, check_options)


	def results(self, check_results, check_options=None):

		if check_options:
			print('Alfa PyChecker use is with no config for now.')
			pass

		# Default result:
		# 1. YES / NO
		# 2. Print reasons.
		# 3. 
		else:
			for file in check_results['files']:
				if file['result'] > 0:
					print(file['result']. file['path'])
					for k, v in file['foundings'].items():
						if len(file['foundings'][key]) > 0:
							for i, wtf in enumerate(file['foundings'][key], 1):
								print(i, file['foundings'][key]['line'])
			return check_results['result']



	# What's up?






if __name__ == '__main__':


	# 1. Intro.

	print()
	print('Pychecker.')
	print()


	# 2. Basic sequence.

	WTF = PyChecker()
	WTF.setup()


	'''
	3. What.

	- a. no arguments default - file landing.
	- b. given folder / file
	- c. list of folders / files
	- d. repo / repo files
	- e. internet folder / file
	'''

	# a. default. Check whole landing.
	if len(sys.argv) == 1:
		what = 'landing'
		WTF.check_it(what)
	
	# b. check given file or folder.
	elif len(sys.argv) == 2 or '-c' in sys.argv:
		what = sys.argv[1]
		if '-c' in sys.argv:
			i = sys.arvg.find('-c')
			what = sys.argv[i+1]
		WTF.check_it(what)
	
	# c. path to file with listed files and/or folders paths to check.
	elif '-cf' in sys.argv:
		i = sys.arvg.find('-cf')
		what = sys.argv[i+1]
		WTF.check_listed(what)

	# d. repo / repo files.
	elif '-g' in sys.argv:
		i = sys.arvg.find('-g')
		what = sys.argv[i+1]
		WTF.check_listed(what)

	# e. internet folder / file.
	elif '-l' in sys.argv:
		i = sys.arvg.find('-l')
		what = sys.argv[i+1]
		#WTF.check_listed(what)

	# f. usage informations.
	else:
		print('Use:')
		print('')
		print('0. no arguments - check landing.')
		print('python3 pychecker.py')
		print('')
		print('1. 1 argument - check file/folder by given path.')
		print('python3 pychecker.py /path/to/folder/file.py')
		print('')
		print('2. flag  -c <path> ---- check file(s) under given path.')
		print('python3 pychecker.py -c /path/to/folder/file.py')
		print('')
		print('3. flag -cf <path> ---- check all folders and files listed in a linked file.')
		print('python3 pychecker.py -cf /path/to/paths_list.txt')
		print('')
		print('')
		print('Keep it up. Cheers.')