import PyPDF2
import sys 
import os




def main():
    print("Hello from pdf-merger!")

    merger = PyPDF2.PdfMerger()

    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):

            merger.append(file)
        merger.write("ML_Fundamentals.pdf")
    print("PDFs merged successfully")



if __name__ == "__main__":
    main()
