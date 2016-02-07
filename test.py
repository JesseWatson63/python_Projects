        # try to remove duplicate recipient user.
        # special case when last recipient entry gets duplicated
        try:
            return_list = []
            for recip in recipients:
                if recip not in return_list:
                    return_list.append(recip)
            recipients = return_list
            #if recipients and recipients[-1] == recipients[-2]:
                #recipients = recipients[:-1]
        except IndexError:
            pass

        temp_list = []
        for index in range(1, count + 1):
            email_tag_id = 'toemail' + str(index)
            email_address = value_dict.get(email_tag_id, "")
            if email_address not in temp_list:
                temp_list.append(email_address)
        print temp_list
