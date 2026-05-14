import sys
with ( open( sys.argv[1], "r"  ) as myfile1, 
       open( sys.argv[2], "a"  ) as myfile2 ):
    for line in myfile1:
        myfile2.write(line)

