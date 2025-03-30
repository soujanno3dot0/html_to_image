import imgkit


html_file=r'C:\Docs\Projects\html_to_image\env\blue_page.html'


#Install it and add path 
path_wkthmltoimage = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'

config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
options = {
            'format': 'jpg',
            'quality': '40'
        }

# From File
imgkit.from_file(html_file, 'out.png', config=config, options=options)

# from string
#imgkit.from_string("<html><title></title></html>", 'out.png', config=config, options=options)



