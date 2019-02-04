def get_maxSquare(length,width,count):

    if length==width:

        count=count+1

        return count

    else :

        if length>width:

            length=length-width

            count=count+1

            count= get_maxSquare(length,width,count)

        elif width>length:

            width=width-length

            count=count+1

            count=get_maxSquare(length,width,count)

    return count


local_count=0

max_Squares=get_maxSquare(7,4,local_count)

print(max_Squares)