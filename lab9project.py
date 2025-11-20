import webbrowser
title = input('Enter the file name you would like to use (remember this will be a .html file)  : ')
headin = input('Enter the heading : ')
topicname = input('Enter your topic name : ')
paragraph = input('Enter a paragraph for your topic : ') 
avenues = input('What are 3 ways that it can be implemented? (seperate answers with a `,`) : ') 
avenuesL = avenues.split(',')

htmlfile = open(f'{title}', 'x+')
htmlfile.write(
        f'<!DOCTYPE html>\n'
        f'<html lang="en">\n'
        f'<head>\n'
	    f'  <title>{headin}</title>\n'
        f'</head>\n'
        f'<body>\n'
	    f'  <h1>{title}</h1>\n'
	    f'  <p>{paragraph}</p>\n'
	    f'    <ul>\n'
		f'        <li>{avenuesL[0]}</li>\n'
		f'        <li>{avenuesL[1]}</li>\n'
        f'        <li>{avenuesL[2]}</li>\n'
        f'    </ul>\n'
        f'</body> \n'
        f'</html>\n')
webbrowser.open('practiceHTML11-8-25.html')
