import os
import PyPDF2

path = os.getcwd() + '\\'

files = os.listdir(path)

outputFile = open('Combained.pdf','wb')
writer = PyPDF2.PdfFileWriter()
#print(files)



try:
    for file in files:
        if(file.endswith('.pdf')):
            FilePDF = open(file,'rb')
            ReadPDF = PyPDF2.PdfFileReader(FilePDF)
            PagesPDF = ReadPDF.getNumPages()
            for page in range(PagesPDF):
                writer.addPage(ReadPDF.getPage(page))
            writer.write(outputFile)
            FilePDF.close()

except:
    print('Error on ' + file)

writer.write(outputFile)
outputFile.close()
    
print('Files have been combained into Combained.pdf')
