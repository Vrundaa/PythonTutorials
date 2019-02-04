def get_maxSquare(length,width,count):

    if length==width:

        count=count+1

        return count

    else :
        if length-width==1 or width-length==1:
            if length>width:
                count=count+length
            elif width>length:
                count=count+width
            return count
        elif length>width:

            length=length-width

            count=count+1

            count= get_maxSquare(length,width,count)

        elif width>length:

            width=width-length

            count=count+1

            count=get_maxSquare(length,width,count)

    return count


local_count=0

max_Squares=get_maxSquare(3,3,local_count)

print(max_Squares)