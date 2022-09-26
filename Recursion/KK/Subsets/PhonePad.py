# Q) Leetcode Link :-


def pad(processed,unprocessed):
    if len(unprocessed)==0:
        print(processed)
        return

    digit = int(unprocessed[0])  # converted into integer as we need to use this to define our range.

    for i in range((digit-1)*3,digit*3):
        char_to_add_in_processed = chr(i + ord('a'))
        pad(processed+char_to_add_in_processed,unprocessed[1:])


# pad("","12")


# Q) With Return.

def padRet(processed, unprocessed):
    if len(unprocessed) == 0:
        final_list = []
        final_list.append(processed[:])
        return final_list

    digit = int(unprocessed[0])  # converted into integer as we need to use this to define our range.

    l1 = []

    for i in range((digit - 1) * 3, digit * 3):
        char_to_add_in_processed = chr(i + ord('a'))
        l1.extend(padRet(processed + char_to_add_in_processed, unprocessed[1:]))
        # l1.extend(ans)

    return l1


print(padRet("", ""))

# Q) in argument (This code is not working.

def padRetInArg(processed, unprocessed,final_list):
    if len(unprocessed) == 0:
        # final_list = []
        # final_list.append(processed[:])
        return final_list

    digit = int(unprocessed[0])  # converted into integer as we need to use this to define our range.

    # l1 = []

    # if digit==1:
    #     return []


    for i in range((digit - 1) * 3, digit * 3):
        char_to_add_in_processed = chr(i + ord('a'))
        final_list.extend(processed + char_to_add_in_processed)
        padRetInArg(processed + char_to_add_in_processed, unprocessed[1:],final_list)
        # l1.extend(ans)

    # return l1


print(padRetInArg("", "23",[]))