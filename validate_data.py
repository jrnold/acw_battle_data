from goodtables import processors
import datapackage
import os


system_path = os.getcwd()
src_folder = 'data'
files = []
filenames = os.listdir(os.path.join(system_path, src_folder))
for file in filenames:
	if file.endswith('.csv'):
		files.append(file)

schema = 'datapackage.json'
schemafile = os.path.join(system_path, src_folder, schema)
dp = datapackage.DataPackage(schemafile)
try:
	dp.validate()
except datapackage.exceptions.ValidationError as e:
	pass

# processor is currently giving an invalid schema error
processor = processors.SchemaProcessor(format='csv', schema=schemafile)
for file in files:
	print(file)
	datafile = os.path.join(system_path, src_folder, file)
	valid, report, data = processor.run(datafile)
	output_format = 'txt'
	exclude = ['result_context', 'processor', 'row_name', 'result_category', 'column_index', 'column_name', 'result_level']
	# This was generating an I/O error
	out = report.generate(output_format, exclude=exclude)
	print(out)