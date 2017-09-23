from flask import Flask
 
my_app1 = Flask(__name__)
 
@my_app1.route('/')
def root():
	print "running root man"
	return '<a href= "/foo">Go to Foo</a><br><a href= "/oof">Go to Oof</a>'

@my_app1.route('/foo')
def foo():
	retStr = ""
	for x in range(0,100):
		retStr = retStr + str(x) + "<br>"
	return retStr
	
@my_app1.route('/oof')
def bar():
	return 'oof'
	
if __name__ == '__main__':
	my_app1.debug = True
	my_app1.run()