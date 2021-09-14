#!usr\bin\env python 3


with open("file.fq") as f:

        for line in f:
                length=(len(line)-2)
                if line.startswith('@'):
                        line=line[:length]+''+line[length+1:]
                        print(line)