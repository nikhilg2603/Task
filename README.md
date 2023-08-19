
# Approach 1
We first convert each page of the pdf to an image. Then for each image we wil devide the page into number of images based on different lines or different font sizes to improve accuracy in formatting. Using the pytesseract library we will first estimate the font size based on the contour width of each of this sub image. Also using the same ibrary we will conver the image into text. Then using the function len(lstrip()) we will find the indentaion of each sentence.
We then use the html_file.write() function to convert the given text to html format where for each line now we have the indentaionand font size.
