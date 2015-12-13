import urllib
import os

def download_files(params):
    target_dir = os.path.join(params['output_path'], params['project_name'].lower(), 'external')
    os.mkdir(target_dir)
    urllib.urlretrieve('https://raw.githubusercontent.com/philsquared/Catch/master/single_include/catch.hpp',
                       os.path.join(target_dir, 'catch.hpp'))
    urllib.urlretrieve('https://raw.githubusercontent.com/philsquared/Catch/master/LICENSE_1_0.txt',
                       os.path.join(target_dir, 'Catch_LICENSE_1_0.txt'))
    print 'Catch.hpp downloaded. Please consult: ' + target_dir + '/Catch_LICENSE_1_0.txt for its licensing information'

