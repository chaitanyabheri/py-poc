import gzip
import io
import os
import shutil


file_path = os.path.dirname(__file__) + '/athena-ug.pdf'
file_path_gz = os.path.dirname(__file__) + '/athena-ug.pdf.gz'

with open(file_path,'rb') as f_in:
    with gzip.open(file_path_gz, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


