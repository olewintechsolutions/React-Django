

@app.route('/') 
def index(): 
	return render_template('index.html') 


@app.route('/navbarpage') 
def navpage(): 
	return render_template('navbarpage.html') 


if __name__ == '__main__': 
	app.run()
