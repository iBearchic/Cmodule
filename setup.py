from distutils.core import setup, Extension

module1 = Extension( 
	'my_mod', # module name in interpreter
	sources = ['mymod.c'] 
)

setup( 
	name = 'my_mod',
	version = '1.1',
	description = 'Simple module',
	ext_modules= [module1]
)