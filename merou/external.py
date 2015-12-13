import urllib
import os

def download_files(params):
    target_dir = os.path.join(params['output_path'], params['project_name'].lower(), 'external')
    os.mkdir(target_dir)
    try:
        urllib.urlretrieve('https://raw.githubusercontent.com/philsquared/Catch/master/single_include/catch.hpp',
                           os.path.join(target_dir, 'catch.hpp'))
        urllib.urlretrieve('https://raw.githubusercontent.com/philsquared/Catch/master/LICENSE_1_0.txt',
                           os.path.join(target_dir, 'Catch_LICENSE_1_0.txt'))
        print '  catch.hpp downloaded. Please consult: ' + target_dir + '/Catch_LICENSE_1_0.txt for its licensing information'
    except IOError as e:
        print
        print 'Couldn\'t download Catch header. Unit testing will not be functional in the new project.'
        print 'To enable unit testing, please download catch.hpp from: ',
        print 'https://raw.githubusercontent.com/philsquared/Catch/master/single_include/catch.hpp ',
        print 'and save it in the "external" folder of your new project root.'
        print

