
import numpy as np




def returnstat(sum_pos,sum_neg):
        
    
    
    positives=['that is fine. try to be a little more cheerful and positive',
               'okay.that sounds fine.Be Happy',
               'YOLO. stay happy stay cheerful.',
               'An apple a day keeps the doctor away, but you dont try to keep your happiness away.Bring it back.',
               'Cheers to life , you are borderline positive in life',
               'Very nice. so positive',
               'Even I can smell the positivity in the air',
               'WOW.that is great going',
               'Thankyou.Hope others have a beautfiul day just like you have yours with this kind of mood',
               'Wakanda Forever. You are a king.']
    
    negatives=['noooooo. dont be so negative . dont let negative thoughts win over you',
               'Naah. This is not the way mate. Try to be cheerful',
               'Try to talk with someone. It"ll help to uplift your mood',
               'There are bad days and good days. But dont you every think that this is the end and stay negative',
               'There will be good days. Try to be happy',
               'it seems you have a very negative mood']
    
    if (sum_pos - sum_neg)> 0 and (sum_pos - sum_neg)<5 :
        stat=positives[np.random.randint(0,5)]
    if (sum_pos - sum_neg) >= 5:
        stat=positives[np.random.randint(5,9)]
    if (sum_pos - sum_neg) < 0:
        stat=negatives[np.random.randint(0,5)]
    if (sum_pos - sum_neg) == 0:
        stat="this is a neutral statement"
    
        
    return stat