from setuptools import setup

setup(name='ask_amy',
      version='0.1',
      description='Python framework for Alexa Skill development',
      url='https://github.com/dphiggs01/ask_amy',
      author='Dan Higgins',
      author_email='daniel.higgins@yahoo.com',
      license='MIT',
      packages=['ask_amy'],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': ['ask-amy-cli=ask_amy.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
