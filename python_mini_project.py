from math import sqrt



def binomial_test(sample_proportion,proportion_we_want_to_check, confidence_level,sample_size):
    dictionaire = { 0.95:1.96 , 0.9 :1.645 , 0.99:2.576 ,0.98 :2.33 , 0.80 : 1.282 }
    if confidence_level in dictionaire:
        C_I_low = sample_proportion - dictionaire[confidence_level]*sqrt(sample_proportion*(1-sample_proportion)/sample_size)
        C_I_upper = sample_proportion + dictionaire[confidence_level]*sqrt(sample_proportion*(1-sample_proportion)/sample_size)
        print("the calculated C.I. is...",({C_I_low,C_I_upper}))
        if  C_I_low <= proportion_we_want_to_check <=C_I_upper :
            print("since proportion_we_want_to_check is in the range of C.I.low and C.I.upper ,there is not enough evidence to reject the idea of the true population proportion is likely have the value of proportion_we_want_to_check")
        else:
            print("since proportion_we_want_to_check is not in the range of C.I.low and C.I.upper ,there is enough evidence to reject the idea of the true population proportion is not mostly to have the value of proportion_we_want_to_check")
    else:   
        print("there is error inthe input, please check it!")